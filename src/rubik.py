from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *


class Rubik:
	def __init__(self):
		self.load_textures()

	def load_textures(self):
		# Red
		texturefile = os.path.join('../img','rubik','red.png')
		textureSurface = image.load(texturefile)
		
		t1=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t1.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )

		self.textures1= t1
		
		# Yellow
		texturefile = os.path.join('../img','rubik','yellow.png')
		textureSurface = image.load(texturefile)
		
		t2=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t2.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )

		self.textures2=t2
		
		# Blue
		texturefile = os.path.join('../img','rubik','blue.png')
		textureSurface = image.load(texturefile)
		
		t3=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t3.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		
		self.textures3=t3
		
		# Green
		texturefile = os.path.join('../img','rubik','green.png')
		textureSurface = image.load(texturefile)
		
		t4=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t4.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		self.textures4=t4
		
		# Orange
		texturefile = os.path.join('../img','rubik','orange.png')
		textureSurface = image.load(texturefile)
		
		t5=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t5.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		self.textures5=t5
		
		# White 
		texturefile = os.path.join('../img','rubik','white.png')
		textureSurface = image.load(texturefile)
		
		t6=textureSurface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t6.id)
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
		self.textures6=t6

	def draw(self):

		# Red Face (note that the texture's corners have to match the quad's corners)
		glBindTexture(GL_TEXTURE_2D, self.textures1.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(-1, -1,  1)	# Bottom Left Of The Texture and Quad
		glTexCoord2f(1.0, 0.0); glVertex3f( 1, -1,  1)	# Bottom Right Of The Texture and Quad
		glTexCoord2f(1.0, 1.0); glVertex3f( 1,  1,  1)	# Top Right Of The Texture and Quad
		glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1,  1)	# Top Left Of The Texture and Quad
		glEnd()
		
		# Yellow Face (note that the texture's corners have to match the quad's corners)
		glBindTexture(GL_TEXTURE_2D, self.textures2.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(-1, -1,  -1)	# Bottom Left Of The Texture and Quad
		glTexCoord2f(1.0, 0.0); glVertex3f(-1, -1,  1 )	# Bottom Right Of The Texture and Quad
		glTexCoord2f(1.0, 1.0); glVertex3f(-1,  1,  1 )	# Top Right Of The Texture and Quad
		glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1,  -1)	# Top Left Of The Texture and Quad
		
		glEnd()
		
		# Blue 
		glBindTexture(GL_TEXTURE_2D, self.textures3.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(-1, 1,  1)	# Bottom Left Of The Texture and Quad
		glTexCoord2f(1.0, 0.0); glVertex3f(1, 1,  1 )	# Bottom Right Of The Texture and Quad
		glTexCoord2f(1.0, 1.0); glVertex3f(1,  1,  -1 )	# Top Right Of The Texture and Quad
		glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1,  -1)	# Top Left Of The Texture and Quad
		glEnd()
		
		# Green
		glBindTexture(GL_TEXTURE_2D, self.textures4.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(1, -1,  1)	# Bottom Left Of The Texture and Quad
		glTexCoord2f(1.0, 0.0); glVertex3f(-1, -1,  1 )	# Bottom Right Of The Texture and Quad
		glTexCoord2f(1.0, 1.0); glVertex3f(-1,  -1,  -1 )	# Top Right Of The Texture and Quad
		glTexCoord2f(0.0, 1.0); glVertex3f(1,  -1,  -1)	# Top Left Of The Texture and Quad
		glEnd()
		
		# Orange
		glBindTexture(GL_TEXTURE_2D, self.textures5.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(1, -1,  1)    # Bottom Left Of The Texture and Quad
		glTexCoord2f(1.0, 0.0); glVertex3f(1, -1,  -1 )   # Bottom Right Of The Texture and Quad
		glTexCoord2f(1.0, 1.0); glVertex3f(1,  1,  -1 )   # Top Right Of The Texture and Quad
		glTexCoord2f(0.0, 1.0); glVertex3f(1,  1,  1) # Top Left Of The Texture and Quad
		glEnd()
		
		# White
		glBindTexture(GL_TEXTURE_2D, self.textures6.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(1, -1,  -1)    # Bottom Left Of The Texture and Quad
		glTexCoord2f(1.0, 0.0); glVertex3f(-1, -1,  -1 )  # Bottom Right Of The Texture and Quad
		glTexCoord2f(1.0, 1.0); glVertex3f(-1,  1,  -1 )  # Top Right Of The Texture and Quad
		glTexCoord2f(0.0, 1.0); glVertex3f(1,  1,  -1)    # Top Left Of The Texture and Quad
		glEnd()
		
