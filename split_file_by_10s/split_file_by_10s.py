import argparse
import os
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python version of tail function.')
    parser.add_argument('--input', type=argparse.FileType('r'))
    args = parser.parse_args()
    all_lines = args.input.readlines()
    if not os.path.exists("split"):
        os.makedirs("split")
    for ten in range(0,len(all_lines)/10):
        use_lines =  all_lines[ten*10:(ten+1)*10]
        with open("split/lines"+str(ten)+".txt", 'w') as f:
            for line in use_lines:
                f.write(line)
        sys.stdout.write("Ten file saved as split/lines"+str(ten)+".txt\n")

