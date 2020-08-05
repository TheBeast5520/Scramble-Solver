from itertools import permutations

word = input("Please enter the scrambled word: ")

fin = open("wordlist.txt","r")
finLines = fin.readlines()
finLines = [i.strip() for i in finLines]

##def fac(n):
##    if n==1:
##        return n
##    else:
##        return n*fac(n-1)

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

for i in permutations(word, len(word)):
    i="".join(i)
    if binary_search(finLines, i):
        print(i)

