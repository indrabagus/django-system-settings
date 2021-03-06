from rest_framework import serializers

class LinuxPlatformSerializer(serializers.Serializer):
    system = serializers.CharField(read_only=True)
    node = serializers.CharField(read_only=True)
    release = serializers.CharField(read_only=True)
    version = serializers.CharField(read_only=True)
    machine = serializers.CharField(read_only=True)
    processor = serializers.CharField(read_only=True)
    linux_distrib = serializers.CharField(read_only=True)
    architecture = serializers.CharField(read_only=True)

class LinuxMemInfoSerializer(serializers.Serializer):
    active = serializers.IntegerField(read_only=True,source='Active')    
    active_str = serializers.CharField(read_only=True,source='Active')
    mem_available = serializers.IntegerField(read_only=True,source='MemAvailable')
    mem_available_str = serializers.CharField(read_only=True,source='MemAvailable')    
    mem_free = serializers.IntegerField(read_only=True,source='MemFree')
    mem_free_str = serializers.CharField(read_only=True,source='MemFree')
    mem_total = serializers.IntegerField(read_only=True,source='MemTotal')    
    mem_total_str = serializers.CharField(read_only=True,source='MemTotal')
    kernel_stack = serializers.IntegerField(read_only=True,source='KernelStack')    
    kernel_stack_str = serializers.CharField(read_only=True,source='KernelStack')            

class LinuxSysInfoSerializer(serializers.Serializer):
    platform = LinuxPlatformSerializer(required=True)
    meminfo = LinuxMemInfoSerializer(required=True)