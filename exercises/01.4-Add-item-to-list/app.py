# Remember import random function here:
import random

my_list = [4, 5, 734, 43, 45]

# The magic is here:
  aux_list = []
   randonlength = random.randint(1, 100)

      for i in range(randonlength):
           aux_list.append(randonlength)
            i += i
    return aux_list
