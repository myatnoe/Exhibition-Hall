import os
from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *
import math

class cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.quadObj = gluNewQuadric();
        self.load_textures()
    
    def draw(self,distance=100):
        glEnable ( GL_TEXTURE_2D )
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        
        lod = 25-min(20,int(distance/1000))
        glPushMatrix()
        glRotatef(-90,1,0,0)
        glColor3f(1,1,1)
        gluCylinder(self.quadObj, self.radius, self.radius, self.height, 50,50)
        gluQuadricTexture(self.quadObj, GL_TRUE)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glTranslatef(0,0,self.height)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glPopMatrix()
        
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)
        glColor3f(1,1,1)
    
    def load_textures(self):
        file = os.path.join('img','wheel.png')
        surface = image.load(file)
        
        t1 = surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, t1.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        self.texture = t1


class sphere:
    def __init__(self, radius):
        self.radius = radius
        self.quadObj = gluNewQuadric();
        self.load_textures()
    
    def draw(self,distance=500):
        glEnable ( GL_TEXTURE_2D )
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        
        lod = 25-min(20,int(distance/1000))
        gluQuadricTexture(self.quadObj, GL_TRUE)
        
        glPushMatrix()
        glRotatef(-90,1,0,0)
        gluSphere(self.quadObj, self.radius, 50,50)
        glPopMatrix()
        
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)
        glColor3f(1,1,1)
    
    def load_textures(self):
        file = os.path.join('img','pumpkin.jpg')
        surface = image.load(file)
        
        t1 = surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, t1.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        self.texture = t1
    

class Pumpkin:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.sphere = sphere(width)
        self.rot = 0
    
    def draw(self):
        glPushMatrix()
        self.sphere.draw()
        glPopMatrix()
    
    def update(self):
        self.rot += 1
        self.rot %= 360

