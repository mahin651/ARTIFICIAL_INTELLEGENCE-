class Node:
def _init__(self,data,heuristic):
self.data = data
self.fval = heuristic
def children(self,puz,x1,y1,x2,y2):
i f x2 >= 0 and x2 < l en(self.data) and y2 >= 0 and y2 <
len(self.data):
temp1 = []
temp1 = self.copy(puz)
temp2 = temp1[x2][y2]
temp1[x2][y2] = temp1[x1][y1]
temp1[x1][y1] = temp2
return temp1
else:
return None
def generate_child(self):
x,y = self.blank(self.data,'_')
val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
children = []
for i i n val_list:
child = self.children(self.data,x,y,i[0],i[1])
if child is not None:
child_node = Node(child,0)
children.append(child_node)
return children
def copy(self,root):
temp = []
for i i n root:
t = []
for j i n i :
t.append(j)
temp.append(t)
return temp
def blank(self,puz,x):
for i i n range(0,len(self.data)):
for j i n range(0,len(self.data)):
i f puz[i][j] == x:
return i,j
class Puzzle:
def _init__(self,size):
self.n = size
self.open = []
self.closed = []
def accept(self):
puz = []
for i in range(0,self.n):
temp = i nput().split(" ")
puz.append(temp)
return puz
def f(self,start,goal):
return self.h(start.data,goal)
def h(self,start,goal):
temp = 0
for i i n range(0,self.n):
for j in range(0,self.n):
i f start[i][j] != goal[i][j] and start[i][j] != ' _':
temp += 1
return temp
def evaluate(self):
print("Enter the start state matrix \n")
start = self.accept()
print("Enter the goal state matrix \n")
goal = self.accept()
start = Node(start,0)
start.fval = self.f(start,goal)
self.open.append(start)
print("\n\n")
step = 0
while True:
print("iteration -> ", iteration)
cur = self.open[0]
for i i n cur.data:
for j i n i :
print(j,end=" ")
print("")
print("\n")
i f(self.h(cur.data,goal) == 0):
break
for i i n cur.generate_child():
i .fval = self.f(i,goal)
self.open.append(i)
self.closed.append(cur)
del self.open[0]
self.open.sort(key = l ambda x:x.fval,reverse=False)
step+=1
puzzle = Puzzle(3)
puzzle.evaluate()
