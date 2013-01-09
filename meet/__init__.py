#/usr/bin/env python

# Python script to scp keys and other config files to servers upon first run.

import paramiko, os, getpass, argparse


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
  parser =  argparse.ArgumentParser()
  parser.add_argument('server', help='Specify server(s) to add key', type=str, nargs='+')
  parser.add_argument('-u', "--username", help='Specify username to use', type=str)
  parser.add_argument('-i', "--identity", help='Specify identity file to use', type=str)
  args = parser.parse_args()
  hosts =  args.server

  if args.identity:
    key = args.identity
  else:
    key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()

  password = getpass.getpass()

  if args.username:
    username = args.username
  else:
    username = os.getlogin()

  for host in hosts:
    deploy_key(key, host, username, password)

if __name__ == '__main__':
  run()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 
