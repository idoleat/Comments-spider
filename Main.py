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
		
print("Searching....")#I can add something interesting here to make the program juicy. Maybe a joke.
print("Hey! Here is the stuff I found: ")
print("	I haven't finish yet. HEHE")
ShareIt = input("Do you want to share it on Twitter?(N/Y)")
#Maybe I will change it to Facebook if output is too long.
#The probability I will change to Facebook is 0.7
if ShareIt=='Y':
	print("successfully shared!")
	print("Thanks for using this tool!")
	print("You can find the source code on https://github.com/idoleat/Comments-spider")
else:
	print("Thanks for using this tool!")
	print("You can find the source code on https://github.com/idoleat/Comments-spider")