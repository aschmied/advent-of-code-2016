import decoder

def main():
  with open('input') as f:
    input = f.read().strip()

  decoded = decoder.Decoder(input).decode()
  print(len(decoded))

if __name__ == '__main__':
  main()
