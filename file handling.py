##Method one

f_write = open("C:\\Codepy\\funny.txt", "w")
f_write.write("I Love My Family")
f_write = open("C:\\Codepy\\funny.txt", "a")
f_write.write("\nI Love Moni and Adhiran")
f_write = open("C:\\Codepy\\funny.txt", "a")
f_write.write("\nI Love Amma, Appa, Anna Family")

f_read = open("C:\\Codepy\\funny.txt", "r")
f_writeNew = open("C:\\Codepy\\funny_wc.txt", "w")
for line in f_read:
    lineCount = line.split(' ')
    f_writeNew.write("Wordcount:" + str(len(lineCount)) + ' ' + line)
    # print(len(lineCount))

f_write.close()
f_read.close()

#Method 2
with open("C:\\Codepy\\funny.txt", "r") as fopen:
    print(fopen.read())
#print(fopen.closed)  ##It will check if the file is closed or not using with keyword
