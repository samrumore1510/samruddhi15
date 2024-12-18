#WAP to find second smallest element in the list
l2=[89,64,65,2,6,5]
#remove duplicate
remove_dup=(list(set(l2)))
#final list
s_list=sorted(remove_dup)
print(l2)
#giving index to find largest number
print("the seconed largest number is",s_list[-2])
