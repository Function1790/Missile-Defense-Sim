frame = 0.1
x = [-0.2, -0.1, 0, 0.1, 0.2]
y = [i**2-2*i+3*i**3 for i in x]

primeYvalues = []
beforeDYpos = y
while True:
    deltaY = []
    for i in range(len(beforeDYpos)-1):
        deltaY.append(beforeDYpos[i+1]-beforeDYpos[i])

    beforeDYpos = deltaY
    if beforeDYpos == []:
        break
    dyCount = len(deltaY)
    middle = int(dyCount/2)
    square=len(primeYvalues)+1
    if dyCount%2==0:
        primeYvalues.append((beforeDYpos[middle]+beforeDYpos[middle-1])/2/frame**square)
    else:
        primeYvalues.append(beforeDYpos[middle]/frame**square)

print(primeYvalues)