import pyxel as px

TS = 8   # Tilesize

class App:
    def __init__(self):
        px.init(10*TS, 10*TS, "Pyxel-Tutorial 1", display_scale = 5)
        self.x = 0   # px.width/2
        self.y = 0   # px.height/2
        self.speed = TS

        #Read resource file
        px.load("assets/firststep.pyxres")
        
        px.run(self.update, self.draw)
        
    def update(self):
        if px.btnp(px.KEY_RIGHT):
            if self.x + self.speed >= px.width - TS:
                self.x = px.width - TS
            else:
                self.x += self.speed
        elif px.btnp(px.KEY_LEFT):
            if self.x - self.speed <= 0:
                self.x = 0
            else:
                self.x -= self.speed
        elif px.btnp(px.KEY_UP):
            if self.y - self.speed <= 0:
                self.y = 0
            else:
                self.y -= self.speed
        elif px.btnp(px.KEY_DOWN):
            if self.y + self.speed >= px.height - TS:
                self.y = px.height - TS
            else:
                self.y += self.speed
            

    def draw(self):
        px.cls(3)

        #Image drawing:(x, y, img, u, v, w, h, [colkey])
        # xy:Copy destination coordinates, img:Image bank number
        # uv:Coordinates of copy source, wh:Copy range, colkey:Transparent color
        px.blt(self.x, self.y, 0, 0, 0, 8, 8, 0)

App()