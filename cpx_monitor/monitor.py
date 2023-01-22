import os
import time
from prettytable import PrettyTable
import requests

from cpx_monitor.log import get_logger
from cpx_monitor.service_info import ServiceInfo
logger = get_logger(__name__)

NO_NAME = "Unknown"


class ConsoleColor:
    # Color
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GRAY = '\033[97m'

    # Style
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # BackgroundColor
    BgBLACK = '\033[40m'
    BgRED = '\033[41m'
    BgGREEN = '\033[42m'
    BgORANGE = '\033[43m'
    BgBLUE = '\033[44m'
    BgPURPLE = '\033[45m'
    BgCYAN = '\033[46m'
    BgGRAY = '\033[47m'

    # End
    END = '\033[0m'


class CpxMonitor(object):
    """
    Captures services and hosts information from CPX Service.
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

    def list_services_avg(self):
        """
        Print services avg cpu/mem info.
        """
        ptable = PrettyTable(["Service", "AVG CPU", "AVG MEMORY"])
        logger.info("Listing services - ")
        for name, service in self._services.items():
            if service.needs_attention:
                ptable.add_row(
                    [ConsoleColor.RED + name, service.avg_cpu, str(service.avg_memory) + ConsoleColor.END])
            else:
                ptable.add_row(
                    [ConsoleColor.GREEN + name, service.avg_cpu, str(service.avg_memory) + ConsoleColor.END])
        print(ptable)

    def list_services(self, services=None):
        """
        Print cpu/mem info for all hosts per service. 
        """
        ptable = PrettyTable(
            ["IP", "Service", "CPU", "MEMORY"])
        for name, service in self._services.items():
            for host in service.hosts:
                if services and name not in services:
                    continue
                if service.needs_attention:
                    ptable.add_row([ConsoleColor.RED + host.ip_addr,
                                   name, host.cpu(), host.memory() + ConsoleColor.END])
                else:
                    ptable.add_row([ConsoleColor.GREEN + host.ip_addr,
                                   name, host.cpu(), host.memory() + ConsoleColor.END])
        print(ptable)

    def track_services(self, services, interval_sec=2):
        """
        Track a given list of services over time.

        Args:
            services(list): List of service names to track.
        """
        for service_name in services:
            if service_name not in self._services:
                raise IOError(
                    "{} service not found in CPX".format(service_name))
        while True:
            self.clear_screen()
            self.list_services(services=services)
            time.sleep(interval_sec)

    @staticmethod
    def clear_screen():
        """
        Clear screen
        """
        # posix is os name for Linux or mac
        if (os.name == 'posix'):
            os.system('clear')
        # else screen will be cleared for windows
        else:
            os.system('cls')
