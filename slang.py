import os
import time


array_of_arrays = [[1]]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def get_input():
    number = input("Pick a number to be printed:")
    return int(number) 


def add_right(current, length):
    for i in range(current+1, current+length+1):
        print("right ", i)
        array_of_arrays[-1].append(i)


def add_left(current, length):
    for i in range(current+1, current+length+1):
        print("left ", i)
        array_of_arrays[0].insert(0,i)


def add_down(current, length):
    print("current: ", current, " length ", length)
    for array, i in zip(array_of_arrays[1:], range(current+1, current+length+1)):
        print("down ", i)
        if i == (current + length):
            print("voeg array toe onderin")       
            array_of_arrays.append([i])
        else:
            array.insert(0,i)           


def add_up(current, length):
    print("current: ", current, " length ", length)  
    for array, i in zip(array_of_arrays[:-1:-1], range(current+1, current+length+1)):
        print("up ", i)
        if i == (current + length):
            print("voeg array toe bovenin") 
            array_of_arrays.insert(0,[i])
        else:
            array.append(i)   
                   

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


def print_array():
    #cls()
    for array in array_of_arrays:
        temp_string = ' '.join(map(str, array))
        print(temp_string)


def start():
    number = get_input()
    fill_array_of_arrays(number)
    time.sleep(5)
    print_array()



start()
