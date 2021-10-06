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

Let me remind you - I only changed the source colors, NOTHING ELSE. That's the power of interpolation and shading.

What? You still aren't impressed? I still have one trick up my sleeve.

Interpolation won't just shade everything with a different color - it can COMPLETELY CHANGE the image. Here's what happens with `SOURCE_COLORS` = [`red / orange`, `white`]:

[![NASA (Original)][7]][7]|[![NASA (After Shading)][8]][8]
:----:|:------:
Original Image|After Shading

BAM! How cool is that? Since black and the blue NASA circle are pretty similar in darkness, the interpolation replaced both of them with orange-red, giving us that **sexy** background look. This result was so surprisingly impressive, that I actually used this as my desktop background XD

# But Aryan, I don't know how to start?

Don't worry my child, I have made everything clear in the source code. Read the documentation inside main.py, and you should be ready to go. Yes, it's that simple.

**Potential Applications**:

 - [x] Adding subtle effects to a logo or design
 - [x] Making images take a theme color, like with my NASA example
 - [ ] Getting you laid
 - [x] Potentially bypassing copyright infringement, as you can completely change how an image looks, while keeping the content same

  [1]: Images/Spider-Man.jpg
  [2]: Generated/Spider-Man.png
  [3]: Images/Pingle.jpg
  [4]: Generated/Pingle.png
  [5]: Images/Dr.%20Stone.jpg
  [6]: Generated/Purple%20Stone.png
  [7]: Images/NASA.jpg
  [8]: Generated/NASA.png