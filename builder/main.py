class MazeBuilder:
    def __init__(self):
        pass

    def build_maze(self):
        pass

    def build_room(self, room_number):
        pass

    def build_door(self, room_from, room_to):
        pass

    def get_maze(self):
        return 0


class MazeGame:
    """MazeGame uses builder to create the maze."""
    def __init__(self):
        pass

    def create_maze(self, maze_builder):
        maze_builder.build_maze()

        maze_builder.build_room(1)
        maze_builder.build_room(2)
        maze_builder.build_door(1, 2)

        return maze_builder.get_maze()

    def create_complex_maze(self, maze_builder):
        maze_builder.build_maze()
        for i in range(1, 100):
            maze_builder.build_room(i)

        return maze_builder.get_maze()


class StandardMazeBuilder(MazeBuilder):
    """Concrete instance of maze builder."""
    def __init__(self):
        self._current_maze = None

    def build_maze(self):
        self._current_maze = Maze()

    def get_maze(self):
        return self._current_maze

    def build_room(self, room_number):
        if room_number not in self._current_maze:
            room = Room(room_number)
            self._current_maze.add_room(room)

            room.set_side(North, Wall())
            room.set_side(South, Wall())
            room.set_side(East, Wall())
            room.set_side(West, Wall())

    def build_door(self, room_from, room_to):
        r1 = self._current_maze[room_from]
        r2 = self._current_maze[room_to]

        r1.set_side(CommonWall(r1, r2), d)
        r2.set_side(CommonWall(r2, r1), d)


class CountingMazeBuilder(MazeBuilder):
    """Just counts different kind of components that would be required."""
    def __init__(self):
        self._rooms = 0
        self._doors = 0
        super().__init__()

    def build_room(self, room_number):
        self._rooms += 1

    def build_door(self, room_from, room_number):
        self._doors += 1

    def get_counts(self):
        return self._rooms, self._doors


def main():
    maze_game = MazeGame()
    maze_builder = StandardMazeBuilder()
    maze_game.create_maze(maze_builder)
    maze = maze_builder.get_maze()
