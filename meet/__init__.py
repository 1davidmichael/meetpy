#/usr/bin/env python

# Python script to scp keys and other config files to servers upon first run.

"""meet.

Usage:
  meet [ -v --username=NAME --identity-file=PATH ] (<server>...)

Options:
  -h --help                     Show this screen.
  -v --verbose                  Verbose output.
  -u --username=NAME            Define username.
  -i --identity-file=PATH       Define path to identity file.

"""

from docopt import docopt
import paramiko, os, getpass, sys

args = docopt(__doc__)

def deploy_key(key, server, username, password):
  client = paramiko.SSHClient()
  try:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=username, password=password)
  except:
    print 'Could not connect to %s' % host

  try:
    client.exec_command('mkdir -p ~/.ssh')
    client.exec_command('echo "%s" >> ~/.ssh/authorized_keys' % key)
    client.exec_command('echo "%s" >> ~/.ssh/authorized_keys2' % key)
    client.exec_command('chmod 600 ~/.ssh/authorized_keys*')
    client.exec_command('chmod 700 ~/.ssh/')
  except:
    print 'Creating folders or keys has failed'

def run():

  if args['--username']:
    username = args['--username']
  else:
    username = os.getlogin()

  if args['--identity-file']:
    key = args['--identity-file']
  else:
    key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()

  hosts =  args['<server>']

  password = getpass.getpass()

  for host in hosts:
    deploy_key(key, host, username, password)

if __name__ == '__main__':
  run()

# vim: tabstop=8 expandtab shiftwidth=2 softtabstop=2
