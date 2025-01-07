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
     re.search(r"\w+@\w+\.\w+",emaildata) # re.search - find the first Match
     re.findall(r"\w+@\w+\.\w+",emaildata)  # re.findall - find the all matches/ findall will convert all matches into a list

     result = re.findall(r"(\w+)@(\w+)\.(\w+)",emaildata)
     result.group(1)

# --------------------------------------------

   # search ip address
    logfile = '192.168.0.1 [01/01/24 15:01:01] /index.html 200'
     re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+",logfile)
     re.search(r"\d+\.\d+\.\d+\.\d+", logfile)

# --------------------------------------------
