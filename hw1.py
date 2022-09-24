#!/usr/bin/env python2
import sys

w, h = 10, 5
x, y = 2, 3
map = [['-' for _ in range(w)] for _ in range(h)]
def init():
	map[y][x] = '*'
	print 'Current position: ({}, {})'.format(x, y)
	for i in range(h):
		for j in range(w):
			print map[i][j],
		print ''
				
def get_cmd():
	cmd = raw_input('Press W/A/S/D to move the star(q to quit):').split()[0]
	if cmd == 'w':
		return [0, -1]
	elif cmd == 's':
		return [0, 1]
	elif cmd == 'a':
		return [-1, 0]
	elif cmd == 'd':
		return [1, 0]
	elif cmd == 'q':
		sys.exit(0)
	else:
		return -2

def move(delta_x, delta_y):
	global x, y
	map[y][x] = '-'
	x += delta_x
	y += delta_y

def main():
	while 1:
		init()
		c = get_cmd()
		if c == -2:
			print 'Bad input'
			continue
		move(c[0], c[1])
		if x<0 | y<0:
			print 'Bad position'
			continue
	return 0

if __name__ == '__main__':
	main()