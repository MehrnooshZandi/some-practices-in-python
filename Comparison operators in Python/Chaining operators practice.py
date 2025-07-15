'''
In Python, you can use comparison operators in a chained manner. For example, the expression a < b <= c is equivalent to two separate comparisons: a < b and b <= c. This allows you to perform multiple comparisons in a single expression.

Your task: Write a program that takes three input numbers and checks whether the first number is less than the second number and the second number is less than or equal to the third number.

Inputs:

Three integers, a, b, and c.

Outputs:

If a < b <= c, return True.

Otherwise, return False.

Sample Input:

5
10
15

Sample Output:

True

Hint:
To get input from the user, you can use the following command:

a=input()

Now if we want to convert this input to int at the same time, we have:

a = int(input())

You will learn more about this command later.'''
# input
a = int(input())
b = int(input())
c = int(input())

result = a < b <= c

print(result)

