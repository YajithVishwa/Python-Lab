Paragraph=input("enter pargraph")
new=Paragraph.split()
for i in new:
	if(i.isdigit()):
		print(i)
	else:
		continue
