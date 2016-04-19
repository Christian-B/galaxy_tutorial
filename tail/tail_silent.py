import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python version of tail function.')
    parser.add_argument('--input', type=argparse.FileType('r'))
    parser.add_argument('--output', type=argparse.FileType('w'))
    parser.add_argument('--lines', type=int, default=10)
    parser.add_argument('--from_top', action='store_true', default=False)
    args = parser.parse_args()
    all_lines = args.input.readlines()
    print "top"
    print  all_lines[args.lines-1:]
    print "bottom"
    print all_lines[-5:]
    if args.from_top:
        use_lines =  all_lines[args.lines-1:]
    else:
        use_lines =  all_lines[-args.lines:]
    for line in use_lines:
        args.output.write(line)

