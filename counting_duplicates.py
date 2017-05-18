def duplicate_count(text):
    ### retrieve distinct characters in the text
    str_list=list(text)
    distinctive_str_list=[]
    duplicate_str_list=[]
    
    for character in str_list:
        if character not in distinctive_str_list:
            distinctive_str_list.append(character)
            
    ### identify characters with more than 1 index in the list.
    for character in distinctive_str_list:
        if len([i for i, letter in enumerate(text) if letter == character])>1:
            duplicate_str_list.append(character)
    
    return len(duplicate_str_list)