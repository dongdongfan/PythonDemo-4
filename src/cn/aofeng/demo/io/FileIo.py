#coding:utf8

# 文件操作：读、写、追加
''' 
r          以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb        以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+        打开一个文件用于读写。文件指针将会放在文件的开头。
rb+     以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w         打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb       以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+       打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+    以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a          打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab       以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+       打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
 '''
 
fileName = "FileIoTest.txt"
 
# 写入文件
fo = open(fileName, "wb+")
fo.write("中文汉字写入测试\n")
fo.write("English Tet")
fo.close()

# 读取文件，没有指定模式，默认是读操作（r）
fo = open(fileName, "rb")
lineNum=1
while True:
    line = fo.readline()   # 读取的行内容携带换行符
    if 0 == len(line):
        break
    print "第%d行：%s" % (lineNum, line.strip("\n"))
    lineNum+=1
fo.close()
