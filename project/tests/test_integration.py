
import unittest

from project.integration import main


class IntegrationTests(unittest.TestCase):

    def test_call_main_returns_int(self):
        self.assertEqual(8, main())
