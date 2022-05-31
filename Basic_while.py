i = 0
while i <= 10:        # As long as the condition is true, the code following the loop is executed
    print(i)
    i += 1

print("End of loop")        # basic example of while loop


c = 1
while c < 10:
    print(c)
    if c == 5:
        break       # we can stop the loop by using a break statement while the condition is still true
    c += 1

print("End of loop")


n = 0
while n < 10:
    n += 1
    if n == 7:
        continue        # the continue statement can skip an iteration and move to executing the next.
    print(n)

print("End of loop. 7 is missing")
