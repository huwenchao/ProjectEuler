# -*- coding: utf-8 –*-
__author__ = 'apple'

chain = {
	1: (1, 1),	# 1为访问的节点，元组第一个数为接下来的数，第二个数为深度
}
chain = {1:1}
def collatz_chain(n):
	if n not in chain:
		if n % 2 == 0:
			next = n/2
		else:
			next = 3*n + 1
		chain[n] = next
	return chain[n]

# for i in xrange(2, 30):
# 	max_dep = 1
# 	child, depth = collatz_chain(i)
# 	if depth > max_dep:
# 		max_dep = depth
# 		max_node = i

# print max_node, max_dep
#print sorted(chain.iteritems(),key=lambda d:d[1][1], reverse=True)
