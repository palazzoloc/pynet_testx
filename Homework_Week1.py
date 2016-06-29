''' Beginner Python - Homework #1
+ Notes to Don:
+ a) Found 'break' online.
+ b) Left my test handling in the code (try/except and "print" statements)
+ c) Have not figured out how to strip commas out of money without stealing code
'''

print '''
=====================================================================
+ Welcome to your retirement calculator!
+ Please provide some information for me to
+ help you calculate your retirement.
+
=====================================================================
'''

'''
Need user's input on Age, Retirement Age and Hourly Wage.
'''

while True:
    try:
        Current_Age = raw_input('First, please tell me old how you are right now?:')
        Current_Age = int(Current_Age)
        '''print type(Current_Age)'''
        break
    except ValueError:
        print ' Sorry, your current age should only contain numbers, not characters. Please try again.'
print 'Thank you!'

while True:
    try:
        Age_of_Retirement = raw_input('\nNow, at what age do you plan to retire?:')
        Age_of_Retirement = int(Age_of_Retirement)
        '''print type(Age_of_Retirement)'''
        break
    except ValueError:
        print ' Sorry, your age of retirement should only contain numbers, not characters. Please try again.'
print 'Thank you!'

while True:
    try:
        Job_Title = raw_input('\nOk, please provide your dream job title:')
        Job_Title = str(Job_Title)
        '''print type(Job_Title)'''
        break
    except NameError:
        print ' Sorry, your Job Title must not contain numbers, only characters. Please try again.'''
print 'Thanks!'

while True:
    try:
        Hourly_Wage = raw_input('\nNow, please provide your expected hourly wage in dollars and cents per hour (example 25.00):')
        Hourly_Wage = float(Hourly_Wage)
        '''print type(Hourly_Wage)'''
        break
    except ValueError:
        print ' Your Hourly Wage should only contain numbers and a decimal, not characters. Please try again.'
print 'Thank you!'

'''
Lets do the math here.
'''

Years_of_Work_Left = int(Age_of_Retirement - Current_Age)
Work_Week = 40
Weeks_in_a_Year = 52
Weekly_Wage = float(Hourly_Wage * Work_Week)
Yearly_Wage = float(Weekly_Wage * Weeks_in_a_Year)
Accumulated_Savings = float(Yearly_Wage * Years_of_Work_Left)
Retirement_Goal = input('\nAnd how much do you expect to to need at retirement? (example: 1,400,000):')
'''print type(Retirement_Goal)'''
Retirement_Goal_Number = float(Retirement_Goal)
Final_Retirement = int(Retirement_Goal_Number / Yearly_Wage)
if Final_Retirement % 2 == 0:
    print 'Final_Retirement is EVEN.'
else:
    print 'Final_Retirement is ODD.'

print 'You have %d more years to retire.' % Years_of_Work_Left
print 'You make $%d per week.' % Weekly_Wage
print 'You make $%d per year.' % Yearly_Wage
print 'I calculate it will take you about %d years to retire, if you save all your money! :-)' % Final_Retirement




