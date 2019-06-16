from PIL import Image

im = Image.open('obama_og.jpg')
pix = im.load()
x_dim, y_dim = im.size
print("dimensions:", x_dim, y_dim)

for x in range(x_dim ):
    for y in range(y_dim):
        print("(",x, ",", y,")", " ---->  (", pix[x,y], ")",sep="")
        print("(",x, ",", y_dim - y - 1,")", " ---->  (", pix[x,y_dim - y - 1], ")",sep="")
        pix[x,y] = pix[y,x]
        print("-------------------------------------------------------")
        print("(",x, ",", y,")", " ---->  (", pix[x,y], ")",sep="")
        print("(",x, ",", y_dim - y - 1,")", " ---->  (", pix[x,y_dim - y - 1], ")",sep="")
        print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")

im.save('obama_flipped.png')
# pix[x,y_dim - y - 1], pix[x,y] = pix[x,y], pix[x, y_dim - y - 1]
# def flip(x):
#     print("og:", x)
#     y = []
#     for i in x:
#         y += [i[::-1]]
#     print("new",  y)
#
# flip([[1,2,3],[4,5,6],[7,8,9]])
