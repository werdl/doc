import sys
import inspect

from runpy import run_path
settings = run_path(sys.argv[1])

FILE=f'{sys.argv[1].split("/")[-1].split(".")[0]}.md'
def strip_lines(source: str) -> str:
    toret=""
    c=0
    for line in source.split("`")[0].split("\n"):
        toret+=line.strip()
        if c%2==0:
            toret+="\n"
        c+=1
    return toret
def args(source: str):
    toret=""
    try:
        source.split("`",1)[1]
    except IndexError:
        return "This function has no arguments."
    for line in ("`"+(source.split("`",1)[1])).split("\n"):
        toret+=line
    return toret
def grab_def(string: str) -> int:
    c=0
    for line in string.split("\n"):
        if "def " in line:
            return string.split("\n")[c].strip()
        c+=1
with open(FILE,"w") as file:
    file.write("")
def flush(string, fname):
    with open(fname,"a") as file:
        file.write(string)

global_symbols = settings
classes = [symbol for symbol in global_symbols.values() if inspect.isclass(symbol)]
for obj in classes:
    members = inspect.getmembers(obj, predicate=inspect.isfunction)
    flush(f"""
---

## `{obj.__name__}`
{strip_lines(obj.__doc__)}

---""",FILE)
    for method in members:
        m=method[1]
        source=inspect.getsource(m)
        flush(f"""
### `{obj.__name__}.{grab_def(source)[4:]}`
#### Description
{strip_lines(m.__doc__)}
#### Arguments:
{args(m.__doc__)}

---""",FILE)