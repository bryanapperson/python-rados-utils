#!/usr/bin/env python
'''Utilities for RADOS in python.

Common utilities for RADOS clusters written in python.
'''

import rados


class Cluster(object):
    '''A wrapper object for utilities around the rados.Rados object

    Contains utility functions around a rados.Rados object.
    '''

    def __init__(self, clustkeyring='/etc/ceph/ceph.client.admin.keyring',
                 clustconfig='/etc/ceph/ceph.conf'):
        '''Initializes the Cluster object

        Initializes the Cluster object using a ceph keyring and ceph.conf
        as input.
        '''
        self.clustkeyring = clustkeyring
        self.clustconfig = clustconfig
        self.cluster = rados.Rados(conffile=clustconfig,
                                   conf=dict(keyring=clustkeyring))
        # Open connection to cluster
        self.cluster.connect()

    def print_info(self):
        '''Prints information to the user  about the cluster

        Prints information about the rados cluster to the user.
        '''
        print ("\nlibrados version: " + str(self.cluster.version()))
        print ("Will attempt to connect to: " +
               str(self.cluster.conf_get('mon initial members')))
        print ("\nCluster ID: " + self.cluster.get_fsid())
        print ("\n\nCluster Statistics")
        print ("==================")
        cluster_stats = self.cluster.get_cluster_stats()
        for key, value in cluster_stats.iteritems():
            print (key, value)

    def get_obj_list(self, pool):
        '''Returns a list of all_objects in a given pool

        Returns a list of all objects in a given pool.
        '''
        iocontext = self.cluster.open_ioctx(pool)
        all_objects = iocontext.list_objects()
        iocontext.close()
        return all_objects

    def read_object(self, pool, objectname):
        '''Reads an object and returns it's contents

        Reads an object and returns it's contents as an object in memory.
        '''
        iocontext = self.cluster.open_ioctx(pool)
        size, timestamp = iocontext.stat(objectname)
        readobj = iocontext.read(objectname, size)
        iocontext.close()
        return readobj

    def write_object(self, pool, objectname, contents):
        '''Writes an object to the rados cluster

        Takes as input the key/name of the object, contents to be written
        and pool name as a string. Writes the object contents to key objectname
        in the specified pool.
        '''
        iocontext = self.cluster.open_ioctx(pool)
        iocontext.write_full(objectname, contents)
        iocontext.close()

    def copy_object(self, obj, source, target):
        '''Copies a given object <obj> from source pool to target pool

        Copies and object from source pool to target pool can be a
        multiprocessing target.
        '''
        objname = obj.key
        print ('Copying: ' + str(objname))
        objcontents = self.read_object(source, objname)
        self.write_object(target, objname, objcontents)

    def copy_pool(self, source, target):
        '''Copies all objects from source pool to target pool

        Copies all objects in source pool to target pool.
        '''
        print ('Beginning copy from pool ' + source + ' to pool ' +
               target + ' with 1 simulataneous copies.')
        src_objs = self.get_obj_list(source)
        for obj in src_objs:
            self.copy_object(obj, source, target)
        print ('Pool copy complete.')
