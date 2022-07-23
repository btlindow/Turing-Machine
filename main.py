from turing import *
from os.path import exists
import argparse

def parse_file(file):
    with open(file, 'r') as fp:
        num_lines = len(fp.readlines())
        fp.seek(0)
        line0 = fp.readline()
        num_nodes, start = (line0.split(',')[0], line0.split(',')[1])
        nodes = []
        for idx in range(int(num_nodes)):
            nodes.append(TuringNode(idx))
        for _ in range(num_lines - 2):
            line = fp.readline()
            line = line.split(',')
            nodes[int(line[0])].add_edge(TuringEdge(line[1],line[2],line[3],int(line[4])))
        string = fp.readline()
        tm = TuringMachine(nodes, string, int(start))
        tm.run()

parser = argparse.ArgumentParser(description='Headless Turing Machine')
parser.add_argument('input_file')
args = parser.parse_args()
if exists(args.input_file):
    parse_file(args.input_file)
else:
    print("file doesn't exist")