def count(sequence, item):
    total=0
    for n in sequence:
      if n==item:
          total=total+1
    return total



print count([8,1,2,3,8,8],8)
