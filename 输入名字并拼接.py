def get_formatted_name(first_name,last_name):
    full_name=first_name+''+last_name
    print(type(full_name))
    print(type(full_name.title))
    return full_name.title

while True:
    print('please enter your name:')
    print('( enter q at any time to quit)')
    
    f_name=input('first_name:')
    if  f_name=='q':
    	print('over')
        break
        
    l_name=input('last_name:')
    if  l_name=='q':
    	print('over')
        break
        
    formatted_name=get_formatted_name(f_name, l_name)
    print(type(formatted_name))
    print('hello',formatted_name.title,'!')