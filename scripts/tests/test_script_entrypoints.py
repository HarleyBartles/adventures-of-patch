"""Keep the portable script entrypoints aligned across supported shells."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
PYTHON_BASES = (
    "generate_index_mesh",
    "install_agent_skills",
    "refresh_agent_surfaces",
    "validate_agent_mesh",
)
WRAPPER_BASES = PYTHON_BASES + ("ci-preflight",)


class ScriptEntrypointTests(unittest.TestCase):
    def test_python_entrypoints_have_bash_and_powershell_wrappers(self) -> None:
        for base in PYTHON_BASES:
            with self.subTest(base=base):
                self.assertTrue((SCRIPTS / f"{base}.py").is_file())
                self.assertTrue((SCRIPTS / f"{base}.ps1").is_file())
                self.assertTrue((SCRIPTS / f"{base}.sh").is_file())

    def test_operational_wrappers_have_strict_shell_contracts(self) -> None:
        for base in WRAPPER_BASES:
            with self.subTest(base=base):
                powershell = (SCRIPTS / f"{base}.ps1").read_text(encoding="utf-8")
                bash = (SCRIPTS / f"{base}.sh").read_text(encoding="utf-8")
                self.assertIn("Set-StrictMode", powershell)
                self.assertIn("$ErrorActionPreference = 'Stop'", powershell)
                self.assertIn("set -euo pipefail", bash)
                self.assertNotRegex(bash, r"(?i)powershell|pwsh")


if __name__ == "__main__":
    unittest.main()
