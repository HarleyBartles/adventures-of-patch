"""Smoke-test the repository-specific agent mesh validator."""

import unittest

from scripts import validate_agent_mesh


class AgentMeshValidatorTests(unittest.TestCase):
    def test_current_mesh_has_no_findings(self) -> None:
        self.assertEqual([], validate_agent_mesh.collect_findings())


if __name__ == "__main__":
    unittest.main()
