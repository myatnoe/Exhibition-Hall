# SID : 91148
# Name : Aint Myat Noe @ Michelle


from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *
from pyglet.window import key
from models import grid,camera,draw_localAxis
from room import Wall, Floor
from accessory import DisplayStand
from rubik import Rubik
import math
from math import *


class pygletApp(pyglet.window.Window):
    def __init__(self):
        super(pygletApp, self).__init__(width=800,height=600)
        
        self.set_exclusive_mouse(True)
        self.grid    = grid(size=300)
        self.camera  = camera(pos=(0., -100., -750.),rot=(0.,0.,0.),window=self)
        self.renderMode=GL_FILL
        
        self.light = False
        LightAmbient  = (GLfloat*4)(0.5, 0.5, 0.5, 1.0)
        LightDiffuse  = (GLfloat*4)(1.0, 1.0, 1.0, 1.0)
        LightPosition = (GLfloat*4)(0.0, 0.0, 2.0, 1.0)
        
        self.wall1 = Wall(600,300)
        self.floor = Floor(600,600)
        
        # Testing
        self.stand = DisplayStand(20,50)
        self.rubik = Rubik()
        
        self.x_rot = self.y_rot = self.z_rot = 0
        self.scale = 1
		
		# init
        glEnable(GL_TEXTURE_2D)
        #self.load_textures()
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glLightfv( GL_LIGHT1, GL_AMBIENT, LightAmbient )
        glLightfv( GL_LIGHT1, GL_DIFFUSE, LightDiffuse )
        glLightfv( GL_LIGHT1, GL_POSITION, LightPosition )
        glEnable( GL_LIGHT1 )
    
    def on_mouse_motion(self,x, y, dx, dy):
        self.camera.rot_y += dx / 4. 
        self.camera.rot_x -= dy / 4.
    
    def on_key_press(self,sym, mod):
        if sym == key.ESCAPE:   # stop the program
            self.has_exit = True
        elif sym == key.F:        # toggle between windows and fullscreen
            if mod == key.MOD_SHIFT:
                self.set_fullscreen(not self.fullscreen)
            #else:
                #self.filter = (self.filter + 1) % 2
        elif sym == key.G:        
            if self.renderMode==GL_FILL:
                self.renderMode=GL_LINE
            else:
                self.renderMode=GL_FILL
            glPolygonMode(GL_FRONT_AND_BACK, self.renderMode)
        elif sym == key.L:
            self.light = not self.light
            if not self.light:
                glDisable(GL_LIGHTING)
            else:
                glEnable(GL_LIGHTING)
        elif sym == key.C:
            if mod == key.MOD_SHIFT:
                if self.scale < 1.5:
                    self.scale += .1
            else:
                if self.scale > 1:
                    self.scale -= .1
    
    # Function that sets the camera to 3D mode           
    def on_resize(self,width, height): 
        glViewport(0, 0, self.width, self.height) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective(30., self.width / float(self.height), .1, 8000.)
        glMatrixMode(GL_MODELVIEW) 
        return pyglet.event.EVENT_HANDLED
    
    # your update function
    def update(self):
        self.dispatch_events()
        dt=pyglet.clock.tick()
        
        #update everything
        self.camera.update(dt)
        self.grid.update(dt)
        
        # TODO: update
        self.stand.update()
        
        self.x_rot += 1
        self.x_rot %= 360
        self.y_rot += 1
        self.y_rot %= 360
        self.z_rot += 1
        self.z_rot %= 360
        
    
    # your draw function
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        
        glPushMatrix()
        self.camera.draw()
        #self.grid.draw()
        cx,cy,cz=self.camera.getLocation()
    	distance=sqrt(cx*cx+cy*cy+cz*cz)
        
        # Wall & Floors
        self.draw_room()
        
        # Objects
        dis = (self.floor.width/2)*0.75
        
        # Object 1
        glPushMatrix()
        glRotatef(30,0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance)
		
        glPushMatrix()
        glTranslatef(0,self.stand.height*1.5,0)
        glScalef(10*self.scale,10*self.scale,10*self.scale)
        glRotatef(self.x_rot,1,0,1)
        self.rubik.draw()
        glPopMatrix()
        glPopMatrix()
        
        # Object 2
        glPushMatrix()
        glRotatef(-30, 0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance)
        glPopMatrix()
        
        glPushMatrix()
        glRotatef(-150, 0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance)
        glPopMatrix()
        
        glPushMatrix()
        glRotatef(-210, 0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance)
        glPopMatrix()
        
        glPushMatrix()
        glRotatef(-270, 0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance)
        glPopMatrix()
        
        glPopMatrix() # final POP
    
    def draw_room(self):
        
        # ==== FLOOR & WALLS
        glPushMatrix()
        glTranslatef(-300,0,-300)
        self.floor.draw()
        self.wall1.draw()  # Wall 1
        glPopMatrix()
        
        # ==== WALL Left
        glPushMatrix()
        glTranslatef(-300,0,300)
        glRotatef(90,0,1,0)
        self.wall1.draw()
        glPopMatrix() # Wall 2 pop
        
        # ==== WALL Right
        glPushMatrix()
        glTranslatef(300,0,-300)
        glRotatef(-90,0,1,0)
        self.wall1.draw()
        glPopMatrix() # Right Wall Pop
    

            
# our application is created using the pygletApp class
problem_3 = pygletApp()

while not problem_3.has_exit:
    problem_3.update()
    problem_3.draw()
    problem_3.flip()
