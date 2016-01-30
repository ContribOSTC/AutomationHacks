# Open Source Technology Consortium
# this a basic classification script
# it helps to extract files of all type below a directory and collect 
# them into a separate directory
# Developed by: Adityan.J 
# Suggestions Welcome :)

import os
import subprocess

extension=raw_input('Enter data type extension:');

#checks for wrong extension 

if extension == '*':
	print 'Wrong extension , try again'
	exit()

#User Input for source directory
src=raw_input('Enter source directory to be scavenged:');

#Checks if source directory is valid
if os.path.isdir(src) == False:
	print 'Invalid path try again'
	exit()

#creates target directory with extension
targetPath=src+'Copy_'+extension;

if os.path.isdir(targetPath) == False:
	subprocess.call(['mkdir',targetPath]);

#searching for all subdirectories and making a list
directoriesList=[]
for root, dirs, files in os.walk(src):
	
	for directory in dirs:
		directoriesList.append(root+'/'+directory)
	directoriesList.append(root)

#moving everything to targetpath
for extract in directoriesList:
	currentPath=extract+'/*.'+extension;
	command='mv '+currentPath+' '+targetPath;
	os.system(command);	

print 'Files were copied successfully'
   
