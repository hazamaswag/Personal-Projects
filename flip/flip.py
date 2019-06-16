from PIL import Image

im = Image.open('obama_og.jpg')
pix = im.load()
x_dim, y_dim = im.size
print("dimensions:", x_dim, y_dim)

for x in range(x_dim // 2):
    for y in range(y_dim):
        pix[x,y], pix[x_dim - x - 1, y] = pix[x_dim - x - 1, y], pix[x,y]

im.save('obama_flipped.png')
