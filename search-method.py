# create file in ipython3

  x = open("user.txt",'w')
  x = write("bob\njack\njohn\nmice\nslice\nwick")
  f.close()
  exit()
# --------------------------------------------

# searching data in file (In opeator) 

  f = open("user.txt")
  data = f.read()
  'jack' in data

 # Regular expression
     import re
     re.search("mice",data)
     re.search(r"[j,a]ck",data)
     re.search(r"[a-z]{2}",data)
     re.search(r"[a-z]+",data)

 # search email address
     re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-zA-Z]+",emaildata)    
     re.search(r"\w+@\w+\.\w+",emaildata)
     re.findall(r"\w+@\w+\.\w+",emaildata)

     result = re.findall(r"(\w+)@(\w+)\.(\w+)",emaildata)
     result.group(1)

# --------------------------------------------
