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

## hw3

比前兩次還要花時間，寫完兩題大概花了我半小時
主要做三件事:
1. 先用`split()`把句子拆成單字
2. 把split完的結果用set儲存完
3. 用dict計數(還要排序 記得要reverse)

```python
#!/usr/bin/env python3

def read_file(path):
  	f = open(path, 'r')
  	return f.read()

def solve(data):
  	l = data.split()
  	substr = list(set(l))
  	tmp, ans = {}, {}
  	for i in range(len(substr)):
    	tmp[substr[i]] = 0
    	for j in range(len(l)):
     		tmp[substr[i]] += (l[j] == substr[i])
  	s = sorted(tmp.items(), key=lambda x:x[1], reverse=1)
  	for i in range(len(s)):
    	ans[s[i][0]] = s[i][1]
  	return ans

def main():
  	for i in range(5):
    	print('{}.'.format(i+1))
    	print('Counter(', end='')
    	print(solve(read_file('data/article{}.txt'.format(i+1))), end='')
    	print(')\n')

if __name__ == '__main__':
	main()
```

### 加分題

其實沒有很難 只是要做兩次substring

```python
#!/usr/bin/env python3

def main():
  	f = open('data/bonus.txt', 'r')
  	data = f.read()
  	l = data.split()
  	substr, tmp, ans = [], {}, {}
  	for i in range(len(l)-1):
		substr.append(l[i] + ' ' + l[i+1])
  	substr2 = list(set(substr))
  	for i in range(len(substr2)):
		tmp[substr2[i]] = 0
    	for j in range(len(substr)):
      		tmp[substr2[i]] += (substr[j] == substr2[i])
  	#print(substr)
  	#print(substr2)
  	#print(tmp) #debug
  	s = sorted(tmp.items(), key=lambda x:x[1], reverse=1)
  	for i in range(len(s)):
    	ans[s[i][0]] = s[i][1]
  	print('Counter(', end='')
  	print(ans, end='')
  	print(')')

if __name__ == '__main__':
	main()