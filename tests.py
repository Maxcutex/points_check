import unittest

from eno_bassey_checkpoints import Line, PointChecker


class TestPointCheck(unittest.TestCase):
    """Unit test points if they overlap"""

    def test_two_lines_do_not_over_lap(self):
        line_one = Line()
        line_one.set_points(1, 5)

        line_two = Line()
        line_two.set_points(6, 9)

        point_checker = PointChecker()
        result = point_checker.are_separate(line_one.get_points(), line_two.get_points())
        self.assertEqual(result, True)

    def test_two_lines_over_lap(self):
        line_one = Line()
        line_one.set_points(1, 5)

        line_two = Line()
        line_two.set_points(4, 9)

        point_checker = PointChecker()
        result = point_checker.are_separate(line_one.get_points(), line_two.get_points())
        self.assertEqual(result, False)
