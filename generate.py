#encoding: utf-8
import os
fdirPath = "categories"
categories = ["general", "game"]
res = ""
for cat in categories:
    dirPath = fdirPath + "/" + cat
    files = os.listdir(dirPath)
    for file in files:
        if file.endswith(".txt"):
            with open(dirPath + "/" + file, "r", encoding='utf-8') as f:
                content = f.read()
                f.close()
            append = "%s\n" % (content)
            res += append

with open("cave.txt", "w", encoding='utf-8') as outFile:
    outFile.write(res)
    outFile.close()
print(len(res))
