def dec_to_bin(decimal, result=""):
  if decimal == 0:
    return result
  result = str(decimal % 2) + result
  return dec_to_bin(decimal//2, result)

def bin_to_dec(binary, result=0):
  if binary == "":
    return result
  result += int(binary[0]) * (2**(len(binary)-1))
  return bin_to_dec(binary[1:], result)

print(bin_to_dec(dec_to_bin(160000)))