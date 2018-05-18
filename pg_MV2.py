import pyautogui as pg
import time

pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.3)
pg.hotkey('winleft','up')
pg.typewrite('youtube.com\n',0.3)
pg.hotkey('ctrl','t')
pg.typewrite('espn.com \n',0.3)
pg.hotkey('ctrl','1')
time.sleep(1)
pg.typewrite('chris smoove',0.2)
time.sleep(1)
pg.hotkey('down','enter')
pg.moveTo(415,424, 5)
pg.click

