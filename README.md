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

# ... what if we went further?

But that's just two colors - black and white. What if we added a little grey in between? How could we achieve that?

That's where interpolation is great - it allows us to mix black and white to form [`black`, `GREY`, `white`] after just 1 interpolation. Similarly, this becomes [`black`, `DARK-GREY`, `grey`, `LIGHT-GREY`, `white`] after 2 interpolations. I'm sure you can see where this is headed. You can keep interpolating, and the result will consist of multiple shades of `SOURCE_COLORS`.

## The best part? All you have to do is tell the program how many times the colors should be mixed!

Let's try this with a different source colors - [`black`, `purple`, `yellow`, `white`]:

[![Dr. Stone (Original)][5]][5]|[![Dr. Stone (After Shading)][6]][6]
:----:|:------:
Original Image|After Shading

  [1]: Images/Spider-Man.jpg
  [2]: Generated/Spider-Man.png
  [3]: Images/Pingle.jpg
  [4]: Generated/Pingle.png
  [4]: Images/Dr.%20Stone.jpg
  [4]: Generated/Purple%20Stone.png