#binary numbers
one = 0b1
two = 0b10
three = 0b11
four =0b100
five =0b101
six =0b110
seven =0b111
eight =0b1000
nine =0b1001
ten =0b1010
eleven =0b1011
twelve =0b1100

#printing binary of a number of base 10
print bin(5)
#printing base 10 equivalent --reverse process
print int("111",2)
print int("0b100",2)

shift_right = 0b1100
shift_left = 0b1


shift_right =shift_right>>2
shift_left =shift_left<<2
print bin(shift_right)
#0b11
print bin(shift_left)
#0b100

#bitwise and
print bin(0b1110&0b101)
#result ob100

#bitwise or
print bin(0b1110|0b101)
#prints 0b1111

#bitwise XOR (one of inputs are 1 but not both at the sametime)

print bin(0b1110 ^ 0b101)
#prints 0b1011 

#check 4th bit on (right to left)
def check_bit4(input):
  mask = 0b1000
  num=input&mask
  if num>0:
    return "on"
  else:
    return "off"

a = 0b10111011
bitmask=0b100
print bin(a|bitmask)
#prints 0b10111111

#fliping bits with XOR
a = 0b11101110
mask=0b11111111
#flip bits using XOR
print bin(a^mask)
#prints 0b10001

#define a function that flips a n bit from a number

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)

