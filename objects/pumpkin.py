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
    
    def draw(self,distance=100):
        lod = 25-min(20,int(distance/100))
        glPushMatrix()
        glColor3f(0,0,0)
        glDisable(GL_TEXTURE_2D)
        gluCylinder(self.quadObj, self.radius, self.radius, self.height, 50,50)
        glColor3f(1,1,1)
        glEnable ( GL_TEXTURE_2D )
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        gluQuadricTexture(self.quadObj, GL_TRUE)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glTranslatef(0,0,self.height)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glPopMatrix()
        
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)
        glColor3f(1,1,1)
    
    def load_textures(self):
        file = os.path.join('img','pumpkin','wheel.png')
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
        file = os.path.join('img','pumpkin','pumpkin.jpg')
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
        self.wheel = cylinder(height/3,width/20)
        self.whole_rot = 0 # Rotate on Y axis
        self.wheel_rot = 0 # Rotate on Z axis
        self.sphere_rot = 0 # Rotate on X axis
        self.rot_whole = False
        self.rot_wheel = False
        self.rot_sphere = False
    
    def draw(self):
        glPushMatrix()
        glRotatef(self.whole_rot,0,1,0)
        glPushMatrix()
        glRotatef(self.sphere_rot,0,0,1)
        self.sphere.draw()
        glPopMatrix()
        #draw_localAxis()
        # Wheel 1
        glPushMatrix()
        glRotatef(90,0,1,0)
        glTranslatef(-self.sphere.radius,-self.sphere.radius,-self.sphere.radius)
        glRotatef(-self.wheel_rot,0,0,1)
        self.wheel.draw()
        glPopMatrix()
        
        # Wheel 2
        glPushMatrix()
        glRotatef(90,0,1,0)
        glTranslatef(-self.sphere.radius,-self.sphere.radius,self.sphere.radius)
        glRotatef(-self.wheel_rot,0,0,1)
        self.wheel.draw()
        glPopMatrix()
        
        # Wheel 3
        glPushMatrix()
        glRotatef(90,0,1,0)
        glTranslatef(self.sphere.radius,-self.sphere.radius,-self.sphere.radius)
        glRotatef(-self.wheel_rot,0,0,1)
        self.wheel.draw()
        glPopMatrix()
        
        # Wheel 4
        glPushMatrix()
        glRotatef(90,0,1,0)
        glTranslatef(self.sphere.radius,-self.sphere.radius,self.sphere.radius)
        glRotatef(-self.wheel_rot,0,0,1)
        self.wheel.draw()
        glPopMatrix()
        glPopMatrix()
    
    def rotate_whole(self):
        self.rot_whole = not self.rot_whole
    
    def rotate_wheel(self):
        self.rot_wheel = not self.rot_wheel
    
    def rotate_pumpkin(self):
        self.rot_sphere = not self.rot_sphere
    
    def update(self):
        if self.rot_whole:
            self.whole_rot += .5
            self.whole_rot %= 360
        if self.rot_wheel:
            self.wheel_rot += .5
            self.wheel_rot %= 360
        if self.rot_sphere:
            self.sphere_rot += .5
            self.sphere_rot %= 360
    

