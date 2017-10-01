##Tracy Batchelor
##M2T2 Exhaustive Enumeration p.30
##CSC 221
##20 Sep 2017


print('This program calculates the hypotenuse of a right triangle.\n')

a = float(input('Enter a length of the short side of a right triangle: '))
b = float(input('Enter a length of the long side of a right triangle: '))

k = a**2 + b**2

guess = k/2.0

epsilon = 0.01
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/ (2*guess))

print('The hypotenuse of the triangle is about: ', guess)
