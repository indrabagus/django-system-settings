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
    total_memory_ex = serializers.CharField(read_only=True,source='total_memory')
    free_memory = serializers.CharField(read_only=True)

class LinuxSysInfoSerializer(serializers.Serializer):
    platform = LinuxPlatformSerializer(required=True)
    meminfo = LinuxMemInfoSerializer(required=True)