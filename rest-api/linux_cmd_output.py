import subprocess

def lnx_output(cmd):

    output = subprocess.getoutput(cmd)
    return output.split("\n")
