import sys
from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from module.user import User

id_set =[User(ID='0927858281'),User(ID='0899623352'),User(ID='6307106733')]

def add_id(id):
    id_set.append(id)
    
def get_id():
    return id_set
    