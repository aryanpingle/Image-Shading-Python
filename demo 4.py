####################################################################################################
##                                     DEMO FILE: Aryan Pingle                                    ##
####################################################################################################

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

IMAGE_PATH = "Images/Pingle.jpg"
# INTERPOLATION_COUNT -> By keeping the interpolations to just 2, the number of colors that are present in the final image are just 7 shades of grey. So it looks washed-out, which is a nice and unexpected effect!
INTERPOLATION_COUNT = 2
VIEW_SCALE = 0.8
# SOURCE_COLORS -> Clean and simple; If you put just 'black' and 'white' in SOURCE_COLORS, you get a greyscaled image. BUT! Because INTERPOLATION_COUNT is just 2, it gives the result a grainy, water-color effect!
SOURCE_COLORS = ['black', 'white']

# Fun Fact: I actually set this as my wallpaper because of how cool it looked ^.^
SAVE_IMAGE = False
SAVE_NAME = "Pingle"

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