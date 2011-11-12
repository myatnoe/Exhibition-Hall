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
from photo import Monalisa
import math
from math import *
from description import Description


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
        
        # Exhibits
        self.stand = DisplayStand(20,50)
        self.rubik = Rubik()
        self.rubik_des = Description(self, "Rubik Cube+Scale with Up & DOWN", 0,0)
        
        self.monalisa = Monalisa()
        self.mona_des = Description(self, "Mona Lisa Ghost+Press 'c' to see the Ghost+Press 'x' to on/off texture")
        
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
        elif sym == key.UP:
            if self.scale < 1.5:
                self.scale += .1
        elif sym == key.DOWN:
            if self.scale > 1:
                self.scale -= .1
        elif sym == key.C:
            self.monalisa.change_ghost()
        elif sym == key.X:
            self.monalisa.change_see()
    
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
        # All objects will be 'dis' far from the center point of the room
        dis = (self.floor.width/2)*0.75
        
        # Object 1  ########### ########### ########### ########### ###########
        glPushMatrix() # Object 1 push
        glRotatef(30,0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance) # Stand 1
		
        glPushMatrix() # Rubik push
        glTranslatef(0,self.stand.height*1.5,0)
        glScalef(10*self.scale,10*self.scale,10*self.scale)
        glRotatef(self.x_rot,1,0,1)
        self.rubik.draw() # Rubik cube
        glPopMatrix() # Rubik pop
        
        glPushMatrix() # Rubik description push
        glTranslatef(0,self.stand.height*1.5,self.stand.width*1.2)
        glRotatef(-90,0,1,0)
        glScalef(.2,.2,.2)
        #self.draw_localAxis()
        self.rubik_des.draw_description()
        glPopMatrix() # Rubik description pop
        glPopMatrix() # Object 1 pop
        
        # Object 2 ########### ########### ########### ########### ###########
        glPushMatrix() # Object 2 push
        glRotatef(-30, 0,1,0)
        glTranslatef(dis,0,0)
        self.stand.draw(distance)
        
        
        glPopMatrix() # Object 2 pop
        
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
        
        glPushMatrix() # MonaLisa push
        glTranslatef(0,self.stand.height*2,0)
        glRotatef(-90,0,1,0)
        glScalef(20,20,1)
        self.monalisa.draw() # MonaLisa
        glPopMatrix() # MonaLisa pop
        
        glPushMatrix() # MonaLisa description push
        glTranslatef(0,self.stand.height*1.5,self.stand.width*1.2)
        glRotatef(-90,0,1,0)
        glScalef(.2,.2,.2)
        self.mona_des.draw_description()
        glPopMatrix() # MonaLisa description pop
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
