#!/usr/bin/env python

from distutils.core import setup
import os
import shlex
import subprocess
import sys

startdir = os.getcwd()

if '--sourcedir' in sys.argv:
    index = sys.argv.index('--sourcedir')
    sys.argv.pop(index)
    sourcedir = sys.argv.pop(index)
    print "starting dir:", startdir
    os.chdir(sourcedir)
    print "present dir:", os.getcwd()


def get_version():
    inputcmd = 'git describe HEAD'
    fullcmd = shlex.split(inputcmd)
    cmnd = subprocess.Popen(fullcmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    (outstr, errstr) = cmnd.communicate()
    outstr, errstr = str(outstr).rstrip('\n'), str(errstr).rstrip('\n')
    vers = outstr.split('-', 1)[0]
    return vers

setup(name='pyradosutils',
      version=get_version(),
      description='Python RADOS Utilities',
      author='Bryan Apperson',
      author_email='bryan@bryanapperson.com',
      url='https://github.com/bryanapperson/python-rados-utils',
      package_dir={'pyradosutils': 'modules'},
      packages=['pyradosutils'])

os.chdir = (startdir)
