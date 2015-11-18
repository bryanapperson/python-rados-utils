# python-rados-utils
Python RADOS utilities for performing operations on a RADOS/ceph cluster.

## Operating Systems

* CentOS 7
* RHEL 7
* Fedora 22

## Installing python-rados-utils

It's pretty easy to get up and running.

### Building from source

* Clone the git repository `git clone git@github.com:bryanapperson/python-rados-utils.git`

* `cd python-rados-utils`

* `rpmbuild -ba python-rados-utils.spec`

### Installing

* The rpm will be output in ~/rpmbuild/RPMS/noarch/.

* Install the rpm using: `rpm -Uvh python-rados-utils.rpm`

## Using python-rados-utils

* Importing the modules can be done by using statements like:

* `from pyradosutils import common_utils`
