for s in "PYTHON":
    if s == "T":
        continue
    print(s, end="")
print()

for s in "PYTHON":
    if s == "T":
        break
    print(s, end="")
print()

for s in "BIT":
    for i in range(10):
        print(s, end="")
        if s == "I":
            break
