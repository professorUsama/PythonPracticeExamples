# if __name__ == '__main__':
#     n = []
#     for i in range(1, 8, 2):
#         n.append(i)
#     print(n)
#     div = []
#     sum = 0
#     for index , value in enumerate(n):
#         print(index)

if __name__ == '__main__':
    n = 1
    sum = 0
    l = []
    while(n < 99):
        print(f"{n}\t",end="")
        l.append(f"{n}/{n+2}")
        sum += n/(n+2)
        n +=2
    print(l)
    print(sum)