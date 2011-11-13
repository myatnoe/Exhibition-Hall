import os
from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *
import math
from models import draw_localAxis

class cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.quadObj = gluNewQuadric();
        self.load_textures()
    
    def draw(self,distance):
        glEnable ( GL_TEXTURE_2D )
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        
        lod = 25-min(20,int(distance/100))
        gluQuadricTexture(self.quadObj, GL_TRUE)
        
        glPushMatrix()
        glRotatef(-90,1,0,0)
        gluCylinder(self.quadObj, self.radius, self.radius, self.height, 50,50)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glTranslatef(0,0,self.height)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glPopMatrix()
        
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)
        glColor3f(1,1,1)
    
    def load_textures(self):
        file = os.path.join('img','metal.png')
        surface = image.load(file)
        
        t1 = surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, t1.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        self.texture = t1
    

class box():
    def __init__(self,length,depth,height):
        self.rot=0.
        self.rotSpeed=2
        self.length = length
        self.height = height
        self.depth = depth
        self.load_textures()
    
    def update(self,dt=0.):
        self.rot +=self.dRot[0]*dt*self.rotSpeed
        self.rot %= 360
    
    def draw(self):
        glPushMatrix()
        glTranslatef(0,self.height/2,0)
        glScalef(self.length,self.height/2,self.depth)
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(-1, -1,  1)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f( 1, -1,  1)	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f( 1,  1,  1)	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1,  1)	# Top Left Of The Texture and Quad
        glEnd()
        
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(-1, -1,  -1)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f(-1, -1,  1 )	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f(-1,  1,  1 )	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1,  -1)	# Top Left Of The Texture and Quad
        glEnd()
        
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(-1, 1,  1)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f(1, 1,  1 )	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f(1,  1,  -1 )	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1,  -1)	# Top Left Of The Texture and Quad
        glEnd()
        
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(1, -1,  1)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f(-1, -1,  1 )	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f(-1,  -1,  -1 )	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(1,  -1,  -1)	# Top Left Of The Texture and Quad
        glEnd()
        
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(1, -1,  1)    # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f(1, -1,  -1 )   # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f(1,  1,  -1 )   # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(1,  1,  1) # Top Left Of The Texture and Quad
        glEnd()
        
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(1, -1,  -1)    # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f(-1, -1,  -1 )  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f(-1,  1,  -1 )  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(1,  1,  -1)    # Top Left Of The Texture and Quad
        glEnd()
        glPopMatrix()
    
    def load_textures(self):
        file = os.path.join('img','metal.png')
        surface = image.load(file)

        t1 = surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, t1.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        self.texture = t1
    

class DisplayStand:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.top_cylinder = cylinder(width/2,height*0.05)
        self.box = box(width/8,width/8,height*0.9)
        self.base_cylinder = cylinder(width,height*0.05)
        self.rot = 0
    
    def draw(self,distance):
        glPushMatrix()
        glRotatef(self.rot,0,1,0) # rotate the whole stand
        self.top_cylinder.draw(distance)
        glTranslatef(0,self.top_cylinder.height,0)
        glPushMatrix()
        self.box.draw()
        glPopMatrix()
        glTranslatef(0,self.box.height,0)
        self.base_cylinder.draw(distance)
        glPopMatrix()
    
    def update(self):
        self.rot += 1
        self.rot %= 360

