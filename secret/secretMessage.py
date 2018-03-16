
import os # import some function for os / operating system /

def rename_files() : 
	#(1) get file names from a folder
	file_list = os.listdir(r"C:\Users\Auday\SomePython\secret\images") 
	#print file_list                             # to test file_list
                                                 # NOTE: The lines 9,10 Only to know the current working directory and we can deleted
	#saved_path = os.getcwd()            
	#print ("Current Working Directory is "+saved_path)
	
	os.chdir(r"C:\Users\Auday\SomePython\secret\images")
	#(2) for each file, rename filename
	for file_name in file_list :    # for every name file in the file list(array)
		print ("Old Name - "+file_name+ " || "), \
		#print old name and new name by delete the number of the old name
		("New Name - "+file_name.translate(None, "0123456789")), \
		# rename all the file by useing os.rename
   		os.rename(file_name, file_name.translate(None, "0123456789"))
	#os.chdir(saved_path)  # to be back to current working dir
rename_files() 