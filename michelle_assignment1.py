# SID : 91148
# Name : Aint Myat Noe @ Michelle


from OpenGL.GLUT import *
from pyglet import image
from pyglet.gl import *
from pyglet.window import key
from models import grid,camera,draw_localAxis

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.quadObj = gluNewQuadric();
        self.load_textures()
    
    def draw(self):
        glPushMatrix()
        #glTexGenfv(GL_S, GL_SPHERE_MAP, .0)
        #glTexGenfv(GL_T, GL_SPHERE_MAP, .0)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        glRotatef(-90,1,0,0)
        gluCylinder(self.quadObj, self.radius, self.radius, self.height, 50,50)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glTranslatef(0,0,self.height)
        gluDisk(self.quadObj, 0, self.radius, 100, 1)
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)
        glColor3f(1,1,1)
        glPopMatrix()
    
    def load_textures(self):
        file = os.path.join('img','floor.png')
        surface = image.load(file)
        
        t1 = surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, t1.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        self.texture = t1
    

class Wall:
    def __init__(self,width=100,height=100):
        self.width = width
        self.height = height
        self.load_textures()
    
    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(0, 0, 0)
        glTexCoord2f(self.width/200, 0.0); glVertex3f(self.width, 0,  0)
        glTexCoord2f(self.width/200, self.height/300); glVertex3f(self.width, self.height, 0)
        glTexCoord2f(0.0, self.height/300); glVertex3f(0, self.height,  0)
        glEnd()
    
    def load_textures(self):
		file = os.path.join('img','wall_plain.png')
		surface = image.load(file)
		
		t1 = surface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t1.id)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		self.texture = t1
    

class Floor:
	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.load_textures()
    
	def draw(self):
		glBindTexture(GL_TEXTURE_2D, self.texture.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(0, 0, self.width)
		glTexCoord2f(2.0, 0.0); glVertex3f(self.length,0,  self.width)
		glTexCoord2f(2.0, 2.0); glVertex3f(self.length, 0, 0)
		glTexCoord2f(0.0, 2.0); glVertex3f(0, 0,  0)
		glEnd()
	
	def load_textures(self):
		file = os.path.join('img','floor.png')
		surface = image.load(file)
		
		t1 = surface.image_data.create_texture(image.Texture)
		glBindTexture(GL_TEXTURE_2D, t1.id)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		self.texture = t1
	

class Base:
    def __init__(self, base_radius, top_radius, base_height, top_height):
        self.base_radius = base_radius
        self.top_radius = top_radius
        self.base_height = base_height
        self.top_height = top_height
        self.load_textures()
    
    def draw(self):
        pass
    
    def load_textures(self):
        pass
    

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
        self.cy = Cylinder(100,50)
		
		# init
        glEnable(GL_TEXTURE_2D)
        self.load_textures()
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
    
    def load_textures(self):
        pass
    
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
    
    # your draw function
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        
        self.camera.draw()
        #self.grid.draw()
       
        glPushMatrix()
        
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
        
        # Testing
        glPushMatrix()
        #self.cy.draw()
        glPopMatrix()
        
        glPopMatrix() # final POP
        
    
# our application is created using the pygletApp class
problem_3 = pygletApp()

while not problem_3.has_exit:
    problem_3.update()
    problem_3.draw()
    problem_3.flip()
