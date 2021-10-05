# Whoa, What's This?

They told me, "Aryan, you sexy beast, it's impossible to make cool image effects using just Python!", and I set out to prove them wrong. And I did. Kind of.

[![Spider-Man (Original)][1]][1]|[![Spider-Man (After Shading)][2]][2]
:----:|:------:
Original Image|After Shading

# Interpolation is simple

You blend two things in different quantities. Really, it's just that simple. Now what if we interpolated two colors together? That's the question I asked myself while high on caffeine. The program is equally simple: 

1. Take an image
2. For every pixel, calculate its `greyscale` - the average of its R, G and B values (which goes from 0 - 255)
3. Let's make a random color pallete, called the `SOURCE_COLORS` - [`black`, `white`]
4. Based on `greyscale`, choose a color from `SOURCE_COLORS` - if `greyscale` is a small value (0 - 128), choose `black`, and choose `white` if it is large (128 - 255)
5. Set this new color as the pixel color

Congratulations, you just made a black-and-white effect!

[![Pingle (Original)][3]][3]|[![Pingle (After Shading)][4]][4]
:----:|:------:
Original Image|After Black 'N White Shading

  [1]: Images/Spider-Man.jpg
  [2]: Generated/Spider-Man.png
  [3]: Images/Pingle.jpg
  [4]: Generated/Pingle.png