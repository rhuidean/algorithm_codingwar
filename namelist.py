def namelist(names):
    length = len(names)

    if length == 0:
        return "''"
        
    elif length == 1:
        return "'"+names[0]['name']+"'"
    
    else:
    	string_list=[]
    	for object in names[:length-1]:
    		string_list.append(object['name'])
    	
        return "'" + ", ".join(string_list) + " & " + names[length-1]['name'] + "'"

print namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
print namelist([ {'name': 'Bart'}, {'name': 'Lisa'}])
print namelist([ {'name': 'Bart'}])
print namelist([])