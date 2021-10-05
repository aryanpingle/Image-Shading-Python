from PIL import Image

img = Image.open("images/NASA.jpg").convert("RGBA")
data = img.getdata()

def process(rgba):
    if sum(rgba[:3]) // 3 < 20:
        rgba = (0, 0, 0, 0)
    return rgba

data = list(map(process, data))
img.putdata(data)
img.show()
img.save("images/NASA-logo.png", "PNG")