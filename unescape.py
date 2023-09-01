import re

cfg_files = [
    "characters/characters",
    "levelpacks/holiday08/holiday08",
    "levelpacks/z__01contest/z__01contest",
    "levelpacks/z_spring/z_spring",
    "levels/stages",
    "levels/trophy"
]

def unescape(escape_chr: re.Match) -> str:
    return eval(f'"{escape_chr.group(0)}"')

for cfg in cfg_files:
    fin = open(cfg + "_escaped.cfg", "r", encoding="utf-8")
    fout = open(cfg + ".cfg", "w", encoding="utf-8")
    
    for line in fin.readlines():
        line = re.sub(r"//.*$", "", line).rstrip()
        if line == "": continue
        line = re.sub(r"\\u[0-9a-f]{4}", unescape, line, flags=re.IGNORECASE) + "\n"
        fout.write(line)
    
    fin.close()
    fout.close()
