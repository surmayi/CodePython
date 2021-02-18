from stack import Stack

def convert_int_to_bin(dec_num):
  if dec_num==0:
    return 0
  s=Stack()
  while(dec_num>0):
    s.appendToStack(str(dec_num%2))
    dec_num = dec_num//2
  bin=''
  while s.peekStack():
    bin+=str(s.deleteFromStack())
  return bin

print(convert_int_to_bin(24))
print(convert_int_to_bin(5))