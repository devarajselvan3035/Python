import re

file_path = "/home/devselvan/Documents/Python/LLM/the-verdict.txt"
with open(file_path, "r", encoding="utf-8") as file:
    rawText = file.read()


# Split the text with punctualtion and spaces
splitRewText = re.split(r"([,.:;?_!\"()']|--|\s)", rawText)

"""
Removing whitespaces reduces the memory and computing requirements. However, keeping whitespaces can be useful if we train models that are sensitive to the exact structure of the text (For example, Python code, which is sensitive to the indentation and spacing).
"""

# Remove spaces from each splited strings "hello " to "hello"
splitRewText = [item.strip() for item in splitRewText if item.strip()]

print("." in splitRewText)
print(len(splitRewText))
