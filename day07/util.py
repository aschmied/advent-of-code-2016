def flatten(list_of_lists):
  return sum(list_of_lists, [])

def map_flatten(callable_returning_list, list):
  list_of_lists = map(callable_returning_list, list)
  return flatten(list_of_lists)
