import os
import subprocess
import glob

os.chdir(os.path.dirname(__file__))
subprocess.run("cls", shell=True)

old = glob.glob("ETA-*.txt")
for f in old :
  os.remove(f)

for i in range(0,7) :
  subprocess.run("py getETA.py " + str(i), shell=True)

