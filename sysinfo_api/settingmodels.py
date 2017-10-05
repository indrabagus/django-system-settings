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
                meminfo[line.split(':')[0]] = int(line.split(':')[1].split('kB')[0].strip())
        return meminfo

    def __init__(self):
        meminfo = LinuxMemInfo._meminfo()
        self.__dict__ = meminfo

class LinuxCPUInfo(object):
    def _cpuinfo():
        ''' Return the information in /proc/cpuinfo
        as a dictionary in the following format:
        cpu_info['proc0']={...}
        cpu_info['proc1']={...}
        '''
        cpuinfo=OrderedDict()
        procinfo=OrderedDict()
        nprocs = 0
        with open('/proc/cpuinfo') as f:
            for line in f:
                if not line.strip():
                    # end of one processor
                    cpuinfo['proc%s' % nprocs] = procinfo
                    nprocs=nprocs+1
                    # Reset
                    procinfo=OrderedDict()
                else:
                    if len(line.split(':')) == 2:
                        procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                    else:
                        procinfo[line.split(':')[0].strip()] = ''
            
        return cpuinfo

    def __init__(self):
        cpuinfo = LinuxCPUInfo._cpuinfo()



class LinuxSysInfo(object):
    platform = LinuxPlatform()
    meminfo = LinuxMemInfo()