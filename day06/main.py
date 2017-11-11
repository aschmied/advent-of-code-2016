from collections import Counter

def main():
  lines = read_input('input')
  transposed_lines = transpose(lines)

  part_one_decoded_text = ''
  part_two_decoded_text = ''

  for line in transposed_lines:
    h = byte_histogram(line)
    part_one_decoded_text += most_frequent_byte(h)
    part_two_decoded_text += least_frequent_byte(h)

  print(part_one_decoded_text)
  print(part_two_decoded_text)

def read_input(filename):
  with open(filename) as f:
    return [l.strip() for l in f.readlines()]

def transpose(list_of_strings):
  tuples = zip(*list_of_strings)
  return [''.join(t) for t in tuples]

def byte_histogram(string):
  return Counter(string)

def most_frequent_byte(byte_histogram):
  return byte_histogram.most_common(1)[0][0]

def least_frequent_byte(byte_histogram):
  return byte_histogram.most_common()[-1][0]

if __name__ == '__main__':
  main()
