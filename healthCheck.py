import subprocess

out = str(subprocess.check_output(['systemctl', '--host', 'aidan@192.168.1.31', 'status', 'MC-Emergency-Bot']))

mcBot = out.split("\n")

for x in mcBot:
    print(x)