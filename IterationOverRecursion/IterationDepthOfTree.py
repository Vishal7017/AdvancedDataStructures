#!/usr/bin/env python3


def depth(tree):
	result = 0
	queue = [tree]
	while queue:
		level_count = len(queue)
		for child_count in range(0, level_count):
			child = queue.pop()
			if child["left_child"]:
				queue.append(child["left_child"])
			if child["right_child"]:
				queue.append(child["right_child"])
		result += 1
	return result



def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 



 
print(depth(tree_level_1))
# 2
print(depth(tree_level_2))
# 4





