import numpy as np
# Define the file name
file_name = "rooms.txt"

# Read the floor plan text from the file
with open(file_name, "r") as file:
    floor_plan_text = file.read()

# Parsing the floor plan text into a 2D list (matrix)
matrix = []
for line in floor_plan_text.split("\n"):
    row = list(line)  # Convert the line into a list of characters
    matrix.append(row)
# Defining Matrix to Mark which Nodes have been visited (Faster with Numpy)
visited_matrix = np.zeros((len(matrix),len(matrix[0]))).tolist()

# Define the directions for DFS flood fill
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Function to perform DFS flood fill and mark rooms
def dfs_flood_fill(matrix, x, y, room, room_matrix):
    # If any of the following condition exit recursion
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] not in (" ","P","W","S","C","(",")"):
        return
    # Otherwise aka if you find any of these -> (" ","P","W","S","C","(",")")
    # Mark the node as visited, identify which room this is in the room matrix and move to the next step
    if visited_matrix[x][y] != 1:
        visited_matrix[x][y] = 1
        room_matrix[x][y] = room
        for dx, dy in directions:
            dfs_flood_fill(matrix, x + dx, y + dy, room, room_matrix)

# Initialize a matrix to store room indices with
room_matrix = [["" for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


rooms = {}
chairs = {}
# Find the rooms and mark their indices using DFS flood fill
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # Extract Room Names
        if matrix[i][j] == "(":
            room_name = ""
            x, y = i, j
            while y < len(matrix[i]) and matrix[x][y] != ")":
                room_name += matrix[x][y]
                y += 1
            room_name = room_name[1:] 
            chairs[room_name] = {}
            rooms[room_name] = (i, j)
            # Apply Flood Fill
            dfs_flood_fill(matrix, i, j, room_name, room_matrix)

#Sorting Rooms Names Ascendengly
sorted_dict_chairs = dict(sorted(chairs.items(), key=lambda x: x[0]))

# Get Totals
total = {"W":0,"P":0,"S":0,"C":0}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in ('W','S','C','P'):
            total[matrix[i][j]]+=1
            if matrix[i][j] not in chairs[room_matrix[i][j]].keys():
                chairs[room_matrix[i][j]][matrix[i][j]] = 1
            else:
                chairs[room_matrix[i][j]][matrix[i][j]] += 1
total_keys =list(total.keys())
print("total:")
for i in range(len(total)-1):
    print("{}: {}, ".format(total_keys[i],total[total_keys[i]]),end="")
print("{}: {} ".format(total_keys[-1],total[total_keys[-1]]))

# Print rooms with chairs
for i in sorted_dict_chairs:
    print("{}:".format(i.strip()))
    keys = list(sorted_dict_chairs[i].keys())
    for j in range(len(sorted_dict_chairs[i])-1):
        print("{}: {}, ".format(keys[j],sorted_dict_chairs[i][keys[j]]),end = '')
    print("{}: {}".format(keys[-1],sorted_dict_chairs[i][keys[-1]]))