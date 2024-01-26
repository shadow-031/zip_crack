import zipfile

def crack_pass(passlist, obj):
    #tracking no. of line
    idx = 0
    #open file in read byte mode as "rockyou.txt"
    #file contains some special chracter and hence unicodedecodeerror will be generated
    with open(passlist, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd = word)
                    print("password found at line", idx)
                    print("password is", word.decode())
                    return 1
                except:
                    continue
    return 0
passlist = "/home/ghost/passwrd/rockyou.txt"
zip_file = input(("path of file: "))
#zipfile object initialised
obj = zipfile.ZipFile(zip_file)

#count no. of passwrd present in file
cnt = len(list(open(passlist, 'rb')))
print("there are total", cnt, "number of passwords")

if crack_pass(passlist, obj) == 0:
    print("password not found in the file") 