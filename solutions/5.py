with open('inputs/5.txt', 'r') as f:
    l = f.readline()
    while l:
        for i in range(len(l),0,-1):
            print(l[:i])
        #for i in range(2, len(l)+1):
        #    print(l[:i])
        l = f.readline()