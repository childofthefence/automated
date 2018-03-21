import pyautogui
from random import randint
import time

def move_cursor_and_wait(time_stop):
	
	pyautogui.PAUSE = 1  # wait one second before taking control of cursor
	pyautogui.FAILSAFE = True
	width, height = pyautogui.size()
	
	while True:
		
		# move cursor somewhere random on screen
		move_x = randint(0, width)
		move_y = randint(0, height)
		
		pyautogui.moveTo(move_x, move_y, duration=0.25)
		
		# wait, minutes depending on passed parameter
		time_to_wait = time_stop * 60  # this will be how many minutes between each move
		print('Before: %s' % time.ctime())
		print('\nLocation: x: %d y: %d' % (move_x, move_y))
		time.sleep(time_to_wait)
		print('After: %s\n' % time.ctime())
		
		
move_cursor_and_wait(3)