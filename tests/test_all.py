import subprocess

def test_1():
    subprocess.check_call('python ./1.py',shell=True)

def test_2():
    subprocess.check_call('python ./2.py',shell=True)

def test_3():
    subprocess.check_call('python ./3.py',shell=True)

def test_a():
    subprocess.check_call('python ./a.py',shell=True)

def test_b():
    subprocess.check_call('python ./b.py',shell=True)

def test_nodag():
    subprocess.check_call('python ./nodag.py',shell=True)

def test_stdin():
    subprocess.check_call('python ./stdin.py',shell=True)

def test_timed3():
    subprocess.check_call('python ./timed3.py',shell=True)

def test_timed4():
    subprocess.check_call('python ./timed4.py',shell=True)
