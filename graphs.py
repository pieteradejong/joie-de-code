from collections import deque

graph = {
	"1": ["2", "5"], 
	"2": ["1", "3", "5"], 
	"3": ["2", "4"], 
	"4": ["3", "5", "6"], 
	"5": ["1", "2", "4"], 
	"6": ["4"], 
}

graph2 = [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0]
]


def traverse_bfs(graph, root, target):
	viz = set()
	queue = deque([root])

	while queue:
		curr = queue.pop()
		if curr not in viz:
			visit(curr)
			viz.add(curr)
		if curr == target:
			return curr
		
		for node in graph[curr]:
			if node not in viz:
				queue.appendleft(node)


def visit(node):
	print "visit: ", node


def traverse_dfs(graph, root, target):
	viz = set()
	stack = [root]

	while stack:
		curr = stack.pop()

		if curr not in viz:
			visit(curr)
			viz.add(curr)

		for nb in graph[curr]:
			if nb not in viz:
				stack.append(nb)



if __name__ == "__main__":
	print "Breadth First Search"

	print "1 -> 5", traverse_bfs(graph, "1", "5")
	print "\n\n"
	print "1 -> 4", traverse_bfs(graph, "1", "4")
	print "\n\n"
	print "1 -> 3", traverse_bfs(graph, "1", "3")
	
	print "Depth First Search"

	print "1 -> 5", traverse_dfs(graph, "1", "5")
	print "\n\n"
	print "1 -> 4", traverse_dfs(graph, "1", "4")
	print "\n\n"
	print "1 -> 3", traverse_dfs(graph, "1", "3")
	print "\n\n"
	


