string = ""
for line in open("a.txt","r"):
	string+=line
string=string[::-1]
with open("a2.txt","w")as f:
	f.write(string)

