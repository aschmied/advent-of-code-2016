import ipv7

def main():
  with open('input') as f:
    lines = f.readlines()

  number_address_supporting_tls = 0
  for line in lines:
    address = ipv7.Address.parse(line.strip())
    if address.supports_tls():
      number_address_supporting_tls += 1

  print(number_address_supporting_tls)

if __name__ == '__main__':
  main()
