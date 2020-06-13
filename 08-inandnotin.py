filename = "nota_10.txt"
# filename = "code.exe"

if ".txt" in filename:
    print(filename)
elif ".txt" not in filename:
    print(f"{filename} goes in the trash")


options = "012345"

if "9" in filename:
    print("found it")
else:
    print("not found it")
