class TCPConnection(object):
    def __init__(self):
        # self._state is an instance of TCPState.
        # Initialized with closed state.
        self._state = TCPClosedState()

    """
    Delegates state-specific requests to its TCPState instance.
    """
    def active_open(self):
        self._state.active_open(tcp_connection=self)

    def passive_open(self):
        self._state.passive_open(tcp_connection=self)

    def close(self):
        self._state.close(tcp_connection=self)

    def send(self):
        self._state.send(tcp_connection=self)

    def acknowledge(self):
        self._state.acknowledge(tcp_connection=self)

    def synchronize(self):
        self._state.synchronize(tcp_connection=self)

    def _change_state(self, state):
        self._state = state


class TCPState(object):
    """TCP State. Inherited by all concrete states. TCPState maintains no
    state internally. This class implements default for all states.
    """
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


class TCPEstablishedState(TCPState):
    def transmit(self, tcp_connection, tcp_stream):
        print(f"Transferred data {tcp_stream}")

    def close(self, tcp_connection):
        print('Sent FIN, received ACK of FIN')
        tcp_connection._change_state(TCPListenState())


class TCPListenState(TCPState):
    def send(self, tcp_connection):
        print("Sent SYN, received SYN, ACK etc.")
        tcp_connection._change_state(TCPEstablishedState())


class TCPClosedState(TCPState):
    def active_open(self, tcp_connection):
        print('Sent SYN, received SYN, ACK etc')
        tcp_connection._change_state(TCPEstablishedState())

    def passive_open(self, tcp_connection):
        tcp_connection._change_state(TCPListenState())