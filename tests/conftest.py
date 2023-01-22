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
