from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *


class Monalisa:
	def __init__(self):
		self.load_textures()
		self.ghost = False
		self.see = True

	def load_textures(self):
		# 
		texturefile = os.path.join('img','photo','monalisa.jpg')
		textureSurface = image.load(texturefile)
		
		t1=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t1.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )

		self.textures1= t1
		
		# 
		texturefile = os.path.join('img','photo','monalisa_ghost.jpg')
		textureSurface = image.load(texturefile)
		
		t2=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t2.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )

		self.textures2=t2
		
		# Blue
		texturefile = os.path.join('img','rubik','blue.png')
		textureSurface = image.load(texturefile)
		
		t3=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t3.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		
		self.textures3=t3
		
		# Green
		texturefile = os.path.join('img','rubik','green.png')
		textureSurface = image.load(texturefile)
		
		t4=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t4.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		self.textures4=t4
		
		# Orange
		texturefile = os.path.join('img','rubik','orange.png')
		textureSurface = image.load(texturefile)
		
		t5=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t5.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		self.textures5=t5
		
		# White 
		texturefile = os.path.join('img','rubik','white.png')
		textureSurface = image.load(texturefile)
		
		t6=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t6.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		self.textures6=t6

	def draw(self):
		if self.see:
		    if self.ghost:
		        glBindTexture(GL_TEXTURE_2D, self.textures2.id)
		    else:
		        glBindTexture(GL_TEXTURE_2D, self.textures1.id)
		    glBegin(GL_QUADS)
		    glTexCoord2f(0.0, 0.0); glVertex3f(-1, -2,  0)	# Bottom Left Of The Texture and Quad
		    glTexCoord2f(1.0, 0.0); glVertex3f( 1, -2,  0)	# Bottom Right Of The Texture and Quad
		    glTexCoord2f(1.0, 1.0); glVertex3f( 1,  2,  0)	# Top Right Of The Texture and Quad
		    glTexCoord2f(0.0, 1.0); glVertex3f(-1,  2,  0)	# Top Left Of The Texture and Quad
		    glEnd()
		else:
		    glBegin(GL_LINE_LOOP)
		    glVertex3f( -1, -2, 0)
		    glVertex3f( 1, -2, 0)
		    glVertex3f( 1, 2, 0)
		    glVertex3f( -1, 2, 0)
		    glEnd()
		    
	
	def change_ghost(self):
		self.ghost = not self.ghost
	
	def change_see(self):
	    self.see = not self.see
		
		
