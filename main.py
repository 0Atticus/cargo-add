from genericpath import isdir, isfile
import os
import sys

target = str(sys.argv[1])
print(target)
file = ""
path = "/home/atticus/cargo_add/crates.io-index"
count = 2

add_to = sys.argv[2]

while True:

    if not isfile(path):
        for i in os.listdir(path):
            if i == target and isfile(path + f"/{i}"):
                path += f"/{i}"
                break
        
            elif target[count - 2:count] in i and not isfile(path + f"/{i}"):
                path += f"/{i}"
        count += 2
    else:
        break

print(path)

with open(path, "r") as r:
    
    best = ""
    count = 1

    while best == "" or best == " ":
        best = r.read().split()[0 - count]
        count += 1


    best = best.split("vers\":\"")[1].split("\"")[0]
print(best)

with open(add_to, "r") as r:
    content = r.read()
    content += "[dependencies]" if "[dependencies]" not in content else ""
    new = content.split("[dependencies]")[0] + f"[dependencies]\n{target} = \"{best}\"" + content.split("[dependencies]")[1]

with open(add_to, "w") as f:
    f.write(new)
os.system(f"cd {add_to.split('Cargo')[0]} && cargo build")