import re

_dot_re = re.compile(r"(?<=\w)\.(?=\w)")
_at_re = re.compile(r"(?<=\S)@(?=\S)")
