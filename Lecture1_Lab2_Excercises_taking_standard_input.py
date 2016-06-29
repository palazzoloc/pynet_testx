''' Lab 2 - Taking Standard Input

demonstration of reading numbers from stdin
ask the user for age and year they were born, then output

- This version captures exceptions as well.
'''


age_input = raw_input('What is your age? ')
try:
    age = int(age_input)
    
except ValueError:
    print ' The age input is an INVALID integer.'
else:
    ''' print ' Yay, The age input is a valid integer.'''
    
    year_born_input = raw_input('What year were you born? ')
    try:
        year = int(year_born_input)
    except InvalidSyntax:
        print ' The year input is an INVALID integer.'
    else:
        print ' Yay, The year input is a valid integer.'
        print ' You are', age, 'and you were born in', year,'.'




