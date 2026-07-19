from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "generate_index_mesh.py"


def load_module():
    spec = importlib.util.spec_from_file_location("generate_index_mesh", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GenerateIndexMeshTests(unittest.TestCase):
    def configure(self, module, root: Path, tracked: set[str], gitlinks: set[str] | None = None):
        module.ROOT = root
        module.TRACKED_FILES = tracked
        module.GITLINKS = gitlinks or set()
        module.TRACKED_DIRS = {"."}
        for item in tracked | module.GITLINKS:
            path = Path(item)
            for index in range(len(path.parts)):
                module.TRACKED_DIRS.add(Path(*path.parts[:index]).as_posix() or ".")

    def test_render_index_routes_skill_and_gitlink_leaves(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            skill = root / ".agents" / "skills" / "adventures-example"
            gitlink = root / ".agents" / "plugins" / "marketplace-source"
            docs = root / "docs"
            skill.mkdir(parents=True)
            gitlink.mkdir(parents=True)
            docs.mkdir(parents=True)
            (skill / "SKILL.md").write_text("# skill\n", encoding="utf-8")
            (gitlink / "README.md").write_text("submodule\n", encoding="utf-8")
            (docs / "guide.md").write_text("guide\n", encoding="utf-8")
            tracked = {
                ".agents/skills/adventures-example/SKILL.md",
                ".agents/plugins/marketplace-source",
                "docs/guide.md",
            }
            self.configure(module, root, tracked, {".agents/plugins/marketplace-source"})

            rendered = module.render_index(root / ".agents" / "skills")

            self.assertIn("[adventures-example](adventures-example/SKILL.md)", rendered)
            self.assertNotIn("README.md", rendered)

            plugin_rendered = module.render_index(root / ".agents" / "plugins")
            self.assertIn("[marketplace-source](marketplace-source)/", plugin_rendered)

            root_rendered = module.render_index(root)
            self.assertIn("[docs](docs/INDEX.md)", root_rendered)

    def test_lowercase_index_variant_is_not_self_listed(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            docs = root / "docs"
            docs.mkdir(parents=True)
            (docs / "index.md").write_text("legacy\n", encoding="utf-8")
            (docs / "guide.md").write_text("guide\n", encoding="utf-8")
            self.configure(module, root, {"docs/index.md", "docs/guide.md"})

            self.assertEqual(module.index_path(docs), docs / "index.md")
            rendered = module.render_index(docs)

            self.assertNotIn("[index.md]", rendered)
            self.assertIn("[guide.md](guide.md)", rendered)

    def test_shared_checkout_requires_explicit_override(self):
        module = load_module()
        module.ROOT = Path("C:/repo")

        def git_value(_root, *args):
            if "--show-superproject-working-tree" in args:
                return ""
            if "--absolute-git-dir" in args:
                return "C:/repo/.git"
            if "--git-common-dir" in args:
                return "C:/repo/.git"
            raise AssertionError(args)

        with patch.object(module, "git_output", side_effect=git_value):
            with self.assertRaisesRegex(RuntimeError, "linked worktree"):
                module.assert_write_safe(False)
            module.assert_write_safe(True)

    def test_link_validation_reports_missing_target(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            docs = root / "docs"
            docs.mkdir(parents=True)
            self.configure(module, root, {"docs/INDEX.md"})

            with patch.object(module, "repo_root", return_value=root.resolve()):
                failures = module.validate_links(docs / "INDEX.md", "- [missing](missing.md)\n")

            self.assertEqual(failures, ["broken-link: docs/INDEX.md -> missing.md"])


if __name__ == "__main__":
    unittest.main()
