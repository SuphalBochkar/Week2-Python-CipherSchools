def name(first,last="asdasd",age=None):
    print(f'First name is {first}')                           #! Default value is taken only take if there is no input   
    print(f'Last name is {last}')                             #! if input is given it overwrites the default value
    print(f'Age name is {age}')                               #! Default is made only for last parameter
    
name("Suphal","Bochkar")