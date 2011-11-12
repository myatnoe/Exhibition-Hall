from pyglet.gl import *

class Description:
    def __init__(self,window,text='Welcome',x=0,y=0,RGB=(1,1,1)):
        self.window = window
        self.texts = text.split('+')
        self.x = x
        self.y = y
        self.RGB = RGB
        self.get_label()
    
    def draw_description(self):
        for l in self.label:
            l.draw()
            glTranslatef(0,-24,0)
    
    def get_label(self):
        # create the pyglet text label
        self.label = []
        for text in self.texts:
            self.label.append(pyglet.text.Label(text,
                          font_name='Arial',
                          font_size=20,
                          italic =True,
                          color=(int(self.RGB[0]*255),int(self.RGB[1]*255),int(self.RGB[2]*255),255),
                          x=self.x, y=self.y))
    
