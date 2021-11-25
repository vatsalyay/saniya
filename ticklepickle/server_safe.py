import os
import pickle
import hashlib
import hmac


def reverse_fun():
      with open("users.json","rb") as f:
          data = f.read()
      try:
            recvd_digest, pickled_data = data.split(' ')
            new_digest = hmac.new('shared-key', pickled_data, hashlib.sha1).hexdigest()
            if recvd_digest != new_digest:
                  print 'Integrity check failed'
            else:
                  unpickled_data = pickle.loads(pickled_data)
            return unpickled_data
      except:
            return 'Data not in format'

if __name__ == '__main__':
      print(reverse_fun())