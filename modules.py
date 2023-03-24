from string import*
from random import*
def generate_id():
    numbers = []
    length = int(input("how long do you want your id? "))
    amount = int(input("how many id's do you want "))
    content = ascii_letters + digits
    while len(numbers) < amount:
        joined = "".join(choices(content, k=length))
        numbers.append(joined)
    return("\n".join(numbers))
print(generate_id())
#gets random rgb colour
def rgb_color_gen():
    rgb_list = []
    while len(rgb_list) < 3:
        rgb_list.append(randint(0,255))
    return(f"rgb: {rgb_list}")
print(rgb_color_gen())
#get n numbers of hexa colours
def list_hexa_colours(n):
    lst = []
    content = ascii_letters + digits
    while len(lst) < n:
        shuffled = "#" + "".join(choices(content, k = 6))
        lst.append(shuffled)
        
    return(lst)
print(list_hexa_colours(5))
#gets n numbers of rgb colours
def list_rgb_colours(n):
    lst = []
    while len(lst) < n:
        lst.append(rgb_color_gen())
        
    return(lst)
print(list_rgb_colours(3))
#level 2 number 3
def generate_colours(item, n):
    if item == "hexa":
        return list_hexa_colours(n)
    elif item == "rgb":
        return list_rgb_colours(n)
print(generate_colours("rgb" ,2))
def shuffle_list(lst):
    shufulled = lst[:]
    shuffle(shufulled)
    return shufulled
my_shuffled = [1,2,3,45,6]
print(shuffle_list(my_shuffled))
def array_unique_numbers():
    lst_of_array = []
    while len(lst_of_array) < 7:
        num = randint(0,9)
        #checks if number already in list, if not it adds
        if num not in lst_of_array:
            lst_of_array.append(num)
    return lst_of_array
print(array_unique_numbers())


    

