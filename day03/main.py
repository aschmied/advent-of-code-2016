def main():
  with open('input') as f:
    matrix = parse_input(f.read())
  print count_triangles_in_horizontal_triples(matrix)
  print count_triangles_in_horizontal_triples(transpose(matrix))

def transpose(matrix):
  to_l = lambda t: list(t)
  return map(to_l, zip(*matrix))

def parse_input(input):
  out = []
  for line in input.strip().split('\n'):
    out.append(parse_line(line))
  return out

def parse_line(line):
  ints_as_strings = filter(None, line.strip().split(' '))
  return map(lambda s: int(s), ints_as_strings)

def count_triangles_in_horizontal_triples(matrix):
  number_triangles = 0
  for row in matrix:
    number_triangles += count_triangles_in_triples(row)
  return number_triangles

def count_triangles_in_triples(array):
  number_triangles = 0
  for start in xrange(0, len(array), 3):
    end = start + 3
    candidate_sides_lengths = array[start:end]
    if do_side_lengths_form_a_triangle(candidate_sides_lengths):
      number_triangles += 1
  return number_triangles

def do_side_lengths_form_a_triangle(sides):
  sides.sort()
  return sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
  main()
