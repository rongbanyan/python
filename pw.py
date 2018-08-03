# coding:utf-8
# pw.py -- An insecure password locker program.

import sys,pyperclip


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'
            }


if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print ('Password for %s copied to clipboard.' % (account))
else:
    print ('There is no account named %s' % (account))
