meun = {
    "chai" : 50,
    "pizza" : 100,
    "burger" : 80,
    "pasta" : 70,
}

print ("WELL COME TO CHAI CHAI  RESTAURANT")
print ("chai : 50\npizza : 100\nburger : 80\npasta : 70" )

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in meun:
    order_total += meun[item_1]
    print (f"your item {item_1} has been added to your order")
else:
    print (f"ordered item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order == "yes":
    item_2 = input("Enter the name of secound item = ")
    if item_2 in meun:
        order_total += meun[item_2]
        print (f"item {item_2} has been added to order")
    else:
        print (f"ordered item {item_1} is not avaialable yet!")

print (f"The total amount of  items to pay is {order_total} ")        


# menu = {"chai": 50, "pizza": 100, "burger": 80, "pasta": 70}

# print("WELCOME TO CHAI CHAI RESTAURANT")
# print("chai : 50\npizza : 100\nburger : 80\npasta : 70")

# order_total = 0

# item_1 = input("Enter the name of the item you want to order: ")
# if item_1 in menu:
#     order_total += menu[item_1]
#     print(f"Your item {item_1} has been added to your order")
# else:
#     print(f"The item {item_1} is not available yet!")

# another_order = input("Do you want to add another item? (Yes/No): ")
# if another_order == "Yes":
#     item_2 = input("Enter the name of the second item: ")
#     if item_2 in menu:
#         order_total += menu[item_2]
#         print(f"Item {item_2} has been added to your order")
#     else:
#         print(f"The item {item_2} is not available yet!")

# print(f"The total amount to pay is {order_total}")




