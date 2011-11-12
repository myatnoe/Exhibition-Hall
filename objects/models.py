from math import pi,sin,cos
import pyglet
from pyglet.gl import *
from pyglet.window import key
import os
from pyglet import image
# Library of renderable objects

def draw_sphere(radius,RGB,lod=None):
    draw_localAxis(radius*0.5)
    if lod != None:
        lod=max(6,lod)
        lod=min(26,lod)
        lod=30-lod
    else:
        lod=12
    lod=int(lod)
    
    glColor3f(RGB[0],RGB[1],RGB[2])
    glPushMatrix()
    glRotatef(90,1,0,0)
    q = gluNewQuadric()
    gluQuadricDrawStyle(q,GLU_FILL )
    gluSphere(q,radius,lod,lod)
    glColor3f(0,0,0)
    gluQuadricDrawStyle(q,GLU_LINE)
    gluSphere(q,radius+1,lod,lod)
    glPopMatrix()


def draw_sphere_texture(radius=6, distance=500):
    #draw_localAxis(radius)				# draw the local axis for this sphere
    
    lod=25-min(20,int(distance/1000))			# set the LOD (level of detail) for this model
    q = gluNewQuadric()					# create a sphere model
    
    gluQuadricTexture(q, GL_TRUE)    # Enable Texture Coords For The Quad
    #gluQuadricOrientation(q, GLU_OUTSIDE) # Michelle's testing
    
    glPushMatrix()					# save current transformations
    glRotatef(-90,1,0,0)        
    gluSphere(q,radius,lod,lod)				# draw sphere with texture
    glPopMatrix()					# restore the transformations as they were before


def draw_localAxis():
    localAxis = pyglet.graphics.vertex_list(6, 
        ('v3f/static', (0.0,0,0.0,25,0,0.0,0.0,0,0.0,0.0,25, 0.0,0.0,0,0.0,0.0,0.0,25)), 
        ('c3B/static', (255,0,0,255,0,0,0,255,0,0,255,0,0,0,255,0,0,255)))
    
    glLineWidth(4)
    localAxis.draw(GL_LINES)
    glLineWidth(1)


# Draw a cube with variable size
def draw_cube(size=250):
    
    glBegin(GL_QUADS) ##################################################
    
    glColor3f(0,1,0)
    glVertex3f( size, size, 0)
    glVertex3f(0,     size, 0)		
    glVertex3f(0,     size, size)		
    glVertex3f( size, size, size)		
    
    glColor3f(0,1,0)
    glVertex3f( size, 0,    size)
    glVertex3f(0,     0,    size)		
    glVertex3f(0,     0,    0)		
    glVertex3f( size, 0,    0)		
    
    glColor3f(0,0,1)
    glVertex3f( size, size, size)
    glVertex3f(0,     size, size)		
    glVertex3f(0,     0,    size)		
    glVertex3f( size, 0,    size)		
    
    glColor3f(0,0,1)
    glVertex3f( size, 0,    0)
    glVertex3f(0,     0,    0)
    glVertex3f(0,     size, 0)		
    glVertex3f( size, size, 0)		
    
    glColor3f(1,0,0)
    glVertex3f(0,     size, size)
    glVertex3f(0,     size, 0)		
    glVertex3f(0,     0,    0)		
    glVertex3f(0,     0,    size)		
    
    glColor3f(1,0,0)
    glVertex3f( size, size, 0)
    glVertex3f( size, size, size)
    glVertex3f( size, 0,    size)		
    glVertex3f( size, 0,    0)
    glEnd() ##################################################
    # draw this box local axis
    draw_localAxis()

# a 3d cube with variable size, pos and rot
def draw_box(length=250,height=50,depth=100):
    
    glBegin(GL_QUADS) ##################################################
    
    glColor3f(0,1,0)
    glVertex3f( length,  height, 0)
    glVertex3f(0,       height, 0)		
    glVertex3f(0,       height, depth)		
    glVertex3f( length,  height, depth)		
    
    glColor3f(0,1,0)
    glVertex3f( length,  0,      depth)
    glVertex3f(0,       0,      depth)		
    glVertex3f(0,       0,      0)		
    glVertex3f( length,  0,      0)		
    
    glColor3f(0,0,1)
    glVertex3f( length,  height, depth)
    glVertex3f(0,       height, depth)		
    glVertex3f(0,       0,      depth)		
    glVertex3f( length,  0,      depth)		
    
    glColor3f(0,0,1)
    glVertex3f( length,  0,      0)
    glVertex3f(0,       0,      0)
    glVertex3f(0,       height, 0)		
    glVertex3f( length,  height, 0)		
    
    glColor3f(1,0,0)
    glVertex3f(0,       height, depth)
    glVertex3f(0,       height, 0)		
    glVertex3f(0,       0,      0)		
    glVertex3f(0,       0,      depth)		
    
    glColor3f(1,0,0)
    glVertex3f( length,  height  ,0)
    glVertex3f( length,  height, depth)
    glVertex3f( length,  0,      depth)		
    glVertex3f( length,  0,      0)
    glEnd() ##################################################
    # draw this box local axis
    draw_localAxis()

class fps():
    def __init__(self,width,height):
        self.fps = pyglet.clock.ClockDisplay()
        self.width=width
        self.height=height
        
    def update(self,width,height):
        self.width=width
        self.height=height
    
    def draw(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width, 0, self.height, 1, -1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        self.fps.draw()
        
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45., self.width / float(self.height), .1, 10000.)
        glMatrixMode(GL_MODELVIEW)


class grid():
    def __init__(self,pos=(0.,0.,0.),rot=(0.,0.,0.),rotSpeed=2,size=6):
        self.rot_x=0.
        self.rot_y=0.
        self.rot_z=0.
        self.trn_x=pos[0]
        self.trn_y=pos[1]
        self.trn_z=pos[2]
        self.size=int(size)
        self.dRot=rot
        self.rotSpeed=rotSpeed
        # text text
        self.xLabel=pyglet.text.Label('x', font_name='Times New Roman',color=(255,1,1,255),
            font_size=40, x=0, y=0, anchor_x='center', anchor_y='center')
        self.yLabel=pyglet.text.Label('y', font_name='Times New Roman',color=(1,255,1,255),
            font_size=40, x=0, y=0, anchor_x='center', anchor_y='center')
        self.zLabel=pyglet.text.Label('z', font_name='Times New Roman',color=(1,1,255,255),
            font_size=40, x=0, y=0, anchor_x='center', anchor_y='center')
            
        # the coloured 3 axis
        self.step=self.size/10
        size=300
        oset=0.
        self.axis = pyglet.graphics.vertex_list(6, 
        ('v3f/static', (-oset,0,-oset,size-oset,0,-oset,-oset,0,-oset,-oset,size, -oset,-oset,0,-oset,-oset,0,size-oset)), 
        ('c3B/static', (255,0,0,255,0,0,0,255,0,0,255,0,0,0,255,0,0,255)))
    
    def update(self,dt=0.):
        self.rot_x+=self.dRot[0]*dt*self.rotSpeed
        self.rot_y+=self.dRot[1]*dt*self.rotSpeed
        self.rot_z+=self.dRot[2]*dt*self.rotSpeed
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.trn_x,self.trn_y,self.trn_z)
        glRotatef(self.rot_x,1.0,0.0,0.0)
        glRotatef(self.rot_y,0.0,1.0,0.0)
        glRotatef(self.rot_z,0.0,0.0,1.0)
        glLineWidth(4)
        self.axis.draw(gl.GL_LINES)
        glLineWidth(1)
        glPopMatrix()
            
        glPushMatrix()
        glTranslatef(self.trn_x,self.trn_y,self.trn_z)
        glBegin(GL_LINES)
        glColor3f(0.5,0.5, 0.5)
        for i in range(-self.size,self.size+1,self.step):
            glVertex3f(-self.size, 0., i)
            glVertex3f( self.size, 0., i)
            
            glVertex3f(i, 0., -self.size)
            glVertex3f(i, 0.,  self.size)
        glEnd()
        glPopMatrix()
        
        glPushMatrix() # x
        glTranslatef(280,24,0)
        self.xLabel.draw()
        glPopMatrix()
        
        glPushMatrix() # y
        glTranslatef(0,340,0)
        self.yLabel.draw()
        glPopMatrix()
        
        glPushMatrix() # z
        glTranslatef(0,4,280)
        glRotatef(90, .0,1.0,0.0)
        
        glRotatef(180,.0,.0 ,1.0)
        self.zLabel.draw()
        glPopMatrix()
    
    

class sphere():
    def __init__(self,pos=(0.,0.,0.),rot=(0.,0.,0.),rotSpeed=2,size=6):
        self.rot_x=0.
        self.rot_y=0.
        self.rot_z=0.
        self.trn_x=pos[0]
        self.trn_y=pos[1]
        self.trn_z=pos[2]
        self.size=size
        self.sections=size/5
        self.dRot=rot
        self.rotSpeed=rotSpeed
        
    def update(self,dt=0.):
        self.rot_x+=self.dRot[0]*dt*self.rotSpeed
        self.rot_y+=self.dRot[1]*dt*self.rotSpeed
        self.rot_z+=self.dRot[2]*dt*self.rotSpeed
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.trn_x,self.trn_y,self.trn_z)
        glRotatef(self.rot_x,1.0,0.0,0.0)
        glRotatef(self.rot_y,0.0,1.0,0.0)
        glRotatef(self.rot_z,0.0,0.0,1.0)
        draw_localAxis()
        q = gluNewQuadric()
        gluQuadricDrawStyle(q,GLU_LINE)
        gluSphere(q,self.size,self.sections,self.sections)
        glPopMatrix()
    

class pyramid():
    def __init__(self,pos=(0.,0.,0.),rot=(0.,0.,0.),rotSpeed=2,size=6):
        self.rot_x=0.
        self.rot_y=0.
        self.rot_z=0.
        self.trn_x=pos[0]
        self.trn_y=pos[1]
        self.trn_z=pos[2]
        self.size=size
        self.dRot=rot
        self.rotSpeed=rotSpeed
        
    def update(self,dt=0.):
        self.rot_x+=self.dRot[0]*dt*self.rotSpeed
        self.rot_y+=self.dRot[1]*dt*self.rotSpeed
        self.rot_z+=self.dRot[2]*dt*self.rotSpeed
        
    def draw(self):
        glPushMatrix()
        glTranslatef(self.trn_x,self.trn_y,self.trn_z)
        glRotatef(self.rot_x,1.0,0.0,0.0)
        glRotatef(self.rot_y,0.0,1.0,0.0)
        glRotatef(self.rot_z,0.0,0.0,1.0)
        
        draw_localAxis()
        
        glBegin(GL_TRIANGLES)				
        glColor3f(1.0,0.0,0.0)
        glVertex3f( 0.0, self.size, 0.0)		
        glColor3f(0.0,1.0,0.0)
        glVertex3f(-self.size,-self.size, self.size)
        glColor3f(0.0,0.0,1.0)	
        glVertex3f( self.size,-self.size, self.size)
        
        glColor3f(1.0,0.0,0.0)	
        glVertex3f( 0.0, self.size, 0.0)
        glColor3f(0.0,0.0,1.0)	
        glVertex3f( self.size,-self.size, self.size)
        glColor3f(0.0,1.0,0.0)	
        glVertex3f( self.size,-self.size, -self.size)
        
        glColor3f(1.0,0.0,0.0)	
        glVertex3f( 0.0, self.size, 0.0)
        glColor3f(0.0,1.0,0.0)	
        glVertex3f( self.size,-self.size, -self.size)
        glColor3f(0.0,0.0,1.0)	
        glVertex3f(-self.size,-self.size, -self.size)
            
        glColor3f(1.0,0.0,0.0)	
        glVertex3f( 0.0, self.size, 0.0)
        glColor3f(0.0,0.0,1.0)	
        glVertex3f(-self.size,-self.size,-self.size)
        glColor3f(0.0,1.0,0.0)	
        glVertex3f(-self.size,-self.size, self.size)
        glEnd()
        glPopMatrix()
    

        
class cube():
    def __init__(self,pos=(0.,0.,0.),rot=(0.,0.,0.),rotSpeed=2,size=6):
        self.rot_x=0.
        self.rot_y=0.
        self.rot_z=0.
        self.trn_x=pos[0]
        self.trn_y=pos[1]
        self.trn_z=pos[2]
        self.size=size
        self.dRot=rot
        self.rotSpeed=rotSpeed
        
    def update(self,dt=0.):
        self.rot_x+=self.dRot[0]*dt*self.rotSpeed
        self.rot_y+=self.dRot[1]*dt*self.rotSpeed
        self.rot_z+=self.dRot[2]*dt*self.rotSpeed
        
    def draw(self):
        glPushMatrix()
        glTranslatef(self.trn_x,self.trn_y,self.trn_z)
        glRotatef(self.rot_x,1.0,0.0,0.0)
        glRotatef(self.rot_y,0.0,1.0,0.0)
        glRotatef(self.rot_z,0.0,0.0,1.0)

        draw_localAxis()

        glBegin(GL_QUADS)	
        
        glColor3f(0.0,1.0,0.0)
        glVertex3f( self.size, self.size,-self.size)
        glVertex3f(-self.size, self.size,-self.size)		
        glVertex3f(-self.size, self.size, self.size)		
        glVertex3f( self.size, self.size, self.size)		
        
        glColor3f(1.0,0.5,0.0)	
        glVertex3f( self.size,-self.size, self.size)
        glVertex3f(-self.size,-self.size, self.size)		
        glVertex3f(-self.size,-self.size,-self.size)		
        glVertex3f( self.size,-self.size,-self.size)		
        
        glColor3f(1.0,0.0,0.0)		
        glVertex3f( self.size, self.size, self.size)
        glVertex3f(-self.size, self.size, self.size)		
        glVertex3f(-self.size,-self.size, self.size)		
        glVertex3f( self.size,-self.size, self.size)		
        
        glColor3f(1.0,1.0,0.0)	
        glVertex3f( self.size,-self.size,-self.size)
        glVertex3f(-self.size,-self.size,-self.size)
        glVertex3f(-self.size, self.size,-self.size)		
        glVertex3f( self.size, self.size,-self.size)		
        
        glColor3f(0.0,0.0,1.0)	
        glVertex3f(-self.size, self.size, self.size)
        glVertex3f(-self.size, self.size,-self.size)		
        glVertex3f(-self.size,-self.size,-self.size)		
        glVertex3f(-self.size,-self.size, self.size)		
        
        glColor3f(1.0,0.0,1.0)	
        glVertex3f( self.size, self.size,-self.size)
        glVertex3f( self.size, self.size, self.size)
        glVertex3f( self.size,-self.size, self.size)		
        glVertex3f( self.size,-self.size,-self.size)		
        glEnd()
        glPopMatrix()


class camera():
    def __init__(self,pos=(0.,0.,0.),rot=(0.,0.,0.),window=None,speed=200):
        self.rot_x=rot[0]
        self.rot_y=rot[0]
        self.rot_z=rot[0]
        self.trn_x=pos[0]
        self.trn_y=pos[1]
        self.trn_z=pos[2]
        self.speed=speed
        
        self.keys=key.KeyStateHandler()
        window.push_handlers(self.keys)

    def update(self,dt=0.):
        if self.keys[key.W]: 
            yrotrad = (self.rot_y / 180 * pi) 
            xrotrad = (self.rot_x / 180 * pi) 
            self.trn_x -= float(sin(yrotrad)) * dt * self.speed 
            self.trn_z += float(cos(yrotrad)) * dt * self.speed 
            self.trn_y += float(sin(xrotrad)) * dt * self.speed 
        if self.keys[key.S]: 
            yrotrad = (self.rot_y / 180 * pi) 
            xrotrad = (self.rot_x / 180 * pi) 
            self.trn_x += float(sin(yrotrad)) * dt * self.speed 
            self.trn_z -= float(cos(yrotrad)) * dt * self.speed
            self.trn_y -= float(sin(xrotrad)) * dt * self.speed
        if self.keys[key.D]:
            yrotrad = (self.rot_y / 180 * pi) 
            self.trn_x -= float(cos(yrotrad)) * dt * self.speed
            self.trn_z -= float(sin(yrotrad)) * dt * self.speed
        if self.keys[key.A]: 
            yrotrad = (self.rot_y / 180 * pi) 
            self.trn_x += float(cos(yrotrad)) * dt * self.speed
            self.trn_z += float(sin(yrotrad)) * dt * self.speed
    
    def draw(self):
        glRotatef(self.rot_x,1,0,0) 
        glRotatef(self.rot_y,0,1,0) 
        glRotatef(self.rot_z,0,0,1) 
        glTranslatef(self.trn_x,self.trn_y,self.trn_z)
        #print "Cam tran %.2f,%.2f,%.2f"%(self.trn_x, self.trn_y, self.trn_z)
        #print "Cam rot  %.2f,%.2f,%.2f"%(self.rot_x,self.rot_y,self.rot_z)
    def getLocation(self):
        return self.trn_x,self.trn_y,self.trn_z
    
    

