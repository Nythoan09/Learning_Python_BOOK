# Learning How to Use Lists
"""
cars = ['audi', 'BMW', 'toyota', 'chevrolet']
print(cars)
print(cars[0])
print(cars[0].title())
print(cars[1])
print(cars[3])
print(cars[1].lower())
print(cars[-2])
"""

## Using Individual Values from a List
"""
message = f"I want to buy a {cars [-3].lower()}"
print(message)
"""

## Modifying Elements in a list
"""
smartphones = ["Iphone","Xiaomi","OnePlus","googlepixel"]
smartphones [0] = "HTC"
print (smartphones)

smartphones.append("Iphone")
print(smartphones)
"""

## Appending items to lists
"""
brand_list = []
brand_list.append ("Nike")
brand_list.append ("Adida")
brand_list.append ("Jordan")

print(brand_list)

# Inserting items into lists

brand_list.insert(2, "Zara")
print(brand_list)

# Removing items using the del Statement

brand_list
del brand_list[3]
print(brand_list)
"""
# Removing items using the pop() method
"""
new_brands = ["nexus","Kenick", "Bensons", "Paniack"]
print(new_brands)

# new_service = new_brands.pop()
# print (new_brands)
# print (new_service)

service_recived = new_brands.pop(2)
print (new_brands)
print (f"The last service I recived was from {service_recived.upper()} company.")

new_brands.remove("Kenick")
print(new_brands)

paniack = "Paniack"
new_brands.remove(paniack)
print(new_brands)
print (f"\nNo me interesan los servicios de {paniack.upper()} por ahora")
"""

# Organizing a List

## Sorting Lists with the sort() Method:
"""
car_brands = ["bmw", "audi","chevrolet","toyota","hyundai"]
carbrands_order = car_brands.sort(reverse=True)
print (car_brands)
print (carbrands_order)
"""

## Sorting with sorted() funtion:
"""
car_brands = ["bmw", "audi","chevrolet","toyota","hyundai"]

print ("The following one is the original list:")
print (car_brands)

print ("\nAnd This another one is the sorted list")
print (sorted(car_brands))

print ("\nAnd This last one is the original list again")
print (car_brands)

# sort() with reverse=True

car_brands = ["bmw", "audi","chevrolet","toyota","hyundai"]
print("\n\tWITH reverse=True")

print ("\nThe following one is the original list:")
print (car_brands)

car_brands.sort(reverse=True)
print ("\nAnd This another one is the sorted list")
print (car_brands)

print ("\nAnd This last one is the original list again")
print (car_brands)
"""

## Finding the length of lists
"""
car_brands = ["bmw", "audi","chevrolet","toyota","hyundai"]
print(f"Es {len(car_brands)} la cantidad de marcas de automviles que tenemos registradas actualmente")

"""

# Using 'for' loop in lists
"""
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"\n{magician.upper()}, that was a great trick, I am in shock")


magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"\nOMG {magician.title()}, that was a great trick, I am in shock")
    print(f"I look forwoard to seeing the next one soon")
"""

# Using 'range' funtion:

# for num in range(1,10):
#     print(num)

# Using 'range' to make lists:

num = list(range(0,20))
print(num)



