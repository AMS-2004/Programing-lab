step=5
#print upperpart pyramid
for i in range(1,step+1):
   for j in range(1,i+1):
      print("*",end="")
   print()
#print lowerpart pyramid
for i in range(step-1,0,-1):
   for j in range(1,i+1):
      print("*",end="")
   print()