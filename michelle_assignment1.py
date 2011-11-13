# SID : 91148
# Name : Aint Myat Noe @ Michelle
# Git : git@github.com:myatnoe/C316-Assignment1.git

from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *
from pyglet.window import key
from objects.models import grid,camera,draw_localAxis
from objects.room import Wall, Floor, Ceiling
from objects.accessory import DisplayStand
from objects.rubik import Rubik
from objects.photo import Monalisa
from objects.pumpkin import Pumpkin
from objects.gear import Gear
import math
from math import *
from objects.description import Description

class pygletApp(pyglet.window.Window):
    def __init__(self):
        super(pygletApp, self).__init__(width=800,height=600)
        self.set_fullscreen(True)
        self.set_exclusive_mouse(True)
        self.grid    = grid(size=300)
        self.camera  = camera(pos=(0., -100., -550.),rot=(0.,0.,0.),window=self,speed=400)
        self.renderMode=GL_FILL
        
        self.light = False
        LightAmbient  = (GLfloat*4)(0.5, 0.5, 0.5, 1.0)
        LightDiffuse  = (GLfloat*4)(1.0, 1.0, 1.0, 1.0)
        LightPosition = (GLfloat*4)(0.0, 0.0, 2.0, 1.0)
        
        self.wall = Wall(600,300)
        self.floor = Floor(600,600)
        self.ceiling = Ceiling(600,600)
        
        # Exhibits
        self.show_des = True
        self.stand = DisplayStand(20,50)
        self.rubik = Rubik()
        self.rubik_des = Description("Rubik Cube+Scale with Up & DOWN")
        
        self.monalisa = Monalisa()
        self.mona_des = Description("Mona Lisa Ghost+Press 'c' to see the Ghost+Press 'x' to on/off texture")
        
        self.pumpkin = Pumpkin(60,60)
        self.pumpkin_des = Description("Cinderella Carriage+'p' to rotate pumpkin on X axis+'o' to rotate wheel on Z axis+'i' to rotate the carriage on Y axis")
        
        self.gear = Gear()
        self.rubik_rot = self.gear_rot = 0
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
            self.show_des = not self.show_des
        elif sym == key.UP:
            if self.scale < 1.5:
                self.scale += .1
        elif sym == key.DOWN:
            if self.scale > .5:
                self.scale -= .1
        elif sym == key.C:
            self.monalisa.change_ghost()
        elif sym == key.X:
            self.monalisa.change_see()
        elif sym == key.P:
            self.pumpkin.rotate_pumpkin()
        elif sym == key.O:
            self.pumpkin.rotate_wheel()
        elif sym == key.I:
            self.pumpkin.rotate_whole()
    
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
        
        self.rubik_rot += 1
        self.rubik_rot %= 360
        self.gear_rot += 1
        self.gear_rot %= 360
        
        self.pumpkin.update()
        
    
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
        # All objects will be 'dis' far from the center point of the room
        dis = (self.floor.width/2)*0.75
        
        ############ ########### ########### ########### ###########
        glPushMatrix() # Object 1 push
        glRotatef(30,0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance) # Stand 1
		
        glPushMatrix() # Rubik push
        glTranslatef(0,self.stand.height*1.5,0)
        glScalef(10*self.scale,10*self.scale,10*self.scale)
        glRotatef(self.rubik_rot,0,1,1)
        self.rubik.draw() # Rubik cube
        glPopMatrix() # Rubik pop
        
        glPushMatrix() # Rubik description push
        glTranslatef(0,self.stand.height*1.5,self.stand.width*1.2)
        glRotatef(-90,0,1,0)
        glScalef(.2,.2,.2)
        if self.show_des:
            self.rubik_des.draw_description()
        glPopMatrix() # Rubik description pop
        glPopMatrix() # Rubik pop
        
        ############ ########### ########### ########### ###########        
        glPushMatrix() # Pumpkin push
        glRotatef(-30,0,1,0)
        glTranslatef(-dis,self.pumpkin.height*1.5,0)
        self.pumpkin.draw() # Pumpkin cube
        glPopMatrix() # Pumpkin pop
        
        glPushMatrix() # Pumpkin description push
        glRotatef(-30,0,1,0)
        glTranslatef(-dis,0,0)
        glTranslatef(0,self.pumpkin.height*1.5,-self.pumpkin.width*1.5)
        glRotatef(90,0,1,0)
        glScalef(.2,.2,.2)
        if self.show_des:
            self.pumpkin_des.draw_description()
        glPopMatrix() # Pumpkin description pop
        
        ############ ########### ########### ########### ###########
        glPushMatrix()
        glRotatef(-270, 0,1,0)
        glTranslatef(dis,0,0)
        #self.stand.draw(distance)
        
        glPushMatrix() # MonaLisa push
        glTranslatef(0,self.stand.height*3,0)
        glRotatef(-90,0,1,0)
        glScalef(40,40,1)
        self.monalisa.draw() # MonaLisa
        glPopMatrix() # MonaLisa pop
        
        glPushMatrix() # MonaLisa description push
        glTranslatef(-10,self.stand.height*1.5,self.stand.width*2.5)
        glRotatef(-90,0,1,0)
        glScalef(.2,.2,.2)
        if self.show_des:
            self.mona_des.draw_description()
        glPopMatrix() # MonaLisa description pop
        glPopMatrix() # Mona Lisa Pop
        
        glPushMatrix() # Gear push
        glTranslatef(200,200,-300+2.5)
        self.gear.draw()
        glPushMatrix()
        glRotatef(self.gear_rot,0,0,1)
        glTranslatef(40,0,0)
        glRotatef(self.gear_rot-1.5,0,0,1)
        self.gear.draw()
        glPopMatrix()
        glPopMatrix() # Gear pop
        
        glPushMatrix() # Gear push
        glTranslatef(-200,200,-300+2.5)
        self.gear.draw()
        glPushMatrix()
        glRotatef(-self.gear_rot,0,0,1)
        glTranslatef(-40,0,0)
        glRotatef(-self.gear_rot-1.5,0,0,1)
        self.gear.draw()
        glPopMatrix()
        glPopMatrix() # Gear pop
        
        glPopMatrix() # final POP
    
    def draw_room(self):
        # ==== FLOOR & WALLS
        glPushMatrix()
        glTranslatef(-300,0,-300)
        self.floor.draw()
        self.wall.draw()  # Wall 1
        glPopMatrix()
        
        # ==== WALL Left
        glPushMatrix()
        glTranslatef(-300,0,300)
        glRotatef(90,0,1,0)
        self.wall.draw()
        glPopMatrix() # Wall 2 pop
        
        # ==== WALL Right
        glPushMatrix()
        glTranslatef(300,0,-300)
        glRotatef(-90,0,1,0)
        self.wall.draw()
        glPopMatrix() # Right Wall Pop
        
        # ==== Ceiling
        glPushMatrix()
        glTranslatef(-300,300,-300)
        self.ceiling.draw()
        glPopMatrix()
    
    def draw_localAxis(self):
        localAxis = pyglet.graphics.vertex_list(6, 
            ('v3f/static', (0.0,0,0.0,25,0,0.0,0.0,0,0.0,0.0,25, 0.0,0.0,0,0.0,0.0,0.0,25)), 
            ('c3B/static', (255,0,0,255,0,0,0,255,0,0,255,0,0,0,255,0,0,255)))
        glLineWidth(4)
        localAxis.draw(GL_LINES)
        glLineWidth(1)
    

# our application is created using the pygletApp class
problem_3 = pygletApp()

while not problem_3.has_exit:
    problem_3.update()
    problem_3.draw()
    problem_3.flip()
