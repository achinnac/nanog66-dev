import re
SYSLOG = 'syslog.txt'

DATESTAMP_RE = r'(\d+\s+\w+\s+\d+)'
SPACE_RE = r'\s+'
TIMESTAMP_RE = r'(\d+:\d+:\d+)'
DEVICE_RE = r'(\S+)'
ERROR_CODE_RE = r'%(\S+):'
ERROR_MSG_RE = r'(.*)'

SYSLOG_RE = DATESTAMP_RE + SPACE_RE + TIMESTAMP_RE + SPACE_RE + \
            DEVICE_RE + SPACE_RE + ERROR_CODE_RE + SPACE_RE + ERROR_MSG_RE

## (\d+\s\w+\s\d+)\s+(\d+:\d+:\d+)\s+(\S+)\s+%(.*):\s+(.*)

with open(SYSLOG, 'r') as f:
    log_line = f.readlines()

    for line in log_line:
        #print line
        matched = re.match(SYSLOG_RE, line)
        #print matched
        if not matched:
           continue
        datestamp, timestamp, device, error_code, error_msg = matched.groups()
        if 'ETHPORT-5-IF_DOWN_INTERFACE_REMOVE' in error_code:
            print('Found a known error in {0} -- attempting remediation.'.format(device))

interface = re.match(r'.+(\d+)/\d+', error_msg)
module_name = interface.group(1)
command = ('show module {0}'.format(module_name))
print('--> Sent command {0}'.format(command))
#print('Executing..')

### Progress bar
import time
import sys

def do_task():
    time.sleep(1)

def example_1(n):
    for i in range(n):
        do_task()
        print '\b.',
        sys.stdout.flush()
    print ' Done!'

#print '--> Executing', example_1(10)

###
# import time
# import sys
#
# def do_task():
# 	time.sleep(1)
#
# def example_1(n):
# 	steps = n/10
# 	for i in range(n):
# 		do_task()
# 		if i%steps == 0:
# 			print '\b.',
# 			sys.stdout.flush()
# 	print ' Done!'
#
# print 'Starting ',
# sys.stdout.flush()
# example_1(100)

def progress_bar(n):
    import sys
    import time

    print 'Loading..... ',
    sys.stdout.flush()

    i = 0

    while i <= n:
    	if (i%4) == 0:
    		sys.stdout.write('\b/')
    	elif (i%4) == 1:
    		sys.stdout.write('\b-')
    	elif (i%4) == 2:
    		sys.stdout.write('\b\\')
    	elif (i%4) == 3:
    		sys.stdout.write('\b|')

    	sys.stdout.flush()
    	time.sleep(0.2)
    	i+=1

    print '\b\b done!'

progress_bar(10)
progress_bar(15)
progress_bar(22)
progress_bar(10)

