# search ip address in User Entered log file and redirected to another file

import re
log_file = input("Enter the log line containing IP Data :")

f = open(log_file,"r")
log_data = f.read()
f.close()

print("Searching file for IP Addressses")
print ("..........................")

result_ips = re.findall(r"\d+\.\d+\.\d+\.\d+", log_data)

print_ask = input("Do you want to redirect the output? [y/n]")

if print.ask.lower()[0] == "y":
  result_file = input("Enter the file name for redirecting: ")
  f = open(result_file,"w")
  for line in result_ips:
    f.write(f"{line}\n")
  f.close()
  print(f"Output redirected successfully in {result_file}")
else: 
  pass
