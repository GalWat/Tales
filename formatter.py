import re
import os

raw_dir = r"src\raw"

for name in reversed(os.listdir(raw_dir)):
    filename, extension = os.path.splitext(name)
    if extension == ".md":
        path = os.path.join(raw_dir, name)
        with open(path, "r", encoding='utf-8') as inp, open("hihi.html", "a", encoding='utf-8') as outp:
            outp.write("<details> <summary>" + inp.readline()[:-1] + "</summary>\n\t<article>\n\t\t<p>")
            inp.readline()
            temp = re.sub(r"\n\n", "</p>\n\t\t<p>", inp.read()) + "\t</article>\n</details>\n\n"
            outp.write(re.sub("\t\t<p>\t</article>", "\t</article>", temp)) # Need to be simply
