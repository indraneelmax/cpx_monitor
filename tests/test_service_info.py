import pytest
import mock
from cpx_monitor.service_info import ServiceInfo

TEST_SERVICE_NAME = "TestService"


def test_service_info_name():
    """
    """
    name = "TestService"
    serv_info = ServiceInfo(name=name)
    assert serv_info.name == name


def test_service_add_hosts(host_data):
    """
    """
    serv_info = ServiceInfo(name=TEST_SERVICE_NAME)
    assert serv_info.num_hosts == 0
    data = host_data[0]
    serv_info.add_host(ip_addr=data.get('ip_addr'),
                       data=data)
    assert serv_info.num_hosts == 1
    host = serv_info.hosts[0]
    assert host.cpu() == data.get('cpu')
    assert host.memory() == data.get('memory')


def test_service_avg_cpu_and_avg_memory(host_data):
    """
    """
    serv_info = ServiceInfo(name=TEST_SERVICE_NAME)
    assert serv_info.num_hosts == 0
    data = host_data[0]
    serv_info.add_host(ip_addr=data.get('ip_addr'),
                       data=data)
    data = host_data[1]
    serv_info.add_host(ip_addr=data.get('ip_addr'),
                       data=data)
    assert serv_info.num_hosts == 2
    assert serv_info.avg_cpu == '28.00%'
    assert serv_info.avg_memory == '30.00%'
