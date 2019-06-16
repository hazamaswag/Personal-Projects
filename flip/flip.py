
def flip(x):
    print("og:", x)
    y = []
    for i in x:
        y += [i[::-1]]
    print("new",  y)

flip([[1,2,3],[4,5,6],[7,8,9]])
