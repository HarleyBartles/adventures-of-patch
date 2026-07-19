"""Functional checks for the deterministic marketplace skill refresh."""

from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
INSTALLER_PATH = ROOT / "scripts" / "install_agent_skills.py"
MARKETPLACE_SOURCE_AVAILABLE = (ROOT / ".agents" / "plugins" / "marketplace-source").is_dir()


def load_installer_module():
    spec = importlib.util.spec_from_file_location("install_agent_skills", INSTALLER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load installer module: {INSTALLER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class InstallAgentSkillsTests(unittest.TestCase):
    @unittest.skipUnless(MARKETPLACE_SOURCE_AVAILABLE, "marketplace source is unavailable in CI")
    def test_check_mode_validates_the_current_installation(self) -> None:
        result = subprocess.run(
            [sys.executable, str(INSTALLER_PATH), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertRegex(result.stdout, r"^OK checked skills: \d+ copied from [0-9a-f]{40}$")

    @unittest.skipUnless(MARKETPLACE_SOURCE_AVAILABLE, "marketplace source is unavailable in CI")
    def test_provenance_matches_manifest_and_pinned_marketplace_revision(self) -> None:
        installer = load_installer_module()
        manifest = installer.load_manifest(installer.DEFAULT_MANIFEST_PATH)
        provenance_path = installer.DEFAULT_OUTPUT_ROOT / ".provenance.json"
        provenance = json.loads(provenance_path.read_text(encoding="utf-8"))

        self.assertEqual(provenance["local_skill_prefixes"], list(manifest.local_skill_prefixes))
        self.assertEqual(
            provenance["source_revision"],
            installer.get_git_revision(installer.DEFAULT_SOURCE_ROOT),
        )
        self.assertEqual(
            sorted(provenance["copied_skills"]),
            sorted(name for name in provenance["skill_providers"]),
        )
        self.assertTrue(
            all(
                not installer.is_local_skill_name(name, manifest.local_skill_prefixes)
                for name in provenance["copied_skills"]
            )
        )
        for path in installer.DEFAULT_OUTPUT_ROOT.rglob("*"):
            if path.is_file() and path.name != ".provenance.json":
                self.assertNotIn("harley", path.read_text(encoding="utf-8").casefold())

    def test_sync_check_rejects_a_noncanonical_output_root(self) -> None:
        installer = load_installer_module()
        manifest = installer.load_manifest(installer.DEFAULT_MANIFEST_PATH)
        with self.assertRaisesRegex(ValueError, "canonical repo-local output root"):
            installer.sync_default_skills(
                manifest,
                installer.DEFAULT_SOURCE_ROOT,
                ROOT / "tmp" / "skills",
                check=True,
            )


if __name__ == "__main__":
    unittest.main()
