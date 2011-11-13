from pyglet.gl import *
from math import *

class Gear():
    def __init__(self,inner_radius=2, outer_radius=20, width=5, teeth=36, tooth_depth=2):
        self.gear = glGenLists(1)
        glNewList(self.gear, GL_COMPILE)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        self.make_gear(inner_radius, outer_radius, width, teeth, tooth_depth)
        glEndList()

    def draw(self,inner_radius=2, outer_radius=20, width=5, teeth=18, tooth_depth=2):
        glCallList(self.gear)

    def make_gear(self,inner_radius=2, outer_radius=20, width=5, teeth=36, tooth_depth=2, fill=1):
        r0 = inner_radius
        r1 = outer_radius - tooth_depth / 2.0
        r2 = outer_radius + tooth_depth / 2.0
        da = 2.0 * pi / teeth / 4.0
        glShadeModel(GL_FLAT)
        glNormal3f(0.0, 0.0, 1.0)

        #draw front face
        glColor3f(.1,.1,.1)
        if not fill: glColor3f(0,0,0)
        glBegin(GL_QUAD_STRIP)
        for i in range(teeth+1):
            angle = i * 2.0 * pi / teeth
            glVertex3f(r0 * cos(angle), r0 * sin(angle), width * 0.5)
            glVertex3f(r1 * cos(angle), r1 * sin(angle), width * 0.5)
            if i < teeth:
                glVertex3f(r0 * cos(angle), r0 * sin(angle), width * 0.5)
                glVertex3f(r1 * cos(angle + 3 * da), r1 * sin(angle + 3 * da), width * 0.5);
        glEnd()
        
        # draw front sides of teeth
        if fill: glColor3f(.1,.1,.1)
        glBegin(GL_QUADS);
        da = 2.0 * pi / teeth / 4.0
        for i in range(teeth+1):
            angle = i * 2.0 * pi / teeth;

            glVertex3f(r1 * cos(angle), r1 * sin(angle), width * 0.5);
            glVertex3f(r2 * cos(angle + da), r2 * sin(angle + da), width * 0.5);
            glVertex3f(r2 * cos(angle + 2 * da), r2 * sin(angle + 2 * da), width * 0.5);
            glVertex3f(r1 * cos(angle + 3 * da), r1 * sin(angle + 3 * da), width * 0.5);
        glEnd();

        glNormal3f(0.0, 0.0, -1.0);

        # draw back face
        glColor3f(.1,.1,.1)
        if not fill: glColor3f(0,0,0)
        glBegin(GL_QUAD_STRIP);
        for i in range(teeth+1):
            angle = i * 2.0 * pi / teeth;
            glVertex3f(r1 * cos(angle), r1 * sin(angle), -width * 0.5);
            glVertex3f(r0 * cos(angle), r0 * sin(angle), -width * 0.5);
            if i < teeth:
                glVertex3f(r1 * cos(angle + 3 * da), r1 * sin(angle + 3 * da), -width * 0.5);
                glVertex3f(r0 * cos(angle), r0 * sin(angle), -width * 0.5);
        glEnd();

        # draw back sides of teeth
        if fill: glColor3f(.1,.1,.1)
        glBegin(GL_QUADS);
        da = 2.0 * pi / teeth / 4.0;
        for i in range(teeth+1):
            angle = i * 2.0 * pi / teeth;

            glVertex3f(r1 * cos(angle + 3 * da), r1 * sin(angle + 3 * da), -width * 0.5);
            glVertex3f(r2 * cos(angle + 2 * da), r2 * sin(angle + 2 * da), -width * 0.5);
            glVertex3f(r2 * cos(angle + da), r2 * sin(angle + da), -width * 0.5);
            glVertex3f(r1 * cos(angle), r1 * sin(angle), -width * 0.5);
        glEnd();

        #draw outward faces of teeth
        if fill: glColor3f(.1,.1,.1)
        glBegin(GL_QUAD_STRIP);
        for i in range(teeth+1):
            angle = i * 2.0 * pi / teeth;
            glVertex3f(r1 * cos(angle), r1 * sin(angle), width * 0.5);
            glVertex3f(r1 * cos(angle), r1 * sin(angle), -width * 0.5);
            u = r2 * cos(angle + da) - r1 * cos(angle);
            v = r2 * sin(angle + da) - r1 * sin(angle);
            len = sqrt(u * u + v * v);
            u /= len;
            v /= len;
            glNormal3f(v, -u, 0.0);
            glVertex3f(r2 * cos(angle + da), r2 * sin(angle + da), width * 0.5);
            glVertex3f(r2 * cos(angle + da), r2 * sin(angle + da), -width * 0.5);
            glNormal3f(cos(angle), sin(angle), 0.0);
            glVertex3f(r2 * cos(angle + 2 * da), r2 * sin(angle + 2 * da),  width * 0.5);
            glVertex3f(r2 * cos(angle + 2 * da), r2 * sin(angle + 2 * da),  -width * 0.5);
            u = r1 * cos(angle + 3 * da) - r2 * cos(angle + 2 * da);
            v = r1 * sin(angle + 3 * da) - r2 * sin(angle + 2 * da);
            glNormal3f(v, -u, 0.0);
            glVertex3f(r1 * cos(angle + 3 * da), r1 * sin(angle + 3 * da),  width * 0.5);
            glVertex3f(r1 * cos(angle + 3 * da), r1 * sin(angle + 3 * da),  -width * 0.5);
            glNormal3f(cos(angle), sin(angle), 0.0);

        glVertex3f(r1 * cos(0), r1 * sin(0), width * 0.5);
        glVertex3f(r1 * cos(0), r1 * sin(0), -width * 0.5);

        glEnd();

        glShadeModel(GL_SMOOTH);
        #draw inside radius cylinder
        if fill: glColor3f(.1,.1,.1)
        glBegin(GL_QUAD_STRIP);
        for i in range(teeth+1):
            angle = i * 2.0 * pi / teeth;
            glNormal3f(-cos(angle), -sin(angle), 0.0);
            glVertex3f(r0 * cos(angle), r0 * sin(angle), -width * 0.5);
            glVertex3f(r0 * cos(angle), r0 * sin(angle), width * 0.5);
        glEnd();
        glColor3f(1,1,1)
