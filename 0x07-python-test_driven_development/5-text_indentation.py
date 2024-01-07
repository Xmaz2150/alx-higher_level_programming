#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
   """
   - Inserts two new lines after each period (.), question mark (?), or colon (:).
   - Skips leading and extra spaces after these punctuation marks.
   - Preserves existing newline characters (\n).

   Args:
       text: The text to be formatted and printed.

   Raises:
       TypeError: If the input text is not a string.
   """

   if not isinstance(text, str):
       raise TypeError("text must be a string, not {}".format(type(text)))

   index = 0  # Keep track of the current position in the text

   while index < len(text):
       character = text[index]
       print(character, end="")

       if character in ".?:":  # Handle punctuation marks
           print("\n\n", end="")  # Add two new lines
           index += 1  # Move to the next character
           while index < len(text) and text[index] == " ":  # Skip spaces
               index += 1
           continue  # Skip to the next iteration

       elif character == "\n":  # Preserve existing newlines
           print()

       index += 1  # Move to the next character
