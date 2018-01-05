"""

8. Your task in this exercise is as follows:

Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
"""
import random
def generatebrack(n):
  """
  Solution for exercise 8
  This will generate a equal number of open and closed brackets
  author: S. Sousa
  """  
  brackets = '['*n + ']'*n
  brackets_test = ''
  sample_ind = random.sample(range(2*n),2*n)
  for ind in sample_ind:
    brackets_test += brackets[ind]
  print ("Brackets to test: ", brackets_test)

  test_count = 0
  for char in brackets_test:
    if char=='[':
      test_count += 1
    else:
      test_count -= 1
    if test_count < 0:
      print (brackets_test, "    NOT OK")
      return      
#  if test_count == 0:
  print (brackets_test, "     OK")
#  else:
#    print brackets_test, "     NOT OK"

generatebrack(4)
