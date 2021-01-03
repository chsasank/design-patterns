class MazeFactory:
    """Factory that can be used by file loading or a maze builder."""
    def __init__(self):
        pass

    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_room(self, room_number):
        return Room(room_number)

    def make_door(self, room_from, room_to):
        return Door(room_from, room_to)


class MazeGame:
    def create_maze(self, factory):
        """Uses factory so that exact components are not hardcoded."""
        maze = factory.make_maze()
        r1 = factory.make_room(1)
        r2 = factory.make_room(2)
        door = factory.make_door(r1, r2)

        maze.add_room(r1)
        maze.add_room(r2)

        r1.set_side(North, factory.make_wall())
        r1.set_side(East, door)
        r1.set_side(South, factory.make_wall())
        r1.set_side(West, factory.make_wall())

        r2.set_side(North, factory.make_wall())
        r2.set_side(East, factory.make_wall())
        r2.set_side(South, factory.make_wall())
        r2.set_side(West, door)

        return maze


class EnchantedMazeFactory(MazeFactory):
    def make_room(self, room_number):
        return EnchantedRoom(room_number, self._cast_spell())

    def make_door(self, room_from, room_to):
        return DoorNeedingSpell(room_from, room_to)

    def _cast_spell(self):
        pass


class BombedMazeFactory(MazeFactory):
    def make_wall(self):
        return BombedWall()

    def make_room(self, room_number):
        return RoomWithABomb(room_number)


def main():
    game = MazeGame()
    game.create_maze(BombedMazeFactory())
