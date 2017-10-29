from fibonacci_series import FIBONACCI_SERIES
import unittest

class Fibonacci:

  def fibonacci_generator(n):
    if n < 1:
      raise ValueError("n must be at least 1")

    a, b = 0, 1
    yield a
    yield b
    while True:
      a, b = b, a + b
      yield b

  def fibonacci_print(n):
    if n < 1:
      raise ValueError("n must be at least 1")

    fib_gen = fibonacci_generator(n)
    i = 1
    while i <= n:
      next_fib = next(fib_gen, -1)
      if next_fib == -1:
        return
      print next_fib
      i += 1

  def fibonacci_to_list(n):
    if n < 1:
      raise ValueError("n must be at least 1")

    fib_gen = fibonacci_generator(n)
    fib_numbers = [None] * n

    i = 1
    while i <= n:
      next_fib = next(fib_gen, -1)
      if next_fib == -1:
        return
      fib_numbers[i-1] = next_fib
      i += 1
    return fib_numbers

  def validate_fib(generated_list, source_of_truth_list):
    for i in xrange(min(len(generated_list), len(source_of_truth_list))):
      if generated_list[i] != source_of_truth_list[i]:
        return False
    return True


class FibonacciTest(unittest.TestCase):
    def set_up(self):
      fib = Fibonacci()


    def tear_down(self):
      pass

    def should_error_on_zero(self):
      assertRaises(ValueError, fib.fibonacci_generator(0))
      assertRaises(ValueError, fib.fibonacci_print(0))
      assertRaises(ValueError, fib.fibonacci_to_list(0))

        

if __name__ == "__main__":
  unittest.main()


# fibonacci(0) # error
# fibonacci_print(1) # 0
# print "\n"
# fibonacci_print(2) # 0, 1
# print "\n"
# fibonacci_print(3) # 1, 1
# print "\n"
# fibonacci_print(10)# 0, 1, 1, 2, 3, ...
# print "\n"
# print fibonacci_to_list(0) # PASSED
# print "\n"
# print fibonacci_to_list(1)
# print "\n"
# print fibonacci_to_list(2)
# print "\n"
# print fibonacci_to_list(10)



# print validate_fib(fibonacci_to_list(3), FIBONACCI_SERIES) # True
# print validate_fib(fibonacci_to_list(10), FIBONACCI_SERIES) # True
# print validate_fib([1,9,4], FIBONACCI_SERIES) # False
# print validate_fib([0,0,1,1,2,3], FIBONACCI_SERIES) # False
# print validate_fib([1,0,1,1,2,3], FIBONACCI_SERIES) # False





