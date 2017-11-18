import decoder

def main():
  with open('input') as f:
    input = f.read().strip()

  decoded_by_v1 = decoder.get(1).decode(input)
  len_decoded_by_v1 = len(decoded_by_v1)
  len_decoded_by_v2 = decoder.get(2).len_decoded(input)
  
  print(len_decoded_by_v1)
  print(len_decoded_by_v2)

if __name__ == '__main__':
  main()
