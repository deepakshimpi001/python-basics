import os

#get the current directory
print("*************************")
print("the current directory before",os.getcwd())

#for creating the directory and folder

#os.mkdir('parentdir')

#os.mkdir('parentdir/childdir')

#if parent folder not created then we can't create the subfolder by using the this method os.mkdir() for that we use another method os.makedirs()


#os.makedirs("ds\df\gh\hj")

#print('******************************************')
#for changing the directory path write the below code
#os.chdir("ds\df")

#print("the current directory before:",os.getcwd())

#for rename the directory

os.rename('ds','deep_main')