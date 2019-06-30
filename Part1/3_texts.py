from manimlib.imports import *

class TextCreation(Scene):
  def construct(self):
    display_text = TextMobject("Getting Started with Manim")
    self.play(ShowCreation(display_text))
    self.wait(2)

class TextRotation(Scene):
  def construct(self):
    display_text = TextMobject("Getting Started with Manim")
    self.play(ShowCreation(display_text)) # display text on scene
    self.play(ApplyMethod(display_text.rotate, np.pi/2)) # rotate text on screen
    self.wait(2)

class MoveText(Scene):
  def construct(self):
    display_text1 = TextMobject("Getting Started with Manim")
    display_text2 = TextMobject(r"TextMobjects with \LaTeX")
    display_text1.move_to(3*UP) # move display_text1 upwards before showing it on scene
    self.add(display_text1) # show display_text1 on the updated location
    self.play(ShowCreation(display_text2)) # show creation of display_text2 at the center
    self.play(ApplyMethod(display_text2.move_to, 2*DOWN+1*LEFT)) # move display_text2
    self.wait(2)

class TextTransformation(Scene):
  def construct(self):
     display_text_1 = TextMobject(r"Getting Started with Manim")
     display_text_2 = TextMobject(r"TextMobject with \LaTeX support | $e^{\pi i} = -1$")
     # transform display_text_1 to display_text_2 on the scene
     self.play(Transform(display_text_1, display_text_2))
     self.wait(2)


# If you know latex typesettings, can you quickly animate this famous equation:
# https://sites.nicholas.duke.edu/statsreview/files/2013/06/normpdf1.jpg
