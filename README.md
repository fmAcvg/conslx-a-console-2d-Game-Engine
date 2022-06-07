# conslx-a-console-2d-Game-Engine
![alt text](https://github.com/fmAcvg/conslx-a-console-2d-Game-Engine/blob/master/Unbenannt.png)
import time

from conslx.main import conslx
from threading import Thread

obj = """
      ,~~.
     (  9 )-_,
(\___ )=='-'
 \ .   ) )
  \ `-' /
   `~j-' 
     "=:
"""
GAME = True
Threads = []
con = conslx(GAME=GAME, sleep=0.1, Bg=" ")
con.start()


def main():
    con.update()


duck = con.objekt(obj=obj).create()
print(duck)
process = Thread(target=main)
process.start()
con.insert(obj=duck, left=10, top=5)
time.sleep(3)
