

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
        self.hosts.append(HostInfo(ip_addr, data))

    def __str__(self) -> str:
        return "<Service {} - {}>".format(self.name, self.num_hosts)

    @property
    def num_hosts(self):
        return len(self.hosts)

    @property
    def is_running(self):
        """
        A service is running if it has atleast one host.

        Returns:
            bool: True if running else False.
        """
        return bool(self.num_hosts)

    @property
    def needs_attention(self):
        """
        Returns whether the service needs attention.
        (i.e less than two running hosts)

        Returns:
            bool: True if it needs otherwise False.
        """
        return self.num_hosts < 2

    @property
    def avg_cpu(self):
        """
        Returns the average cpu usage across hosts.
        """
        cpu_usage = 0
        for host in self.hosts:
            cpu_usage += int(host.cpu)
        return cpu_usage/self.num_hosts

    @property
    def avg_memory(self):
        """
        Returns the average memory usage across hosts.
        """
        cpu_usage = 0
        for host in self.hosts:
            cpu_usage += int(host.memory)
        return cpu_usage/self.num_hosts


class HostInfo(object):
    """
    Host information.
    """

    def __init__(self, ip_addr, data):
        self.ip_addr = ip_addr
        self._cpu = data.get("cpu", None)
        self._memory = data.get("memory", None)

    def __str__(self):
        return "< HostInfo {} - {} - {} >".format(self.ip_addr, self.cpu, self.memory)

    @property
    def cpu(self):
        return self._cpu.split('%')[0] if self._cpu else 0

    @property
    def memory(self):
        return self._memory.split('%')[0] if self._memory else 0
