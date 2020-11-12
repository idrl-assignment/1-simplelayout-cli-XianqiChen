import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="CLI test", description="python training coding exercise"
    )
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs="*")
    parser.add_argument("-o", "--outdir", type=str, default="example_dir")
    parser.add_argument("--file_name", type=str, default="example")
    args = parser.parse_args()

    # 要求 1
    if args.board_grid % args.unit_grid == 0:
        pass
    else:
        sys.exit()

    # 要求 2
    if len(args.positions) != args.unit_n:
        sys.exit()
    for pos in args.positions:
        if pos < 1 | (pos > (args.board_grid / args.unit_grid) ** 2):
            sys.exit()

    # 要求 3
    current_path = os.getcwd()
    target_path = os.path.join(current_path, args.outdir)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    output_path = os.path.join(target_path, args.file_name)
    fp = open(output_path + ".mat", "a")
    fp.close()
    fp = open(output_path + ".jpg", "a")
    fp.close()


if __name__ == "__main__":
    main()
