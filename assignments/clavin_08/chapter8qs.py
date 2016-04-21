#Author: Andrew Clavin
"""
8.1.1. Suppose a list is assigned to the variable name data. Show how you would
(a) print the length of data
(b) print the third element in data
(c) print the last element in data
(d) print the last three elements in data
(e) print the first four elements in data
(f) print the list consisting of the second, third, and fourth elements in data
"""

"""
8.2.2. Write a function that returns a list containing the squares
of the integers 1 through n. Use a for loop.
"""

"""
8.2.19. Rewrite the squares function from Exercise 8.2.2 using a
\list comprehension.
"""

class chapter8:
    def eightOneOneA(s, data):
        print(len(data))
    def eightOneOneB(s, data):
        print(data[2])
    def eightOneOneC(s, data):
        print(data[-1])
    def eightOneOneD(s, data):
        print(data[-3:])
    def eightOneOneE(s, data):
        print(data[0:3])
    def eightOneOneF(s, data):
        print(data[1:3])
    def eightTwoTwo(s, nombre):
        for i in range(1, nombre + 1):
            print( i ** 2 )
    def eightTwoNineteen(s, nombre):
        print( [x**2 for x in range(1, nombre + 1)] )

c8 = chapter8()
hey = [1,3,4,1,3,4,1,3,4,1,3,4,1,3,4,1,3,4]
c8.eightOneOneA(hey)
c8.eightOneOneB(hey)
c8.eightOneOneC(hey)
c8.eightOneOneD(hey)
c8.eightOneOneE(hey)
c8.eightOneOneF(hey)
c8.eightTwoTwo(8)
c8.eightTwoNineteen(8)
