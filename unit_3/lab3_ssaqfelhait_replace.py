""" lab 3 replace items
   Sammy saqfelhait
    replacing one item in with binoculars
    starter code from lab3_ssaqfelhait_add.py
    01/29/26 """
from lab3_ssaqfelhait_add import camping_items

camping_items[5] = "binoculars"

index = camping_items.index("binoculars")

print("Before binoculars:")
print(camping_items[:index])

print("Binoculars:")
print(camping_items[index])

print("After binoculars:")
print(camping_items[index + 1:])
