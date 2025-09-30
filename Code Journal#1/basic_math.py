"""
Write a Python that prints the sum of two floating point numbers,
the difference between two integers, and
the product of a floating point number and an integer.
In each case, have the program print out the data type of the resulting answer.
"""
# git push straight from pycharm
class calculator:
    def addition(self,x,y):
        return x+y
    def subtraction(self,x,y):
        return x-y
    def multiplication(self,x,y):
        return x*y

test = calculator()

# sum of two floating point numbers
result = test.addition(1.2,2.1)
print(result, type(result))
# difference between two integers
result = test.subtraction(10,20)
print(result, type(result))
#product of a floating point number and an integer
result = test.multiplication(2.2,10)
print(result, type(result))



