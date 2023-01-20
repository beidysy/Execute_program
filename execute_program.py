#!/usr/bin/env python
import subprocess

# Write any windows or unix command to execute it!
command = 'echo "You have been Hacked!"'
subprocess.Popen(command, shell=True)
