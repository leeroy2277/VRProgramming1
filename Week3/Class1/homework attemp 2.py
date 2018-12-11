for a in range(26):
    if a % 3 == 0 and a % 5 == 0:
        print(str(a)+":"+"fizzbuzz")
        continue
    if a % 3 == 0:
        print(str(a)+":"+"fizz")
        continue
    if a % 5 == 0:
        print(str(a)+":"+"buzz")
        continue
    print(str(a)+":")

