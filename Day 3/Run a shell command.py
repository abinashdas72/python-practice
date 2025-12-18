 import subprocess
 subprocess.run(
     ["df", "-h"],
 capture_output = True,
 text = True
 )
