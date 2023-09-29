####################################################################################################
##                                          Change These                                          ##
####################################################################################################

IMAGE_PATH = "Images/NASA.jpg"
INTERPOLATION_COUNT = 1
VIEW_SCALE = 0.4
SOURCE_COLORS = ["BLUE / CYAN", "WHITE"]

####################################################################################################
##                                    WARNING: Nerdy Code Stuff                                   ##
####################################################################################################

from Helpers.shader import *

SOURCE_COLORS = prepare_source_colors(SOURCE_COLORS)

sample_image = shade_image(IMAGE_PATH, INTERPOLATION_COUNT, SOURCE_COLORS, VIEW_SCALE=VIEW_SCALE)
sample_image.show()

print("-"*30)
print("Do you want to save this image?")
print("[Enter Y to save it, anything else to exit]")
SAVE_IMAGE = input(">> ").strip()[0].upper() == "Y"

if SAVE_IMAGE:
    print(f"What do you want to save '{IMAGE_PATH}' as?")
    SAVE_NAME = input(">> ").strip()
    print(f"Saving to Generated/{SAVE_NAME}.png")
    final_image = shade_image(IMAGE_PATH, INTERPOLATION_COUNT, SOURCE_COLORS, VIEW_SCALE=1)
    final_image.save(f"Generated/{SAVE_NAME}.png", "PNG")