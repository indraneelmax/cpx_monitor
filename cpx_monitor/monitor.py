import requests
from pprint import pprint

from cpx_monitor.log import get_logger
from cpx_monitor.service_info import ServiceInfo
logger = get_logger(__name__)

NO_NAME = "Unknown"


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
        self._services = {}

    def fetch_services(self):
        """
        Fetch servers.
        """
        url = self._url + "/servers"
        response = requests.get(url)
        logger.debug("Fetching {}".format(url))
        if response.status_code == 200:
            data = response.json()
            logger.debug(data)
            self.capture_services_info(data)

    def capture_services_info(self, server_ip_list):
        """
        Capture services info.

        Args:
            server_ip_list(list): List of IP addr of servers.
        """
        for server_ip in server_ip_list:
            url = self._url + '/' + str(server_ip)
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                name = data.get('service', NO_NAME)
                exist_serv_info = self._services.get(name, None)
                if not exist_serv_info:
                    exist_serv_info = ServiceInfo(name=name)
                    self._services[name] = exist_serv_info
                exist_serv_info.add_host(ip_addr=server_ip, data=data)

    def list_services(self):
        """
        Print all services info.
        """
        logger.info("Listing services - ")
        for name, service in self._services.items():
            logger.info(service)
            logger.info(
                "{}% - {}%".format(service.avg_cpu, service.avg_memory))
