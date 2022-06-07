import array
import os
import time


class conslx:
    def __init__(self, GAME, sleep, Bg):
        pass
        self.GAME = GAME
        self.sleep = sleep
        self.Bg = Bg
        self.MATRIX_GAME = []
        size = os.get_terminal_size()
        self.HEIGHT = size[0]
        self.WIDTH = size[1]
        self.voxels = []

    def start(self):
        self.MATRIX_GAME = [[0] * self.WIDTH for i in range(self.HEIGHT)]
        for i in range(self.HEIGHT):
            for y in range(self.WIDTH):
                self.MATRIX_GAME[i][y] = self.Bg

    def update(self):
        while self.GAME:
            for i in range(self.HEIGHT):
                for y in range(self.WIDTH):
                    self.MATRIX_GAME[i][y] = self.Bg
            time.sleep(self.sleep)
            os.system('cls' if os.name == 'nt' else 'clear')
            # Get the size
            # of the terminal
            for l in self.voxels:
                print(l)
                if isinstance(i, int):
                    pass
                else:
                    for i in range(l[1], l[1] + len(l)):
                        print(i)
                        for z in range(l[0], l[0] + len(l[i])):
                            try:
                                if l[i + 2 - l[1]][z - l[0]] == " ":
                                    i += 1
                            except:
                                i += 1
                            else:
                                self.MATRIX_GAME[i][z] = l[i + 2 - l[1]][z - l[0]]

            for i in self.MATRIX_GAME:
                for z in i:
                    print(z, end="")
                print("")

    def insert(self, obj, left, top):
        obj.insert(0, left)
        obj.insert(1, top)
        self.voxels.append(obj)

    class objekt:
        def __init__(self, obj):
            self.obj = obj

        def create(self):
            OBJ = [list(i) for i in self.obj.split('\n')]
            return OBJ
