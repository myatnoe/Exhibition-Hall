import os
from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *


class Wall:
    def __init__(self,width=100,height=100):
        self.width = width
        self.height = height
        self.load_textures()

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(0, 0, 0)
        glTexCoord2f(self.width/200, 0.0); glVertex3f(self.width, 0,  0)
        glTexCoord2f(self.width/200, self.height/300); glVertex3f(self.width, self.height, 0)
        glTexCoord2f(0.0, self.height/300); glVertex3f(0, self.height,  0)
        glEnd()

    def load_textures(self):
		file = os.path.join('img','xv.png')
		surface = image.load(file)

		t1 = surface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t1.id)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		self.texture = t1



class Floor:
	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.load_textures()

	def draw(self):
		glBindTexture(GL_TEXTURE_2D, self.texture.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(0, 0, self.width)
		glTexCoord2f(4.0, 0.0); glVertex3f(self.length,0,  self.width)
		glTexCoord2f(4.0, 4.0); glVertex3f(self.length, 0, 0)
		glTexCoord2f(0.0, 4.0); glVertex3f(0, 0,  0)
		glEnd()
    
	def load_textures(self):
		file = os.path.join('img','checkered_pattern.png')
		surface = image.load(file)

		t1 = surface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t1.id)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		self.texture = t1
    
    

class Ceiling:
	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.load_textures()

	def draw(self):
		glBindTexture(GL_TEXTURE_2D, self.texture.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(0, 0, self.width)
		glTexCoord2f(4.0, 0.0); glVertex3f(self.length,0,  self.width)
		glTexCoord2f(4.0, 4.0); glVertex3f(self.length, 0, 0)
		glTexCoord2f(0.0, 4.0); glVertex3f(0, 0,  0)
		glEnd()

	def load_textures(self):
		file = os.path.join('img','struckaxiom.png')
		surface = image.load(file)

		t1 = surface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t1.id)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		self.texture = t1


