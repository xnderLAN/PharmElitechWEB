import os
path="./"
for r, d, f in os.walk(path):
  for file in  f:
    fullp = os.path.join(r,file)
   #print(fullp) 
    try:
      opned_f = open(fullp, 'r')
      if "ALLOWED_HOSTS" in opned_f.read():
        print(fullp)
      opned_f.close()
    except:
      pass
