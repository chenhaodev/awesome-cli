import subprocess
import os, sys

# execute the command using subprocess for uniq ID
cmd = "uuidgen"  
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()
output = output.decode("utf-8")
error = error.decode("utf-8")
id = output.split('-')[0]

# create folder using uniq ID
#topic_str = "".join(sys.argv[1:])
cmd = 'mkdir -p ~/Desktop/' + "".join(sys.argv[1:]) +'-'+id 
os.system(cmd)
print("".join(sys.argv[1:]) +'-'+id)
