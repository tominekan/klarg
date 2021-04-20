import klarg
import unittest

ALL_ARGS = [
    "--some-number",
    "10",
    "--not-number",
    "1a",
    "--number-no-args",
    "-n"
]


class TestKlarg():
    def __init__(self):
        self.test_get_all()
        self.test_get_bool()

    def test_get_all(self):
        """
        Tests that klarg.get_all() actually returns all the arguments possible

        """

        assert klarg.get_all() == ALL_ARGS

    def test_get_bool(self):
        """
        Tests that klarg.get_bool() returns if the argument exists or not.

        """

        # Tests that whena multi-letter flag is there,
        # but a single letter flag is not, klar.get_bool() returns True.
        assert klarg.get_bool("--some-number", "-s") is True

        # Tests that when both the shortened and non-shortened flags are
        # present, klarg.get_bool() returns True.
        assert klarg.get_bool("--not-number", "-n") is True

        # Tests that when a multi letter flag is not there but a shortened
        # flag is present, klarg.get_bool() returns True.
        assert klarg.get_bool("--non-existent-args", "-n") is True

        # Tests that when neither the single nor the multi letter flag is
        # present, the klarg.get_bool() returns False.
        assert klarg.get_bool("--non-existent-args", "-s") is False


TestKlarg()
print("All Tests Passed")
