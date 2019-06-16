from PIL import Image

im = Image.open('obama_og.jpg')
pix = im.load()
x_dim, y_dim = im.size
print("dimensions:", x_dim, y_dim)
print("(0,0):", pix[0,0])
print("(0,699):", pix[0,699])

for y in range(x_dim):
    for x in range(y_dim):
        pix[x,y_dim - y - 1], pix[x,y_dim - (y_dim - 1) - 1] = pix[x,y], pix[x, y_dim - 1]
#pix[0,y_dim - 699 - 1] = pix[0,699]
# print("(0,0):",pix[0,0])
# print("(0,699):",pix[0,699])
im.save('obama_flipped.png')

# def flip(x):
#     print("og:", x)
#     y = []
#     for i in x:
#         y += [i[::-1]]
#     print("new",  y)
#
# flip([[1,2,3],[4,5,6],[7,8,9]])
