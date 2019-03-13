f = open('inputs/2.txt', 'r')
i = f.readline().split(' ')
while i:
    x = 0
    for j, k in zip(i[0], i[1]):
        if j != k:
            x+=1
        i = f.readline().split(' ')
    print(x)