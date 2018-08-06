import platform
import os

os = ""

if os.path.exists("/home/chronos/user"):
	os = "cros"
elif platform.system() == 'Darwin':
	os = "macos"
elif platform.system() == 'Linux':
	os = "linux"
else:
	print("Unsupported platform")
	exit(1)

subprocess.call("../build/build-" + os + ".sh", shell=True)