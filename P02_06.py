def sortId(L):
    # ADD ADDITIONAL CODE HERE!
    A = []
    L = sorted(list(zip(L[::2],L[1::2])))
    for i in L:
        for j in i:
            A.append(j)
    return A


print sortId(["14-002","Kim","13-009","Lee","16-005","Na","15-003","Kim"])
#['13-009','Lee','14-002','Kim','15_003','Kim','16-005','Na']
