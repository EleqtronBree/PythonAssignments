"""
Calculates the Surface Area and Volume of a Dodecahedron

Author: Electra Bree
Username: rbre269
User ID: 574069100
"""

import math

lots_of_hashtags = "#" * 34
lots_of_spaces = " " * 7

print(lots_of_hashtags)
print(lots_of_spaces, "Regular Dodecahedron", lots_of_spaces, sep = "")
print("Surface Area and Volume Calculator")
print(lots_of_hashtags)
print()

edge_length = int(input("Edge Length: ")) #Change the value of edge_length here
surface_area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * edge_length ** 2
volume = (15 + 7 * math.sqrt(5)) / 4 * edge_length ** 3
rounded_surface_area = round(surface_area, 3)
rounded_volume = round(volume, 3)

print()
print("Surface area:", rounded_surface_area)
print("Volume:", rounded_volume)
