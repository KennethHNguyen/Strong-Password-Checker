import re, pyperclip

regexDigit = re.compile(r'\d')
regexSpec = re.compile(r'\W')
regexLower = re.compile(r'[a-z]')
regexUpper = re.compile(r'[A-Z]')

def checkPassword(password):
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
    print('Wow, you\'ve got a hard and secure password! Very impressive ^O^')
else:
    print('Pathetic. Look up NIST SP 800-53 and then we can talk.')


