# HCHS_Advenced_Programming

## hw1

其實有更簡單的作法，但我想用最直觀的，直接開陣列做地圖然後在上面改就好
基本上是送分作業

注意陣列的row, column跟直觀上的x, y會相反
其他都還好

```python
#!/usr/bin/env python2
import sys

w, h = 10, 5
x, y = 2, 3
map = [['-' for _ in range(w)] for _ in range(h)]
def init(): # 設定座標 印出地圖
	map[y][x] = '*'
	print 'Current position: ({}, {})'.format(x, y)
	for i in range(h):
		for j in range(w):
			print map[i][j],
		print ''
				
def get_cmd(): #讀WASD 向上或下移動
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

def move(delta_x, delta_y): #移動座標
	global x, y
	map[y][x] = '-'
	x += delta_x
	y += delta_y

def main():
	while 1:
		init()
		c = get_cmd()
		if c == -2: #注意WASD以及Q以外的指令
			print 'Bad input'
			continue
		move(c[0], c[1])
		if x<0 | y<0: #注意出界
			print 'Bad position'
			continue
	return 0

if __name__ == '__main__':
	main()
```
