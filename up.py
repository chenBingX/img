

import os

cmd = "git add . && git commit -m \"update\" && git pull && git push"
print(cmd)
os.system(cmd)