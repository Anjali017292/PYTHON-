#program to write 10 sentences given by user into a text file
#to open a file for write operation 
filev =open ("firstfile.txt","w")
#------------------------------------
print("Enter any 10 sentence (hit enter key for new sentence): ")
for x in range(10):
  sentence = input()
  #writing the data into the file
  filev.write(sentence)
  print("------------------------------")
  print("----Next Sentence----")
print("Data written successfully into the file")
#close the file
filev.close()

'''output 
Enter any 10 sentence (hit enter key for new sentence): 
hello this is python
------------------------------
----Next Sentence----
i am a programming language
------------------------------
----Next Sentence----
i am easy to work on 
------------------------------
----Next Sentence----
my readibility is good
------------------------------
----Next Sentence----
i am list beginner friendly language
------------------------------
----Next Sentence----
i provide varioussequence datatypes like list , tuple,s
tring and dictionary
------------------------------
----Next Sentence----
i have two iteration construct for and while
------------------------------
----Next Sentence----
this is all about myself
------------------------------
----Next Sentence----
nice meeting you 
------------------------------
----Next Sentence----
hope we get along
------------------------------
----Next Sentence----
Data written successfully into the file



'''
