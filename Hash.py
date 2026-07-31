
def hash_function(key, table_size ):
    hash_value = 0
    for char in key:
        hash_value += ord(char)  # Convert character to ASCII value
    return hash_value % table_size

# User input
key = input("Enter a key: ")
table_size = int(input("Enter hash table size: "))

# Calculate hash value
index = hash_function(key, table_size)

print("Hash value (index):", index)


# Output
Enter a key: DeVyAnI
Enter hash table size: 10
Hash value (index): 4

Write a Python program to create a Binary Tree using recursive insertion, where -1 represents a NULL node. Then perform and display the following tree traversals:

Preorder Traversal
Inorder Traversal
Postorder Traversal

Requirements:

Define a Node class with data, left, and right.
Implement a recursive insertNode() function to construct the binary tree.
Use -1 as the sentinel value to indicate no child node.
Implement separate functions for preorder(), inorder(), and postorder() traversals.
Display the traversal outputs after constructing the tree.
