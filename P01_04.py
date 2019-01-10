def printMultTable1():
    for i in range(1,10):
        print i,
    print ""
    for i in range(3,10,2):
        for j in range(i,i*10,i):
            print j,
        print ""


def printMultTable2():
    for i in range(1,10,2):
        for j in range(i,i*i+1,i):
            print j,
        print ""


printMultTable1()
printMultTable2()