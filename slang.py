import os



array_of_arrays = [[1]]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def get_input():
    number = input("Pick a number to be printed:")
    return int(number) 


def add_right(current, length):
    for i in range(current+1, current+length+1):
        array_of_arrays[-1].append(i)


def add_left(current, length):
    for i in range(current+1, current+length+1):
        array_of_arrays[0].insert(0,i)


def add_down(current, length):
    array_index = 1
    for i in range(current+1, current+length+1):
        if i == (current + length):  
            array_of_arrays.append([i])
        else:
            array_of_arrays[array_index].insert(0,i)           
            array_index += 1


def add_up(current, length):  
    array_index =  -2 
    for i in range(current+1, current+length+1):
        if i == (current + length):
            array_of_arrays.insert(0,[i])
        else:
            array_of_arrays[array_index].append(i)   
            array_index -= 1
                   

def fill_array_of_arrays(max_number):
    length = 1
    current = 1
    while current < max_number:
        if current + length <= max_number:
            add_right(current, length)
            current += length
        else:
            new_length = max_number - current
            add_right(current, new_length)   
            current += new_length         
        if current + length <= max_number:
            add_up(current, length)        
            current += length
        else:
            new_length = max_number - current
            add_up(current, new_length)      
            current += new_length                    
        length += 1
        if current + length <= max_number:
            add_left(current, length)
            current += length
        else:
            new_length = max_number - current
            add_left(current, new_length)    
            current += new_length                 
        if current + length <= max_number:
            add_down(current, length)
            current += length
        else:
            new_length = max_number - current
            add_down(current, new_length)       
            current += new_length              
        length += 1          


def get_array_width():
    width = 0
    for array in array_of_arrays:
        if len(array)>width:
            width = len(array)
    return width


def equalize_array():
    max_width = get_array_width()
    for array in array_of_arrays:
        size_difference = max_width - len(array)
        for i in range(1, size_difference):
            array.insert(0," ")


def print_array():
    #cls()
    for array in array_of_arrays:
        temp_string = ' '.join(map(str, array))
        print(temp_string)


def start():
    number = get_input()
    fill_array_of_arrays(number)
    equalize_array()
    print_array()



start()
