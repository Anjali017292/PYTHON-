#program to read content of a text file
#to open a file for read operation 
filev =open ("second.txt","r")
#check file is open 
if(filev):
  #to read all the content line by line
  data = filev.read()
  #to check file is empty or not
  if(len(data)==0):
    print("file is empty")
''' else:
    while data:
      print(data,end='') 
      data=filev.readline()

#------------------------------------
#close the file'''
filev.close()

'''output
hitherehowareyougoodyesnorightwrong
'''
