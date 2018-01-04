print ("Welcome to the comment spider! You can use this tool to get more information from Youtube videos.")
title = input("Please enter the title you want to search on Youtube: ")
print ("Please enter the keywords you want to search in the comments(At most five):")
#I will make it unlimited late. I need to do some research on dynamic memory in Python. Or using Stack/Queue library instead.
keywords = ["","","","",""]

for num in range(0,5):
	tempt = input()
	if tempt== "exit":#Maybe I should use regular expression for this.....
		break
	else:
		keywords[num-1]=tempt
		
print("Searching....")
print("Hey! Here is the stuff I found: ")
print("	I haven't finish yet. HEHE")