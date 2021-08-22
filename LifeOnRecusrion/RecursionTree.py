 # Define build_bst() below...
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  middle_idx = my_list(len(my_list)/2)
  

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "???"
