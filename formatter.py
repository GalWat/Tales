import re

raw = input()

output = re.sub(r"</p><p>", "<br>", raw)

print(output)