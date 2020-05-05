
def reversed_number(number):
  to_string = str(number)
  number_string_stack = []
  for number in to_string:
    number_string_stack.append(number)

  reverse_string = ""

  while len(number_string_stack) > 0:
    reverse_string += number_string_stack.pop()

  return reverse_string


if __name__ == "__main__":
    print(reversed_number(2345))