from get_input_args import *


class PointChecker:
    def __init__(self):
        pass

    def are_separate(self, r, s):
        (a, b) = r
        (x, y) = s
        return b < x or y < a

    def test_method(self):
        return "done"


class Line():

    def __init__(self):
        self.line = None

    def set_points(self, x1, x2):
        self.line = tuple(list([x1, x2]))

    def get_points(self):
        return self.line


def main():
    in_arg = get_input_args()
    setone = in_arg.line_one.split(',')
    settwo = in_arg.line_two.split(',')
    lineOne = Line()
    lineOne.set_points(setone[0], setone[1])

    lineTwo = Line()
    lineTwo.set_points(settwo[0], settwo[1])

    line_one = tuple(in_arg.line_one.split(','))
    line_two = tuple(in_arg.line_two.split(','))
    pt = PointChecker()
    check = pt.are_separate(line_one, line_two)
    if check:
        print("The lines do not overlap")
        return True
    else:
        print("The lines overlap")
        return False


if __name__ == "__main__":
    main()
