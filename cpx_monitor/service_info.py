

class ServiceInfo(object):
    """
    Caputres basic information about
    a Service
    """

    def __init__(self, name, ip_addr):
        self.name = name
        self.ip_addr = ip_addr

    def __str__(self) -> str:
        return "<Service {} - {}>".format(self.name, self.ip_addr)
