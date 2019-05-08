with open("old_file.txt","r+") as file:
    data=file.read()
add=""
qlist=[]
for i in range(len(data)):
    if data[i]=="Q" and data[i+2] ==')':
        qlist.append(add.strip())
        add=""
    add+=data[i]
qlist.append(add)

dic={}
for i in qlist:
    if "Q" in i:
        a=i.split(")")[0][1]
        dic[a]=i

new_file = open('new_file.txt','w')
new_file.write(qlist[0]+'\n')

keylist=dic.keys()
max1=int(max(keylist))
min1=int(min(keylist))
final=[]
for num in range(min1,max1+1):
    for i in keylist:
        if str(num) in i:
            print (dic[i])
            new_file.write(dic[i]+'\n')