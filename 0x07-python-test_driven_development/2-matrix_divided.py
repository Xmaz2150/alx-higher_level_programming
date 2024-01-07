def matrix_divided(matrix, div):
  """
  Divides all elements of a matrix by a divisor.

  Args:
      matrix: A list of lists of numbers.
      div: The divisor.

  Raises:
      TypeError: If the matrix is not a list of lists or contains non-numbers.
      TypeError: If the rows of the matrix have different lengths.
      TypeError: If the divisor is not a number.
      ZeroDivisionError: If the divisor is zero.

  Returns:
      A new list of lists representing the result of the division.
  """

  if not isinstance(matrix, list) or not matrix:
    raise TypeError("matrix must be a non-empty list of lists")

  if not all(isinstance(row, list) for row in matrix):
    raise TypeError("matrix must contain only lists")

  if not all(len(row) == len(matrix[0]) for row in matrix):
    raise TypeError("All rows of the matrix must have the same length")

  if not isinstance(div, (int, float)):
    raise TypeError("div must be a number")

  if div == 0:
    raise ZeroDivisionError("division by zero")

  return [[round(element / div, 2) for element in row] for row in matrix]
