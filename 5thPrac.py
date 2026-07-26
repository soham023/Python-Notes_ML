
data = True
cnt = 0
flag = False
with open("sam2.txt", "r") as f:
    while data:
        data = f.readline()
        cnt += 1
        if("python" in data):
            print("word found")
            flag = True
            break

if flag == False:
    print ("No word")
else :
    print(f"found in line {cnt}" )

