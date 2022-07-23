# Turing Machine
This is a simple Turing Machine parser written in Python. The program takes in a specially formatted input file and outputs the stopping node as well as the current state of the tape.

## Concept
A Turing Machine consists of a tape, a head, nodes, and edges. The tape can be imagined as a long piece of paper with a sequence of characters written on it. The head points to the current character on the tape. The nodes are what keep track of the current state of the machine. A node can transition to another node via an edge. An edge consists of a trigger character, replacement character, tape movement direction, and a destination node. The Turing Machine also has a starting node that is specified by the user. When the Turing Machine starts, it first looks at the head to determine the current character on the tape. It will then look at all of the edges leaving the current node, in this case the start node, and determine if the current head character matches any of the edges trigger characters. If it finds a matching trigger character, it will then replace the character in the tape with the edge's replacement character, move the tape in the edge's desired direction, and transition the current node to the destination node.

## Example
Let's say we have 2 nodes, 0 and 1. Lets define the following edges that leave node 0:

a,a,R,0
b,a,R,1

The first edge states that if the head on the tape is the character 'a', leave it an 'a' and move the tape to the right. Then transition to node 0, which is itself. The second edge states that if the head on the tape is the character 'b', change it to an 'a' and move the tape to the right. Then transition to node 1.

Let's define some edges leaving node 1:

b,b,R,1
a,b,R,0

This is very similar to what node 0 is doing, but with 'a' and 'b' swapped.

Let's define our tape to be the string "aaabbbba", our head to start at the first character, and the starting node to be node 0. When the Turing Machine starts, it looks at the head and sees the character 'a'. Node 0 will leave this an 'a', move the tape to the right, and transition to node 0 (itself). The machine again looks at the next character, which is 'a' and repeats this cycle until it reaches the character 'b'. When the machine reads the character 'b', node 0 will change this character to an 'a', move the tape to the right, and transition to node 1. This will leave our string looking as follows:

"aaaabbba"

The machine will then look at the next character, 'b', and node 1 will leave it a 'b', move the tape to the right, and transition to node 1 (itself). It will do this until it reads the final 'a' at the end, where it will replace it with an 'b', move the tape the right, and transition back to node 0. The final string will be:

"aaaabbbb"

However, because our string ran out, doesn't mean the machine has to stop. We can prepend and append a blank character, "B", to the string and continue with edges that trigger on "B". Another way to look at the original input string is:

"....BBBBBBBaaabbbbaBBBBBBBB...."

Since we didn't define any edge triggers for the blank character "B", our Turing Machine stopped at the first "B."

## Input File
The first line of the input file contains the total number of nodes in the Turing Machine followed by the starting node index, seperated by a comma.

The last line of the input file contains the inital string on the tape.

All of the lines in between these two lines contain the edges defined as such:

<node_idx>,<trigger_character>,<replacement_character>,<tape_direction>,<destination_node>

An example input file for the example above would look like this:

```
2,0
0,a,a,R,0
0,b,a,R,1
1,b,b,R,1
1,a,b,R,0
aaabbbba
```

## Future Work
I want to comment things. I would also like to validate the Turing Machine input file to ensure it follows the correct criteria for a Turing Machine.

## Reference
This is an awesome, interactive Turing Machine tool:
https://turingmachine.io/
