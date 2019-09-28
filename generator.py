import os

raw_dir = r"src\raw"

outp = []

for file in reversed(os.listdir(raw_dir)):
    _, extension = os.path.splitext(file)
    if extension == ".md":
        path = os.path.join(raw_dir, file)
        with open(path, "r", encoding='utf-8') as inp_file:
            outp.append("<details> <summary>" + inp_file.readline()[:-1] + "</summary>\n")
            outp.append("\t<article>\n")
            for line in inp_file:
                if line != "\n":
                    outp.append(f"\t\t<p>{line[:-1]}</p>\n")
            outp.append("\t</article>\n")
            outp.append("</details>\n\n")

with open("generated.html", "w", encoding="utf-8") as outp_file:
    outp_file.write("".join(outp))
