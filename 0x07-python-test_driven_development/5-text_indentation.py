#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """
    - Inserts two new lines after each period (.),
    question mark (?), or colon (:).
    - Skips leading and extra spaces after these punctuation marks.
    - Preserves existing newline chars (\n).
    Args:
        text: The text to be formatted and printed.
    Raises:
    TypeError: If the input text is not a string.
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        i = 0
        while i < len(text):
            char = text[i]
            print(char, end="")
            if char in ".?:":
                print("\n\n", end="")
                i += 1  # Move to the next char
                while i < len(text) and text[i] == " ":
                    i += 1
                    continue
            elif char == "\n":
                print()
            i += 1
    except Exception as e:
        print(e)
