import random
import string
def id_generation():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=10))

def nullState(idState):
    if(idState==None):
        return 3
    return idState