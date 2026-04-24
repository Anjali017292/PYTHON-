#program to write 10 sentences given by user into a text file
#to open a file for write operation 
filev =open ("firstfile.txt","r")
#check file is open 
if(filev):
  #to read all the content
  data = filev.read()
  #to check file is empty or not
  if(len(data)==0):
    print("file is empty")
  else:
    print("Content of data")
    print(data) 

#------------------------------------
#close the file
filev.close()




'''output
Content of data
iamabotiamusedtogeneratethe
'''
