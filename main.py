####################################################################################################
##                                           THE CONCEPT                                          ##
##                                           -----------                                          ##
##                                                                                                ##
## Every pixel in an image has a 'greyscale' value - the darker it is, the lower the 'greyscale'. ##
##  If we can use this greyscale value to choose a color from a list of our choice (let's call it ##
##        SOURCE_COLORS), we can effectively 'shade' the image with cool, artistic effects.       ##
##                                                                                                ##
##                                 That's what this program does.                                 ##
##                                                                                                ##
##   Interpolation means 'finding the middle ground' (kind of). By interpolating between [black,  ##
##    white], we get [black, GREY, white]. By interpolating again between this, we get [black,    ##
##                         DARK-GREY, grey, LIGHT-GREY, white], and so on.                        ##
##   The number of interpolations, or 'INTERPOLATION_COUNT' can be whatever number you want - 0   ##
##    meaning only the source colors are used, and 8 meaning infinite combinations between the    ##
##                                     SOURCE_COLORS you set.                                     ##
##                                                                                                ##
##  You can view / run some demo programs I made that showcase just how awesome this feature is.  ##
##                  Above all, art is about experimentation, so have fun with it!                 ##
####################################################################################################

# IMAGE_PATH -> This is the path to the image you want to shade
IMAGE_PATH = "Images/Dr. Stone.jpg"
# INTERPOLATION_COUNT -> This is the number of times the SOURCE_COLORS will be mixed (read the example in the description above)
INTERPOLATION_COUNT = 8
# VIEW_SCALE -> The result will be in a smaller size (original size * VIEW_SCALE) for speed, but the saved image will be regular sized
VIEW_SCALE = 0.4
# SOURCE_COLORS -> These are the colors from which the result will be created - if the original image has a dark pixel, it will be replaced by the left colors in the SOURCE_COLORS. If it was a lighter pixel, it will be replaced by the right colors in SOURCE_COLORS. You can either type out the name of the color (from the HUGE list in Helpers/shader.py) or you can put the RGB values in square brackets (see below)
SOURCE_COLORS = ['black', 'purple', 'yellow', "blanchedalmond", [255, 255, 255]]

# Change this to True if you want to save the result
SAVE_IMAGE = False
SAVE_NAME = "Purple Stone"

####################################################################################################
##                                    WARNING: Nerdy Code Stuff                                   ##
####################################################################################################

from Helpers.shader import *

SOURCE_COLORS = prepare_source_colors(SOURCE_COLORS)

if not SAVE_IMAGE:
    sample_image = shade_image(IMAGE_PATH, INTERPOLATION_COUNT, SOURCE_COLORS, VIEW_SCALE=VIEW_SCALE)
    sample_image.show()
if SAVE_IMAGE:
    print(f"Saving to Generated/{SAVE_NAME}.png")
    final_image = shade_image(IMAGE_PATH, INTERPOLATION_COUNT, SOURCE_COLORS, VIEW_SCALE=1)
    final_image.save(f"Generated/{SAVE_NAME}.png", "PNG")