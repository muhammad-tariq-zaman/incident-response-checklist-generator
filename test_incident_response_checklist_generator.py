import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import checklist


class TestChecklists(unittest.TestCase):
    def test_known_type_not_generic(self):
        steps, generic = checklist("malware")
        self.assertFalse(generic)
        self.assertTrue(any("Isolate" in s for s in steps))

    def test_unknown_type_generic(self):
        steps, generic = checklist("meteor-strike")
        self.assertTrue(generic)
        self.assertTrue(len(steps) >= 3)

    def test_case_insensitive(self):
        self.assertEqual(checklist("MALWARE"), checklist("malware"))

    def test_outage_has_communication_step(self):
        steps, _ = checklist("outage")
        self.assertTrue(any("communication" in s for s in steps))
