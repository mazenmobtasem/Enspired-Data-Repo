# Room Analyzer
## Introduction
This script is designed to analyze a floor plan represented as a text file and identify rooms along with the count of specific objects (chairs, desks, etc.) within each room.

## Installation
This script requires Python 3 and the numpy library. You can install numpy using pip:

pip install numpy

## Usage
Prepare your floor plan in a text file (e.g., rooms.txt) where each character represents a part of the floor plan.
Run the script, providing the path to your floor plan file as an argument.

python Enspired.py rooms.txt

## How it works
The script reads the floor plan text file and parses it into a 2D list (matrix).
It uses Depth-First Search (DFS) flood fill algorithm to identify rooms and mark their indices in the matrix.
The script then counts the occurrences of specific objects (e.g., chairs, desks) within each room.
Finally, it outputs the total count of each object type and the count of objects within each room.

## Example
Consider the following floor plan:

+-----------+
|           |
| (closet)  |
|         P |
|         P |
|         P |                                    
|           |                             
+-----------+

Running the script would produce the following output:

total:
P: 3
Closet:
P: 3
This indicates that there are 3 Plastic Chairs (P) in total. Closet Room contains 3 plastic Chairs.

Note
Rooms are identified within parentheses (e.g., (Room_Name)).
Objects considered for counting include: W (Wooden), P (Plastic), S (Sofa), C (China Chair).
