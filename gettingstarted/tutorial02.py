import pyxel

# Ein paar nützliche Konstanten
TS = 8       # Tilesize
COLKEY = 0   # Color Key
WALL = 2     # Mauer Tile No.

def get_tile(tile_x, tile_y):
    # pyxel.tilemaps() gibt ein Tupel mit den x- und y-Koordinaten
    # aus der Tilemap des mit pget() identifizierten Tiles zurück
    return pyxel.tilemaps[0].pget(tile_x, tile_y)

class Player:
    
    def __init__(self, _x, _y):
        self.x = _x*TS
        self.y = _y*TS
        self.w = self.h = TS
        self.u = 0   
        self.v = 0
        self.imagebank = 0
        
    def move(self):
        if (pyxel.btnp(pyxel.KEY_LEFT) 
        and get_tile((self.x - TS)//TS, self.y//TS)[0] != WALL):            
            self.x -= TS
        elif (pyxel.btnp(pyxel.KEY_RIGHT)
        and get_tile((self.x + TS)//TS, self.y//TS)[0] != WALL):
            self.x += TS
        elif (pyxel.btnp(pyxel.KEY_UP)
        and get_tile(self.x//TS, (self.y - TS)//TS)[0] != WALL):
            self.y -= TS
        elif (pyxel.btnp(pyxel.KEY_DOWN)
        and get_tile(self.x//TS, (self.y + TS)//TS)[0] != WALL):
            self.y += TS

class App:
    
    def __init__ (self):
        pyxel.init(16*TS, 16*TS, "Pyxel Tutorial Stage 2", display_scale = 4)
        pyxel.load("assets/mazegame01.pyxres")
        
        # Initialisiere den Spieler
        # Position in Map-Koordinaten
        self.player = Player(1, 1)
        
    def run(self):
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.player.move()
        
    
    def draw(self):
        pyxel.cls(0)
        
        # Zeichen die Map
        pyxel.bltm(0, 0, 0, 0, 0, 16*TS, 16*TS, 0)
        
        # Zeichne den Player
        pyxel.blt(self.player.x, self.player.y, self.player.imagebank,
                  self.player.u, self.player.v, self.player.w, self.player.h,
                  COLKEY)
                
App().run()