print("Set Programs")
print()
for i in range(0,4):
	if (i==0):
		n=input("Want to find union of set : ")
		print()
		if (n=="yes"):
			print("UNION OS SET")
			print()
			s1={1,2,3,4,5,6,7,8,9,10}
			s2={2,4,6,8,12,28}
			c=s1.union(s2)
			print(c)
		else:
			continue
	print()
	if (i==1):
		n=input("Want to find intersection of set : ")
		print()
		if (n=="yes"):
			print("INTERSECTION OF SET")
			print()
			s1={1,2,3,4,5,6,7,8,9}
			s2={2,4,6,8}
			c=s1.intersection(s2)
			print(c)
		else:
			continue
	print()
	if(i==2):
		n=input("Want to find Eradicate the duplication in set : ")
		print()
		if (n=="yes"):
			print("DUPLICATING THE SET")
			print()
			s1={1,2,3,4,5,6,7,8,9,2,4,6,8,10,13,25,25,28}
			s2={1}
			for i in s1:
				if i in s2:
					continue
				else:
					s2.add(i)
			print(s2)
		else:
			continue
	print()
	if(i==3):
		n=input("Want to find superset : ")
		print()
		if (n=="yes"):
			print("SUPERSET OF SET")
			print()
			s1={1,2,3,4,5,6,7,8,9}
			s2={2,4,6,8}
			c=s1.issuperset(s2)
			print(c," Set-1 is superset of Set-2.")
			print()
			d=s2.issuperset(s1)
			print(d," Set-2 is not a superset of Set-1.")
		else:
			continue
