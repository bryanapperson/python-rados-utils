#!/usr/bin/env python
from pyradosutils import common_utils

# Optionally you can pass in the keyring and ceph.conf
# locations as strings.
thiscluster = common_utils.Cluster()
# Replace these empty stings with your source and target pool names
source = ''
target = ''
thiscluster.copy_pool(source, target)
