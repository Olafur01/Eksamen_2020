def kalkul(oper):
    tall = 0
    for op in oper:
        if op == 'd':
            tall = tall * 2
        elif op == "1":
            tall += 1
        elif op == "2":
            tall += 2
        elif op == "3":
            tall += 3
        elif op == "4":
            tall += 4
        elif op == "5":
            tall += 5
        elif op == "6":
            tall += 6
        elif op == "7":
            tall += 7
        elif op == "8":
            tall += 8
        else:
            tall = tall

    return tall


print(kalkul("1d7d8"))
