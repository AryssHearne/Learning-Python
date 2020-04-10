#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'
for i in range(0, len(dna), 3):   
    for f in range(3):
        position= i+f
        print(position,f, dna[position])

for i in range(0, len(dna)):
    print(i, i%3, dna[i])
        

  


"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T


0 0 0
0 1 1
0 2 2
3 0 3
3 1 4
3 2 5
6 0 6
6 1 7
6 2 8
"""
