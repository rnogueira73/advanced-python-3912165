# Example file for Advanced Python by Joe Marini
import itertools

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]

# the enumerate function
# print(list(enumerate(days)))
# for i, d in enumerate(days):
#   print(i, d)

# use zip to combine sequences
# print(list(zip(days,daysFr)))
# for d in zip(days, daysFr):
#   print(d)

# use enumerate and zip together
# for i, d in enumerate(zip(days, daysFr)):
#   print(i, d[0], ' = ', d[1], 'in spanish')

# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"

result = itertools.zip_longest(seq1, seq2, seq3, fillvalue='-')

for i, d, x in result:
  print(i, d, x)

    