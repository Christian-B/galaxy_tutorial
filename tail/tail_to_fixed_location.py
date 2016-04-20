import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python version of tail function.')
    parser.add_argument('--input', type=argparse.FileType('r'))
    args = parser.parse_args()
    all_lines = args.input.readlines()
    use_lines =  all_lines[-10:]
    with open("tail.txt", 'w') as f:
        for line in use_lines:
            f.write(line)
    sys.stdout.write("Tail file saved as tail.txt")

