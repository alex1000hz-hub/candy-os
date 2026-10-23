# este comando es para cambiar el etorno
import sys
import subprocess
import json as js

args = sys.argv[1:]
lenguaje = args[0]
subprocess.run([lenguaje, args[1]])
