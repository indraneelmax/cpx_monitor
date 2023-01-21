

class ServiceInfo(object):
    """
    Caputres basic information about
    a Service
    """

    def __init__(self, name):
        self.name = name
        self.hosts = []

    def add_host(self, ip_addr, data):
        """
        Add a host to the service.

        Args:
            ip_addr(str): IP addr for the host.
        """
        self.hosts.append(ip_addr)

    def __str__(self) -> str:
        return "<Service {} - {}>".format(self.name, self.num_hosts)

    @property
    def num_hosts(self):
        return len(self.hosts)


class HostInfo(object):
    """
    Host information.
    """

    def __init__(self, ip_addr, data):
        self.ip_addr = ip_addr
        self.cpu = data.get("cpu", None)
        self.memory = data.get("memory", None)

    def __str__(self) -> str:
        return "< HostInfo {} - {} - {} >".format(self.ip_addr, self.cpu, self.memory)
