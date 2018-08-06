import platform
import os
# import subprocess
from subprocess import call

osn = ""

if os.path.exists("/home/chronos/user"):
	osn = "cros"
elif platform.system() == 'Darwin':
	osn = "macos"
elif platform.system() == 'Linux':
	osn = "linux"
else:
	print("Unsupported platform")
	exit(1)

with open("../build/build-" + osn + ".sh", 'rb') as file:
    script = file.read()
rc = call(script, shell=True)

# os.chmod("../build/build-" + osn + ".sh", 0o755)
# subprocess.call("../build/build-" + osn + ".sh", shell=True)