import random
a = input("Password: ")
if len(a) > 5 or len(a) < 5:
 print("you can give only a password of 5 alphabet")
if len(a) == 5:
 i = a[0:2]
 x = i.upper()
 u = a[2:5]
 o = u.lower()
 k = x + "" + o
 s = "1234567890!@#$%^&*()?"
 passlen = 5
 p =  "".join(random.sample(s,passlen ))
 s = k + "" + p

 q = input("Password For: ")
 tyy = q + ":" + s 


 w = input("Want to see your password: ")
 if w == "Yes" or w == "yes":
  print(tyy)

 File = open("Passwords.exe", "a")
 File.write(f"{tyy}\n")

 File.close()
