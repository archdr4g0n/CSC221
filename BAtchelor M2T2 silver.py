##Tracy Batchelor
##M2T2 Exh1ustive Enumeration p.30
##CSC 221
##20 Sep 2017

x = 25
epsilon = 0.01
step = epsilon **2
numGuesses = 0
ans = 0.0
while abs(ans**2 -x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('Number of guesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on squar root of', x)
else:
    print(ans, 'is close to the square root of', x)
