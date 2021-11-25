import os
import pickle
import hashlib
import hmac

def fun(name,password):
    s = {"username":name,"password":password}
    pickled_data = pickle.dumps(s)
    digest =  hmac.new('shared-key', pickled_data, hashlib.sha1).hexdigest()
    header = '%s' % (digest)
    data=header + ' ' + pickled_data
    with open("users.json","wb") as f:
        f.write(data)
    return data

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    yo_fun = fun(u,p)