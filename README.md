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


## hw2

這周的作業感覺比上次更佛了，只要讀檔，然後sort完就好
注意比較刁鑽的地方是資料之間用了`\t`做間隔，不過參考講義內已經附的處理方式很輕鬆就能解


法1:用講義內方式
```python
data = f.read().rstrip().replace('\\t', '\t')
l = data.split()
```

法2:用`re`然後同時split `\t`和`\n`

最後處理印出來的順序，記得倒過來符合要求
p.s一開始沒看到要由大往小輸出，沒加`reverse=True`，所以寫很醜==

```python
def read_sort(path):
	f = open(path)
	data = f.read().rstrip().replace('\\t', '\t')
	l = data.split()
	for i in range(len(l)):
		l[i] = int(l[i])
	for i in range(len(sorted(l))):
		print(sorted(l)[len(sorted(l))-i-1], end=", "[i == len(sorted(l))-1])
	print("")

for i in range(5):
	read_sort("data/test{}.tsv".format(i+1))
```

輸出結果:
```
1 
3,2,1 
1,1,1 
5,4,3,2,1 
11,4,3,2,1 
```
