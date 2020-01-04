import random
import string

def rand_password():
    stringLength = int (input("How long do you want your password to be:" ))
    """Generates a random series of lettersand numbers"""
    lettersandnumbers = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersandnumbers) for i in range(stringLength))

print ("Your Random Password is:  ", rand_password())
