import pyxel

class App:
    def __init__(self):
        pyxel.init(100, 40, "First Steps with Pyxel", display_scale = 5)
        self.x = pyxel.width/2
        self.speed = 1

        #Read resource file
        pyxel.load("assets/firststep.pyxres")
        
    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + self.speed) % pyxel.width

    def draw(self):
        pyxel.cls(0)

        #Image drawing:(x, y, img, u, v, w, h, [colkey])
        # xy:Copy destination coordinates, img:Image bank number
        # uv:Coordinates of copy source, wh:Copy range, colkey:Transparent color
        pyxel.blt(self.x, pyxel.height/2, 0, 0, 0, 8, 8, 0)

App().run()