import pyxel

# Ein paar nützliche Konstanten
TS = 8  # Tilesize
COLKEY = 0  # Color Key
PLAYER_WALK_CYCLE = [(0, 24), (8, 24), (0, 24), (16, 24)]
WALLS = [(0, 1), (1, 1), (2, 1), (3, 1),
         (0, 2), (1, 2), (2, 2), (0, 3), (1, 3)]


def get_tile(tile_x, tile_y):
    # pyxel.tilemaps() gibt ein Tupel mit den x- und y-Koordinaten
    # aus der Tilemap des mit pget() identifizierten Tiles zurück
    return pyxel.tilemaps[0].pget(tile_x, tile_y)


class Player:

    def __init__(self, _x, _y):
        self.x = _x * TS
        self.y = _y * TS
        self.w = self.h = TS
        self.u = 0   # Die x-Position des Sprites in der Imagebank (in Pixeln)
        self.v = 24  # Die y-Position des Sprites in der Imagebank (in Pixeln)
        self.imagebank = 0
        self.speed = 2
        self.frame_index = 0  # Current frame in the sprite sheet
        self.animation_speed = 5  # Lower = faster animation
        self.animation_counter = 0  # Tracks frame updates

    def update(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(PLAYER_WALK_CYCLE)
            self.u, self.v = PLAYER_WALK_CYCLE[self.frame_index]
            self.animation_counter = 0

    def move(self):
        if (pyxel.btnp(pyxel.KEY_LEFT)
                and get_tile((self.x - TS) // TS, self.y // TS) not in WALLS):
            self.x -= TS
        elif (pyxel.btnp(pyxel.KEY_RIGHT)
              and get_tile((self.x + TS) // TS, self.y // TS) not in WALLS):
            self.x += TS
        elif (pyxel.btnp(pyxel.KEY_UP)
              and get_tile(self.x // TS, (self.y - TS) // TS) not in WALLS):
            self.y -= TS
        elif (pyxel.btnp(pyxel.KEY_DOWN)
              and get_tile(self.x // TS, (self.y + TS) // TS) not in WALLS):
            self.y += TS


class App:

    def __init__(self):
        pyxel.init(32 * TS, 16 * TS, "Pyxel Tutorial Stage 6", display_scale=4)
        pyxel.load("assets/res.pyxres")

        # Initialisiere den Spieler
        # Position in Map-Koordinaten
        self.player = Player(1, 1)

    def run(self):
        print(get_tile(0, 0))
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.player.move()

    def draw(self):
        pyxel.cls(0)

        # Zeichen die Map
        pyxel.bltm(0, 0, 0, 0, 0, 32 * TS, 16 * TS, 0)

        # Zeichne den Player
        pyxel.blt(self.player.x, self.player.y, self.player.imagebank,
                  self.player.u, self.player.v, self.player.w, self.player.h,
                  COLKEY)


App().run()