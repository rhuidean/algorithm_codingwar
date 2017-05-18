import numpy as np

def square_digits(num):
    ### convert to string letters
    num=str(num)
    
    ### split the string into characters and convert each to integer
    num=list(num)
    converted_list=[]
    for letter in num:
        converted_list.append(int(letter))
   

    ### square each number in the converted_list
    converted_list=np.array(converted_list)
    squared_list=np.square(converted_list)
    
    ### convert the number into letters and join
    squared_list=map(str,squared_list)
    number="".join(squared_list)
    number=int(number)
    
    return number
        
print square_digits(31)
