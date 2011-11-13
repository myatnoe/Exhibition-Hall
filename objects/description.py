from pyglet.gl import *

class Description:
    def __init__(self,text='Welcome',x=0,y=0,RGB=(0,0,0)):
        self.texts = text.split('+')
        self.x = x
        self.y = y
        self.RGB = RGB
        self.get_label()
        self. width = self.get_width()
        self.height = len(self.label)*24
    
    def draw_description(self):
        #glColor3f(0,0,0)
        #border = 10
        #glPushMatrix()
        #glTranslatef(-border,-border,-border)
        #glRectf(0,0,self.width+border*2,self.height+border)
        #glPopMatrix()
        for l in self.label[::-1]:
            l.draw()
            glTranslatef(0,24,0)
            glColor3f(1,1,1)
    
    def get_label(self):
        # create the pyglet text label
        self.label = []
        for text in self.texts:
            self.label.append(pyglet.text.Label(text,
                          font_name='Arial',
                          font_size=20,
                          italic =True,
                          bold=True,
                          color=(int(self.RGB[0]*255),int(self.RGB[1]*255),int(self.RGB[2]*255),255),
                          x=self.x, y=self.y))
    
    def get_width(self):
        widths = [l.content_width for l in self.label]
        return max(widths)
    
