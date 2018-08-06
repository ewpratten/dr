import platform
import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

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

with cd("../build"):
	with open("../build/build-" + osn + ".sh", 'rb') as file:
	    script = file.read()
	rc = call(script, shell=True)

# os.chmod("../build/build-" + osn + ".sh", 0o755)
# subprocess.call("../build/build-" + osn + ".sh", shell=True)