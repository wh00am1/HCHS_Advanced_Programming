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
注意比較刁鑽的地方是資料之間用了`\\t`做間隔，不過參考講義內已經附的處理方式很輕鬆就能解

```python
data = f.read().rstrip().replace('\\t', '\t')
l = data.split()
```
記得由大而小依序輸出

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
```

## hw4
### 4-1

與hw3性質類似，只是多一層`name`的判定

```python
def counter(l):
  substr = list(set(l))
  tmp = {}
  for i in range(len(substr)):
    tmp[substr[i]] = 0
    for j in range(len(l)):
      tmp[substr[i]] += (l[j] == substr[i])
  s, res = sorted(tmp.items(), key=lambda x:x[1], reverse=1), {}
  for i in range(len(s)):
    res[s[i][0]] = s[i][1]
  return res

def solve(path):
  f = open(path, 'r')
  #print('#####File: {}'.format(path))
  p, tmp = [], []
  for l in f.readlines():
    tmp.append(l)
    p.append(l.split()[0])
  p = list(set(p))
  for i in range(len(p)):
    #print('#####Name: {}'.format(p[i]))
    w = open('data/{}.txt'.format(p[i]), 'w+')
    owo = []
    for j in range(len(tmp)):
      s = tmp[j].split()
      if s[0] == p[i]:
        owo.append(s[1])
    ans = counter(owo)
    for k, v in ans.items():
      #print('{} {}'.format(k, v))
      w.write('{} {}\n'.format(k, v))
    w.close()
  f.close()

for i in range(5):
  solve('data/file{}.txt'.format(i+1))
```

### 4-2

送分題，讓你熟悉`Class`操作而已，max跟min的地方用迭代可以 $O(N)$ ，懶得打字所以用 $O(NlogN)$  的排序

中位數的index可用奇偶數性質推得


```python
class SalaryDistribution:
  def __init__(self, salary):
    self.salary = salary
  def min(self):
    tmp = sorted(self.salary, reverse=0)
    return tmp[0]
  def max(self):
    tmp = sorted(self.salary, reverse=1)
    return tmp[0]
  def median(self):
    tmp = sorted(self.salary)
    if len(self.salary) == 1:
      return self.salary[0]
    elif len(self.salary) % 2 == 0:
      idx = int(len(self.salary)/2)
      return (tmp[idx] + tmp[idx+1])/2
    else:
      idx = (len(self.salary)-1)/2 + 1
      return tmp[int(idx)]
  def mean(self):
    sum = 0
    for i in range(len(self.salary)):
      sum += self.salary[i]
    return sum/len(self.salary)

def main():
  for i in range(5):
    f = open('data/test{}.txt'.format(i+1))
    l = f.readline().split()
    for i in range(len(l)):
      l[i] = int(l[i])
    s = SalaryDistribution(l)
    print('min: ', s.min())
    print('max: ', s.max())
    print('median: ', s.median())
    print('mean: ', s.mean())

if __name__ == '__main__':
  main()
```