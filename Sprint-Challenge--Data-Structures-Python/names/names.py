import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# First improvement is simple syntax change
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)
# >>> runtime: 1.5658197402954102 seconds

# Second method of improvement
# Using a data structure from this week: Binary Search Tree
# Instantiate tree with arbitrary (middle of alphabet) root
bst = BinarySearchTree("main")
for name_1 in names_1:  # Loop through first list to grow tree
    bst.insert(name_1)

for name_2 in names_2:  # Loop through second list to search
    if bst.contains(name_2):
        duplicates.append(name_2)

# >>> runtime: 0.1584320068359375 seconds
# Complexity is O(n + n) = O(2n) = O(n) for BST
# as opposed to O(n * n) = O(n^2) for the nested loops

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Third / stretch improvement
# Using Python set intersection
# duplicates = list(set(names_1) & set(names_2))
# >>> runtime: 0.004755973815917969 seconds

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
