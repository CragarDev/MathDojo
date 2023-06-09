"""

Assignment: MathDojo

Objectives:

Practice creating a class and creating new instances
Practice chaining methods
Practice writing flexible functions that can take a varying number of arguments
Create a Python class called MathDojo that has one attribute, result, and 2 methods: add and subtract. The 2 methods each must take at least 1 parameter, but could take many more.


class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
    	# your code here
    def subtract(self, num, *nums):
    	# your code here
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!


"""


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # your code here
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        # your code here
        self.result -= num
        for n in nums:
            self.result -= n
        return self


md1 = MathDojo()
md2 = MathDojo()
md3 = MathDojo()

x = md1.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
y = md2.add(15).add(98, 5, 1, 10).subtract(6, 5, 4).result
print(y)  # should print 114
z = md3.add(200).add(22, 25, 21).subtract(2, 3, 5, 6).result
print(z)  # should print 252
