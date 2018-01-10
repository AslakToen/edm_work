storeFile = open(("C:/Users/ast/work/edm1/edmbuild/edmcore_build_2017.all.out"), "r")

outputfileDic = {}
summaries = ""
def num_in_line(line):
    for i in range(0, 30):
        temp = (str(i + 1) + ">-")
        if (temp in line) and (temp[0] == line[0]) and (temp[1] == line[1]):
            outputfileDic[i + 1] = [line]

for line in storeFile:
    num_in_line(line)

    if (" error ") in line:
        print(line)
        if(line[1] == ">"):
            outputfileDic[int(line[0:1])].append(line)
        else:
            outputfileDic[int(line[0:2])].append(line)

            if(line[0:2] == str(28)):
                print("printing 28")
                print(outputfileDic[int(line[0:2])])
    elif ("==========") in line:
        summaries += line


storeFile.close()

outputfile = repr(outputfileDic)
outputfile += summaries

output = open("output.txt", "a")

output.write(outputfile)

output.close()
