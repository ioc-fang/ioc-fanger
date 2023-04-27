import re


test_str = 'hi there 153,252,251,252'

pattern = re.compile(r"\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\,|$)){4}\b")

matches = pattern.finditer(test_str)

for i in matches:
    print(i)