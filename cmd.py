import subprocess

# subprocess is a newer module which deprecates system.os

# subprocess.call(*popenargs, **kwargs) Run command with arguments. Wait for command to complete, then return the returncode (success or failure) attribute.

# If you create a Popen object, you must call the sp.wait() yourself.

# If you use call, that's done for you

# it will fail if you give it a pipe in the list, because ls thinks its first argument is the pipe operator
ls_output = subprocess.check_output(['ls', '-l'])
print ls_output # will print ls -l

output = subprocess.call('perl test.pl', shell=True) # will not return anything

subprocess.call('ls -a', shell=True)

#op = subprocess.check_output('ls -l') # not going to work because shell is not set as true, therefore it thinks the entire
									# string is a command.
#print op


# how to capture both output and error
# op = subprocess.check_output(['rm', 'dir2'], stderr=subprocess.STDOUT)
# print op

# op = subprocess.check_output('mv dir1 dir2', shell=True)
# print op

# check_output waits until it finishes running and returns the output to be captured on op1
op1 = subprocess.check_output(['ssh', 'web1', 'perl', 'test.pl'], stderr=subprocess.STDOUT)

# .call will execute the list, but will just return a success failures status. this is a blocking call, program will halt until
# the call returns (like check_output)
op2 = subprocess.call(['ssh', 'web1', 'perl', 'test.pl'], stderr=subprocess.STDOUT)

# same as .call, but the difference is that Popen is a non blocking call, meaning that it is like a background process
# if we would like to wait for the call to return, it our responsibility to call join on it
subprocess.Popen(['ssh', 'web1', 'perl', 'test.pl'], stderr=subprocess.STDOUT)

print op1