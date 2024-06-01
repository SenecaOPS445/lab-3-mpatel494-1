#!/usr/bin/env python3
# Author ID: mpatel494, 175062215

import subprocess
p= subprocess.Popen(['df', '-h', '|', 'grep' "/$", '|', 'awk', "{print $4}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def free_space():
    output = p.communicate()
    print(output)
    print(output[0])
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())

