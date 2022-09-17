

import re

test_str = 'hi there 255,255,255,255'

pattern = re.compile(r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")

matches = pattern.finditer(test_str)

for match in matches:
    print(match)


