storeFile = open(("C:/Users/ast/work/edm1/edmbuild/edmcore_build_2017.all.out"), "r")

outputfileDic = {}
summaries = ""
def num_in_line(line):
    for i in range(1, 31):
        temp = (str(i) + ">-")
        if (temp in line) and (temp[0] == line[0]) and (temp[1] == line[1]) and (not(i in outputfileDic.keys())):
            outputfileDic[i] = [line]

for line in storeFile:
    num_in_line(line)

    if (" error ") in line:
        if(line[1] == ">"):
            outputfileDic[int(line[0:1])].append(line)
        else:
            outputfileDic[int(line[0:2])].append(line)

    elif ("==========") in line:
        summaries += line

storeFile.close()

outputfile = repr(outputfileDic)
outputfile += summaries

output = open("output.txt", "a")

output.write(outputfile)

output.close()
