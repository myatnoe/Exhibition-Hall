import os
from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *
import math

class Cylinder:
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
    


class DisplayStand:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.top_cylinder = Cylinder(width,height*0.05)
        self.steel = Cylinder(width*0.1,height*0.9)
        self.base_cylinder = Cylinder(width,height*0.05)
        self.rot = 0
    
    def draw(self,distance):
        glPushMatrix()
        glRotatef(self.rot,0,1,0)
        self.top_cylinder.draw(distance)
        glTranslatef(0,self.top_cylinder.height,0)
        glPushMatrix()
        glTranslatef(-self.width/2,0,0)
        self.steel.draw(distance)
        glTranslatef(self.width,0,0)
        self.steel.draw(distance)
        glTranslatef(-self.width/2,0,self.width/2)
        self.steel.draw(distance)
        glTranslatef(0,0,-self.width)
        self.steel.draw(distance)
        glPopMatrix()
        glTranslatef(0,self.steel.height,0)
        self.base_cylinder.draw(distance)
        glPopMatrix()
    
    def update(self):
        self.rot += 1
        self.rot %= 360
        
        

