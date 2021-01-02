class Graphic:
    """Base class for graphical objects in the graphical editor."""
    pass


class ConstraintSolver():
    def __init__(self):
        pass

    def solve(self):
        pass

    def add_constraint(start_connection, end_connection):
        pass

    def remove_constraint(start_connection, end_connection):
        pass

    def create_memento(self):
        pass

    def set_memento(self):
        pass


class ConstraintSolverMemento():
    def __init__(self):
        pass


class MoveCommand():
    def __init__(self, target_graphic, delta):
        self._target = target_graphic
        self._delta = delta
        self._state = None

    def execute(self):
        solver = ConstraintSolver()
        self._state = solver.create_memento()
        self._target.move(self._delta)
        solver.solve()

    def unexecute(self):
        solver = ConstraintSolver()
        self._target.move(-self._delta)
        solver.set_memento(self._state)
        solver.solve()
