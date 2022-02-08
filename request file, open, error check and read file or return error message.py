fname = input("Enter the file name: \n")
print("\n")
try:
    filehand = open(fname)
    print("Congratulations, the file was found and will be opened.\n")
    filehandling = open("demotxt.py")
    for x in filehandling:
        print(x.upper())
    print("End of process, files read.")
except:
    print("Error: file can not be opened, file name:", fname, "\n")
    print("checks complete\n")
