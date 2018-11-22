import random
randomList = []
for x in range (10):
    randomNumber = random.randint(1,100)
    randomList.append(randomNumber)

for x in randomList:
    print(x, end=" ")

maxVal =randomList[0]

for y in randomList:
    if y > maxVal:
        maxVal = y

print(maxVal)
