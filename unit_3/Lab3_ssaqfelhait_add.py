"""Lab 3 Add items
   Sammy saqfelhait 
    adding items to a camping list
    01/20/26 """    

from lab3_ssaqfelhait_list import camping_items

camping_items.append("hat")
camping_items.append("socks")
camping_items.append("matches")
camping_items.append("soap")
camping_items.append("towel")

camping_items.sort(reverse=True)
print("Reversed alphabetical list:")
print(camping_items)