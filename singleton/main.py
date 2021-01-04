class Wall:
    pass


class BombedWall(Wall):
    pass


class MazeFactory:
    """We need only one maze factory."""
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance:
            raise RuntimeError(f"Use {type(self).__name__}.instance()")

    def build_wall(self):
        return Wall()


class BombedMazeFactory(MazeFactory):
    _instance = None

    def build_wall(self):
        return BombedWall()


if __name__ == "__main__":
    maze_factory = MazeFactory.instance()
    print(maze_factory.build_wall())

    bombed_maze_factory = BombedMazeFactory.instance()
    print(bombed_maze_factory._instance)
