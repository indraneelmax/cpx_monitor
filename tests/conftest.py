import pytest


@pytest.fixture(scope='function')
def host_data():
    host_data = [{
        'ip_addr': '10.58.1.41',
        'cpu': '23%',
        'memory': '45%'
    },
        {
        'ip_addr': '10.48.5.31',
        'cpu': '33%',
        'memory': '15%'

    }]
    return host_data


@pytest.fixture(scope='function')
def server_data(host_data):
    return [host_data[0].get("ip_addr"), host_data[1].get("ip_addr")]
