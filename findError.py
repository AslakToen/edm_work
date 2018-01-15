import sys

storeFile = open(sys.argv[1], "r")

outputfileDic = {}
summaries = ""

def line_cleanup(line):
    line = line.replace("\\", "/")
    line = line.replace("\n", "")
    return (line)

def num_in_line(line):
    for i in range(1, 31):
        key = (str(i) + ">-")
        if (key in line) and (key[0] == line[0]) and (key[1] == line[1]) and (not(i in outputfileDic.keys())):
            outputfileDic[i] = [line_cleanup(line)]

for line in storeFile:
    num_in_line(line)

    if (" error ") in line:
        if(line[1] == ">"):
            outputfileDic[int(line[0:1])].append(line_cleanup(line))
        else:
            outputfileDic[int(line[0:2])].append(line_cleanup(line))

    elif ("==========") in line:
        summaries += line

storeFile.close()

for i in range(1, len(outputfileDic)):
    if (len(outputfileDic[i]) < 2):
        del outputfileDic[i]
outputfile = summaries
outputfile += repr(outputfileDic)
outputfile = outputfile.replace("],", "],\n")
outputfile = outputfile.replace(', "' , '\n    "')
outputfile = outputfile.replace("{", "")
outputfile = outputfile.replace("}", "\n")


output = open(sys.argv[2], "a")

output.write(outputfile)

output.close()
