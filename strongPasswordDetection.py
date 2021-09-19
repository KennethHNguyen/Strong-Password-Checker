import re

regexDigit = re.compile(r'\d')      #A digit
regexSpec = re.compile(r'\W')       #A special character
regexLower = re.compile(r'[a-z]')   #A lowercase letter
regexUpper = re.compile(r'[A-Z]')   #A uppercase letter

def checkPassword(password):        #Function to run through the regexes and check for match
    if re.search(regexDigit, password) == None:
        return False
    elif re.search(regexSpec, password) == None:
        return False
    elif re.search(regexLower, password) == None:
        return False
    elif re.search(regexUpper, password) == None:
        return False
    elif len(password) < 8:
        return False
    else:
        return True

pw = input('Enter a password for me to check ;)\n')

if checkPassword(pw) == True:
    print('Wow, you\'ve got a strong password! Very impressive ^O^')
else:
    print('Pathetic. Look up NIST SP 800-53 and then we can talk.')


