import mock
from cpx_monitor.monitor import CpxMonitor
from cpx_monitor.monitor import NO_NAME

TEST_URL = "/this/is/test/url:5500"


def test_cpx_monitor_servers_fetches_server_data(server_data):
    """
    """
    cpx_monitor = CpxMonitor(server_url=TEST_URL)
    url = TEST_URL + "/servers"
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = server_data
    with mock.patch("requests.get", return_value=mock_resp) as mock_req:
        capture_serv_info_mock = mock.Mock()
        cpx_monitor.capture_services_info = capture_serv_info_mock
        cpx_monitor.fetch_services()
        mock_req.assert_called_once_with(url)
        capture_serv_info_mock.assert_called_once_with(server_data)


def test_cpx_monitor_capture_services_info(server_data, host_data):
    """
    """
    cpx_monitor = CpxMonitor(server_url=TEST_URL)
    data = host_data[0]
    url = TEST_URL + "/{}".format(data.get('ip_addr'))
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = host_data[0]
    assert not cpx_monitor._services
    with mock.patch("requests.get", return_value=mock_resp) as mock_req:
        cpx_monitor.capture_services_info(server_ip_list=[server_data[0]])
        mock_req.assert_called_once_with(url)
        assert NO_NAME in cpx_monitor._services
        service = cpx_monitor._services[NO_NAME]
        assert len(service.hosts) == 1
        assert service.hosts[0].cpu() == "23%"
        assert service.hosts[0].memory() == "45%"
