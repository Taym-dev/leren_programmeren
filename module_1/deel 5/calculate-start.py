from math_test import test,report
from math_operations import increment, decrement, add, substract, multiply, divide

nr1 = 3
nr2 = 11
nr3 = 37
nr4 = 79

# example
result1 = nr3 * 7
result2 = multiply(nr3, 7)
test('example', result1, result2)

result1 = nr1 + nr2
result2 = increment(nr1,nr2)
test('add', result1,result2)

result1 = (nr1 + nr2) * nr3
result2 = decrement(nr1,nr2)
test('expression-1',result1, result2)

result1 = nr4 / (nr3 - nr2)
result2 = divide(nr4, substract(nr3,nr2))
test('expression-2',result1, result2)

result1 = (nr4 + nr1) / (nr3 - nr2)
result2 = divide(add( nr4,nr1),substract(nr3, nr2))
test('expression-3',result1, result2)

result1 = nr1 + nr2 + nr3
result2 = add(nr1 + nr2 + nr3)
test('expression-4',result1, result2)

report
