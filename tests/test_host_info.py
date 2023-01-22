import pytest
import mock
from cpx_monitor.service_info import HostInfo


def test_host_info_ip_cpu_and_memory(host_data):
    """
    """
    data = host_data[0]
    host_info = HostInfo(data.get("ip_addr"), data)
    host_info.cpu() == data.get('cpu')
    host_info.memory() == data.get('memory')
    host_info.ip_addr == data.get('ip_addr')


def test_host_info_cpu_memory_as_num(host_data):
    """
    """
    data = host_data[0]
    host_info = HostInfo(data.get("ip_addr"), data)
    host_info.cpu(as_num=True) == data.get('cpu').split('%')[0]
    host_info.memory(as_num=True) == data.get('memory').split('%')[0]
