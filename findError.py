storeFile = open(("C:/Users/ast/work/edm1/edmbuild/edmcore_build_2017.all.out"), "r")


def num_in_line(line):
    for i in range(0, 30):
        if (str(i) + ">-") in line:
            return True


outputfile = ""

for line in storeFile:
    if (" error ") in line:
        outputfile += line
    elif ("==========") in line:
        outputfile += line
    elif(num_in_line(line)):
        outputfile += line

storeFile.close()

output = open("output.txt", "a")

output.write(outputfile)

output.close()
