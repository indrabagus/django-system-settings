# coding: utf-8
"""
Various custom model object that doesn't have correlation to any Databases's table.
"""

import platform
from collections import OrderedDict


class LinuxPlatform(object):
    def __init__(self):
        self.system = platform.system()
        self.node = platform.node()
        self.release = platform.release()
        self.version = platform.version()
        self.machine = platform.machine()
        self.processor = platform.processor()
        self.linux_distrib = "%s - %s - %s" % platform.linux_distribution()
        self.architecture = "%s %s" % platform.architecture()

    def __str__(self):
        return "%s - %s - %s - %s - %s - %s" % (
                    self.system,
                    self.node,
                    self.release,
                    self.version,
                    self.machine,
                    self.processor
                )

class LinuxMemInfo(object):
    def _meminfo():
        ''' Return the information in /proc/meminfo as a dictionary '''
        meminfo=OrderedDict()
        with open('/proc/meminfo') as f:
            for line in f:
                meminfo[line.split(':')[0]] = line.split(':')[1].strip()
        return meminfo

    def __init__(self):
        meminfo = LinuxMemInfo._meminfo()
        self.total_memory = meminfo['MemTotal']
        self.free_memory = meminfo['MemFree']


class LinuxSysInfo(object):
    platform = LinuxPlatform()
    meminfo = LinuxMemInfo()