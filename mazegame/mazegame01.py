import pyxel

class App:
    
    def __init__(self):
        pyxel.init(128, 128, "Maze Game 1")
        
        # Read resource file
        pyxel.load("assets/mazegame01.pyxres")
        
    def run(self):
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        
        #Background drawing:(x, y, tm, u, v, w, h, colkey)
        # xy:Coordinates of copy destination, tm:Tile map number
        # uv:Coordinates of copy source, wh:Copy range, col transparent color
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128, 1)
        
        #Image drawing:(x, y, img, u, v, w, h, [colkey])
        # xy:Copy destination coordinates, img:Image bank number
        # uv:Coordinates of copy source, wh:Copy range, colkey:Transparent color
        pyxel.blt(16, 16, 0, 32, 16, 16, 16, 1)

App().run()