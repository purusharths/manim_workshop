from manimlib.imports import *

class FirstScene(Scene): # All classes that animate are a subclass of scene
	def construct(self):
		"""
		All the animation code must lie within construct method.
		This method is invoked by manim.py
		"""
		circle = Circle() # creating circle object
		self.add(circle) # adding that circle object to the scene
		self.wait(2) # waiting for two second ~ time.sleep(2)

"""
Render the scene with: manim first_scene.py FirstScene -p
"""


class SecondScene(Scene):
	def construct(self):
		""" Animation objects will lie within this method"""
		square = Square() # creating square object
		self.play(ShowCreation(square))
		self.wait(4)

# Render the second scene
