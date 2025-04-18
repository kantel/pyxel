import pyxel

# Ein paar nützliche Konstanten
TS = 8          # Tilesize
COLKEY = 0      # Color Key
WALLS = [(2, 1)]

def get_tile(tile_x, tile_y):
    # pyxel.tilemaps() gibt ein Tupel mit den x- und y-Koordinaten
    # aus der Tilemap des mit pget() identifizierten Tiles zurück
    return pyxel.tilemaps[0].pget(tile_x, tile_y)

class Player:

    def __init__(self, _x, _y):
        self.x = _x * TS
        self.y = _y * TS
        self.w = self.h = TS
        self.u = 0  # Die x-Position des Sprites in der Imagebank
        self.v = 0  # Die y-Position des Sprites in der Imagebank
        self.imagebank = 0
        self.dir = "right"

    def move(self):
        if (pyxel.btnp(pyxel.KEY_LEFT)
                and get_tile((self.x - TS)//TS, self.y//TS) not in WALLS):
            self.dir = "left"
            self.x -= TS
        elif (pyxel.btnp(pyxel.KEY_RIGHT)
                and get_tile((self.x + TS)//TS, self.y//TS) not in WALLS):
            self.dir = "right"
            self.x += TS
        if self.dir == "left":
            self.w = -TS
        else:
            self.w = TS

class App:

    def __init__(self):
        pyxel.init(32 * TS, 8 * TS, "Pyxel Tutorial Stage 4", display_scale=4)
        pyxel.load("assets/res.pyxres")

        # Initialisiere den Spieler
        # Position in Map-Koordinaten
        self.player = Player(1, 4)

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.move()

    def draw(self):
        pyxel.cls(0)

        # Zeichen die Map
        pyxel.bltm(0, 0, 0, 0, 0, 32 * TS, 8 * TS, 0)

        # Zeichne den Player
        pyxel.blt(self.player.x, self.player.y, self.player.imagebank,
                  self.player.u, self.player.v, self.player.w, self.player.h,
                  COLKEY)

App().run()