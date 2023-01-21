import requests
from pprint import pprint

from cpx_monitor.log import get_logger
from cpx_monitor.service_info import ServiceInfo
logger = get_logger(__name__)


class CpxMonitor(object):
    """
    Handles monitor.
    """

    def __init__(self, server_url):
        """
        Args:
            server_url(str): URL to the CPX server
        """
        self._url = server_url
        self._services = []

    def fetch_servers(self):
        """
        Fetch servers.
        """
        url = self._url + "/servers"
        response = requests.get(url)
        logger.info("Fetching {}".format(url))
        if response.status_code == 200:
            data = response.json()
            logger.info(data)
            self.capture_server_info(data)

    def capture_server_info(self, server_ip_list):
        """
        Capture server info.

        Args:
            server_ip_list(list): List of IP addr of servers.
        """
        for server_ip in server_ip_list:
            url = self._url + '/' + str(server_ip)
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                server_info = ServiceInfo(name=data.get(
                    'service', 'Unknown'), ip_addr=server_ip)
                self._services.append(server_info)

    def list_services(self):
        """
        Print all services info.
        """
        for service in self._services:
            logger.info(service)
