import time
from PIL import Image

nw, nh = 3840, 2160

img = Image.open("images/NASA.jpg")
data = list(img.getdata())
stime = time.time()
d = {}
for i in data:
    d[i] = d[i] + 1 if i in d else 1
bkg_color = max(d, key=d.get)
print(f"Time Taken: {time.time()-stime}s")
w,h = img.width,img.height
new_img = Image.new(img.mode, (nw, nh), bkg_color)
region = (nw//2 - w//2, nh//2 - h//2, nw//2 - w//2 + w, nh//2 - h//2 + h)
new_img.paste(img, region)
new_img.show()
# new_img.save("images/NASA.jpg", "JPEG")