#!/usr/bin/env python3
'''Lab 3 Part 2 script - free disk space'''
# Author ID: eroshy

import subprocess

def free_space():
    # Launch the command "df -h | grep '/$' | awk '{print $4}'" as a child process
    # Because of pipes, we will use shell=True
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    output, error = p.communicate()

    # Decode the output from bytes to string and strip newline characters
    return output.decode('utf-8').strip()


if __name__ == '__main__':
    print(free_space())
