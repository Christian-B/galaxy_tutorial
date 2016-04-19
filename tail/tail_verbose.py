import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python version of tail function.')
    parser.add_argument('--input', type=argparse.FileType('r'))
    parser.add_argument('--output', type=argparse.FileType('w'))
    parser.add_argument('--lines', type=int, default=10)
    parser.add_argument('--from_top', action='store_true', default=False)
    args = parser.parse_args()
    all_lines = args.input.readlines()
    sys.stdout.write("Original file had {}.\n".format(len(all_lines)))
    if args.from_top:
        use_lines =  all_lines[args.lines-1:]
    else:
        use_lines =  all_lines[-args.lines:]
    sys.stderr.write("{} lines removed.\n".format(len(all_lines)-len(use_lines)))
    for line in use_lines:
        args.output.write(line)

