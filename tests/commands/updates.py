import unittest
from tests.baseclass import CommandTest
from pykickstart.errors import KickstartParseError


class F7_TestCase(CommandTest):
    command = "updates"

    def runTest(self):
        # pass
        self.assert_parse("updates", "updates\n")
        self.assert_parse("updates deliciouscheeses", "updates deliciouscheeses\n")

        # fail
        self.assert_parse_error("updates cheese crackers", KickstartParseError, 'Kickstart command updates only takes one argument')
        self.assert_parse_error("updates --bogus-option")


class F34_TestCase(F7_TestCase):

    def runTest(self):
        # don't run F7 tests

        # pass
        self.assert_parse("updates http://path/to/img", "updates http://path/to/img\n")
        self.assert_parse("updates deliciouscheeses", "updates deliciouscheeses\n")

        # fail
        self.assert_parse_error("updates")
        self.assert_parse_error("updates cheese crackers")
        self.assert_parse_error("updates --bogus-option")


if __name__ == "__main__":
    unittest.main()
