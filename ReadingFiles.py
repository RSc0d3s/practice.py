# create a separate file to read

#open("ReadingFilestext", "r") # reads file
#open("ReadingFilestext", "w") # write or edits  file
#open("ReadingFilestext", "a") # allows add new info
#open("ReadingFilestext", "r+") # allows read and write


employee_file = open("ReadingFilestext.py", "r")

for employee in employee_file.readlines():
    print(employee)

print(employee_file.readable()) #check if file can be read.

print(employee_file.read()) #reads everything

print(employee_file.readline()) #reads 1st line
print(employee_file.readline()) #reads 2nd line

print(employee_file.readlines()) #reads all and put in an array

print(employee_file.readlines()[1]) #index

employee_file.close()
