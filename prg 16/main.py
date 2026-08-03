"""
Write programs for searching, splitting, and replacing strings based on pattern matching
using regular expressions
"""
import re


text = "Hello, this is MCA LAB record. Let's explore some regex patterns."
pattern = r"\b\w+o\w+\b"
match = re.search(pattern, text)
if match:
    print("Found match:", match.group())

parts = re.split(pattern, text)
print("Split parts:", parts)

new_text = re.sub(pattern, "***", text)
print("New text:", new_text)
