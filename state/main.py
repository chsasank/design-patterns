class TCPState(object):
    pass


class TCPConnection(object):
    def __init__(self):
        self._state = TCPState()

    def active_open(self):
        pass

    def passive_open(self):
        pass

    def close(self):
        pass

    def send(self):
        pass

    def acknowledge(self):
        pass

    def synchronize(self):
        pass

    def _change_state(self, state):
        pass


class TCPState(object):
    def transmit(tcp_connection, tcp_stream):
        pass

    """
    Duplicate the state changing interface of TCPConnection.
    But they takes a TCPConnection instance as a parameter so that
    they can modify its state depending on its data.
    """
    def active_open(self, tcp_connection):
        pass

    def passive_open(self, tcp_connection):
        pass

    def close(self, tcp_connection):
        pass

    def send(self, tcp_connection):
        pass

    def acknowledge(self, tcp_connection):
        pass

    def synchronize(self, tcp_connection):
        pass

    def _change_state(self, tcp_connection, tcp_state):
        pass

