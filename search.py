# .py file for search data from existing file 

import re
email_file = input("Enterr file path of email file for search opeartion :")

f = open(email_file,"r")
email_data = f.read()
f.close()

result = re.findall(r"\w+@\w+\.\w+",email_data)
print(result)

# redirect the output to another file

result_file= input("Enter the fileaname to redirect output in :")
f = open(result_file,"w")

for line in result:
  f.write(line+"/n")
f.close()

print("redirect file is created")
print(f"output file is {result_file}")
