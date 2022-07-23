class TuringMachine:
    def __init__(self, nodes, string, start):
        self.nodes = nodes
        self.tape = TuringTape(string)
        self.start = start
        self.current_node = start

    def run(self):
        edge = self.nodes[self.start].find_edge(self.tape.get_trigger())
        while edge is not None:
            self.tape.move(edge.replacement, edge.direction)
            self.current_node = edge.destination
            edge = self.nodes[edge.destination].find_edge(self.tape.get_trigger())
        print("stopped", self.current_node, self.tape.string)

class TuringTape:
    def __init__(self, string):
        self.string = string
        self.head = 0

    def move(self, replacement, direction):
        if replacement != "0":
            self.string = self.string[:self.head] + replacement + self.string[self.head + 1:]
        if direction == "L": self.head -= 1
        else: self.head += 1
        if self.head < 0:
            self.string = "B" + self.string
            self.head = 0
        elif self.head == len(self.string):
            self.string += "B"

    def get_trigger(self):
        return self.string[self.head]

class TuringNode:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def find_edge(self, trigger):
        for edge in self.edges:
            if trigger == edge.trigger:
                return edge
        return None

class TuringEdge:
    def __init__(self, trigger, replacement, direction, destination):
        self.trigger = trigger
        self.replacement = replacement
        self.direction = direction
        self.destination = destination