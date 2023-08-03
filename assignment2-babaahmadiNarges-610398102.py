# %%
Goal_State =  [i for i in range (1, 9)]
Goal_State.append(0)

#%%
def get_input():
	inp = input()
	n = inp[2:-2].split(",")
	x = [int(i) for i in n]
	return x

def parse_input(inp):
	n = inp[2:-2].split(",")
	x = [int(i) for i in n]
	return x

# %%
def show_board(board):
	print("=========")
	print("||", board[0], "|", board[1], "|", board[2], "||")
	print("------------")
	print("||", board[3], "|", board[4], "|", board[5], "||")
	print("------------")
	print("||", board[6], "|", board[7], "|", board[8], "||")
	print("=========")

# %%
def push_up(board):
	temp_board = board.copy()
	z = temp_board.index(0)
	if (z >= 3):
		temp_board[z], temp_board[z-3] = temp_board[z-3], temp_board[z]
		return temp_board
	else:
		return -1

def push_down(board):
	temp_board = board.copy()
	z = temp_board.index(0)
	if (z <= 5):
		temp_board[z], temp_board[z+3] = temp_board[z+3], temp_board[z]
		return temp_board
	else:
		return -1

def push_left(board):
	temp_board = board.copy()
	z = temp_board.index(0)
	if (z not in [0, 3, 6]):
		temp_board[z], temp_board[z-1] = temp_board[z-1], temp_board[z]
		return temp_board
	else:
		return -1

def push_right(board):
	temp_board = board.copy()
	z = temp_board.index(0)
	if (z not in [2, 5, 8]):
		temp_board[z], temp_board[z+1] = temp_board[z+1], temp_board[z]
		return temp_board
	else:
		return -1

def move(board, move_op):
	if (move_op == "U"):
		return push_up(board)
	elif (move_op == "D"):
		return push_down(board)
	elif (move_op == "L"):
		return push_left(board)
	elif (move_op == "R"):
		return push_right(board)

# %%
class TreeNode:
	def __init__(self, board, par, last_move, depth, cost):
		self.board = board
		self.par = par
		self.last_move = last_move
		self.depth = depth
		self.cost = cost
		self.h = 0

# %%
def get_children(node):
	children = []
	for c in ["U", "D", "L", "R"]:
		new_node = TreeNode(move(node.board, c), node, c, node.depth+1, 0)
		if new_node.board != -1:
			children.append(new_node)
	return children
		

# %%
from http.client import GONE
import time

def bfs(root, goal):
	start_time = time.process_time()
	queue = []
	root_node = TreeNode(root, -1, None, 0, 0)
	goal_node = TreeNode(goal, None, None, 0, 0)

	v = root_node
	marked = set()
	marked.add(tuple(root_node.board))

	while v.board != goal:
		if (time.process_time() - start_time) > 120:
			return -1
			# It is taking too long !!! :(

		temp_children = get_children(v)
		children = []
		for u in temp_children:
			if (tuple(u.board) not in marked):
				children.append(u)

		# print(len(children))
		queue.extend(children)
		v = queue.pop(0)
				
		marked.add(tuple(v.board))

	if (v.board != goal):
		return -1

	path = []
	u = v
	while u.par != -1:
		path.append(u.last_move)
		u = u.par
	path.reverse()

	return (path, v.depth, time.process_time()-start_time)


# %%
def dfs(root, goal):
	start_time = time.process_time()
	stack = []
	root_node = TreeNode(root, -1, None, 0, 0)

	stack.append(root_node)
	marked = set()
	marked.add(tuple(root_node.board))

	while len(stack):
		if (time.process_time() - start_time) > 120:
			return -1
			# It is taking too long !!! :(

		v = stack.pop()
		marked.add(tuple(v.board))

		if (v.board == goal):
			break

		# show_board(v.board)

		temp_children = get_children(v)
		children = []
		for u in temp_children:
			if (tuple(u.board) not in marked):
				children.append(u)

		stack.extend(children)				

	if (v.board != goal):
		return -1

	path = []
	u = v
	while u.par != -1:
		path.append(u.last_move)
		u = u.par
	path.reverse()

	return (path, v.depth, time.process_time()-start_time)

# %%
def uni_cost(root, goal):
	start_time = time.process_time()
	queue = []
	root_node = TreeNode(root, -1, None, 0, 0)

	v = root_node
	marked = set()
	marked.add(tuple(root_node.board))

	while v.board != goal:
		if (time.process_time() - start_time) > 120:
			return -1
			# It is taking too long !!! :(

		# show_board(v.board)
		# print(v.depth)

		temp_children = get_children(v)
		children = []
		for u in temp_children:
			if (tuple(u.board) not in marked):
				children.append(u)

		# print(len(children))
		queue.extend(children)
		queue.sort(key=lambda n: n.depth)
		v = queue.pop(0)
				
		marked.add(tuple(v.board))

	if (v.board != goal):
		return -1

	path = []
	u = v
	while u.par != -1:
		path.append(u.last_move)
		u = u.par
	path.reverse()

	return (path, v.depth, time.process_time()-start_time)

def ids(root, goal, depth_lim = 20):
	start_time = time.process_time()
	stack = []
	root_node = TreeNode(root, -1, None, 0, 0)

	stack.append(root_node)
	marked = set()
	marked.add(tuple(root_node.board))

	while len(stack):
		if (time.process_time() - start_time) > 120:
			return -5
			# It is taking too long !!! :(		

		v = stack.pop()
		marked.add(tuple(v.board))

		if (v.board == goal):
			break

		# show_board(v.board)
		# print(v.depth)

		if (v.depth < depth_lim):
			temp_children = get_children(v)
			children = []
			for u in temp_children:
				if (tuple(u.board) not in marked):
					children.append(u)

			stack.extend(children)				

	if (v.board != goal):
		return -1

	path = []
	u = v
	while u.par != -1:
		path.append(u.last_move)
		u = u.par
	path.reverse()

	return (path, v.depth, time.process_time()-start_time)

def sum_manhattan_dist(board):
	z = board.index(0)
	sum = (2 - z//3) + (2 - (z%3))
	for i in range(1, 9):
		cur = board.index(i)
		sum += (abs((i-1)//3 - cur//3) + abs((i-1)%3 - cur%3))
	return sum

def A_star(root, goal):
	start_time = time.process_time()
	queue = []
	root_node = TreeNode(root, -1, None, 0, 0)

	v = root_node
	marked = set()
	marked.add(tuple(root_node.board))

	while v.board != goal:
		if (time.process_time() - start_time) > 120:
			return -1
			# It is taking too long !!! :(

		# show_board(v.board)
		# print(v.depth)

		temp_children = get_children(v)
		children = []
		for u in temp_children:
			if (tuple(u.board) not in marked):
				children.append(u)

		# print(len(children))
		queue.extend(children)
		queue.sort(key=lambda n: n.depth + sum_manhattan_dist(n.board))
		v = queue.pop(0)
				
		marked.add(tuple(v.board))

	if (v.board != goal):
		return -1

	path = []
	u = v
	while u.par != -1:
		path.append(u.last_move)
		u = u.par
	path.reverse()

	return (path, v.depth, time.process_time()-start_time)


# %%
input_file = open("Examples.txt", "r")
out_file = open("out.txt", "w")

cnt = 0
import tracemalloc
for line in input_file:
	out_file.write(str(line) + "\n")
	root = parse_input(line)
	out_file.write(str(cnt) + "\n")
	cnt += 1

	tracemalloc.start()
	out_file.write("A*" + str(A_star(root, Goal_State)) + "\n")
	a, b = tracemalloc.get_traced_memory()
	out_file.write( str((b-a) / 1000) + "KB" + "\n")

	tracemalloc.start()
	out_file.write("bfs" + str(bfs(root, Goal_State)) + "\n")
	a, b = tracemalloc.get_traced_memory()
	out_file.write( str((b-a) / 1000) + "KB" + "\n")

	tracemalloc.start()
	out_file.write("ids" + str(ids(root, Goal_State)) + "\n")
	a, b = tracemalloc.get_traced_memory()
	out_file.write( str((b-a) / 1000) + "KB" + "\n")

	tracemalloc.start()
	out = str(dfs(root, Goal_State))
	if len(out) < 50:
		out_file.write("dfs" + out + "\n")
		a, b = tracemalloc.get_traced_memory()
		out_file.write( str((b-a) / 1000) + "KB" + "\n")


