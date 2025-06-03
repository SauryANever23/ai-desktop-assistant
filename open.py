import sys
import os
import subprocess

def start(cmd):
    result = subprocess.run([f"{cmd}"], capture_output=True)
    print(result.stdout)

if __name__ == '__main__':
    start('ls')
