import re 
def validateEmail(email):
    mailformat = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(mailformat,email)):
        return True
    else:
        return False