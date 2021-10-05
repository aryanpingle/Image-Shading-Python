RGBA_NAMES = {
    "BLACK": [0, 0, 0, 255],
    "WHITE": [255, 255, 255, 255],
    "GREY": [128, 128, 128, 255],
    "GRAY": [128, 128, 128, 255],
    "RED": [255, 0, 0, 255],
    "GREEN": [0, 255, 0, 255],
    "BLUE": [0, 0, 255, 255],
    "YELLOW": [255, 255, 0, 255],
    "CYAN": [0, 255, 255, 255],
    "ORANGE": [255, 128, 0, 255],
    "AZURE": [0, 128, 255, 255],
    "SPRING": [0, 255, 128, 255],
    "PURPLE": [128, 0, 128, 255],
    "REBECCAPURPLE": [102, 51, 153, 255],
    "BLANCHEDALMOND": [255, 235, 205, 255]
}

from PIL import Image
import time
import re

def prepare_source_colors(SOURCE_COLORS):
    # Convert the normal, text source colors to their rgba's
    SOURCE_COLORS = list(map(lambda x: x if (type(x)==list or x.upper() not in RGBA_NAMES) else RGBA_NAMES[x.upper()], SOURCE_COLORS))
    # Add alpha in case I forgot to add those in the source colors
    SOURCE_COLORS = [i+[255] if (type(i)==list and len(i)==3) else i for i in SOURCE_COLORS]
    # convert everything to upper case
    SOURCE_COLORS = [i.upper() if type(i) == str else i for i in SOURCE_COLORS]

    return SOURCE_COLORS

def lerp(val, lb, ub, lv, uv):
    return lv + (val-lv)*(uv-lv)/(ub-lb)

def get_color_towards(color1, color2, fraction):
    """Returns a color which is fraction of the way from color1 to color2"""
    return [int(color1[i]*(1-fraction)+color2[i]*(fraction)) for i in range(4)]

def interpolate(standards: list, INTERPOLATION_COUNT: int):
    for _ in range(INTERPOLATION_COUNT):
        for i in range(len(standards) - 1):
            standards.insert(i*2+1, get_color_towards(standards[i*2], standards[i*2+1], 0.5))

def shade_image(image_path: str, INTERPOLATION_COUNT: int, SOURCE_COLORS: list, VIEW_SCALE: float = 1):
    img = Image.open(image_path).convert("RGBA")
    WIDTH, HEIGHT = int(img.width * VIEW_SCALE), int(img.height * VIEW_SCALE)
    img = img.resize((WIDTH, HEIGHT))
    data = img.getdata()

    INTERPOLATION_TYPE = 1 if any("/" in i for i in SOURCE_COLORS) else 0

    # Perform interpolation now if it's a normal type lerping
    if INTERPOLATION_TYPE == 0:
        interpolate(SOURCE_COLORS, INTERPOLATION_COUNT)

    CACHED_STANDARDS = [0]*WIDTH

    def process(enumerated):
        index,rgba = enumerated
        x = index%WIDTH
        fr = x / WIDTH
        greyscale = sum(rgba[:3]) // 3

        STANDARDS = 0
        if INTERPOLATION_TYPE == 0:
            STANDARDS = SOURCE_COLORS
        elif INTERPOLATION_TYPE == 1 and CACHED_STANDARDS[x]:
            STANDARDS = CACHED_STANDARDS[x]
        else:
            STANDARDS = list(map(lambda x: x if (type(x) == list) else get_color_towards(*[RGBA_NAMES[i] for i in re.split(r'\s+/\s+', x)], fr), SOURCE_COLORS))
            interpolate(STANDARDS, INTERPOLATION_COUNT)
            CACHED_STANDARDS[x] = STANDARDS

        color = STANDARDS[min(len(STANDARDS)-1, max(int(greyscale * len(STANDARDS) / 255), 0))]
        # Preserve the alpha
        return (*color[:3], rgba[-1])

    print(f"Processing '{image_path}'...")
    stime = time.time()
    newdata = list(map(process, enumerate(data)))
    print(f"Finished processing in {time.time()-stime}s")
    stime = time.time()
    img.putdata(newdata)
    return img