import argparse


def get_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--line_one', default="checkpoint_dir",
                        help="The coordinates for first line seperated by comma eg 1,2")
    parser.add_argument('--line_two', default="checkpoint_dir",
                        help="The coordinates for second line seperated by comma eg 1,2")


    return parser.parse_args()