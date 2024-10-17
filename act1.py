def count_digits(number):
  """Counts the number of digits in a given number.

  Args:
    number: The number to count digits in.

  Returns:
    The number of digits in the given number.
  """

  count = 0
  while number > 0:
    number //= 10
    count += 1
  return count

number = int(input("Enter a number: "))
digits = count_digits(number)
print("The number of digits in", number, "is", digits)