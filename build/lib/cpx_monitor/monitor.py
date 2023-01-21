import requests
from pprint import pprint

from cpx_monitor.log import get_logger

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
        self._servers = []

    def fetch_servers(self):
        """
        Fetch servers.
        """
        url = self._url + "/servers"
        response = requests.get(url)
        logger.info("Fetching {}".format(url))
        import pdb
        pdb.set_trace()
        if response.status_code == 200:
            data = response.json()
            logger.info(data)
