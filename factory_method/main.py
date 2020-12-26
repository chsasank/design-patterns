class Maze:
    pass


class Room:
    North = 0
    East = 1
    South = 2
    West = 3

    def __init__(self, n):
        self.n = n

    def set_side(self, side, element):
        pass


class Door:
    def __init__(self, room_1, room_2):
        self.room_1 = room_1
        self.room_2 = room_2


class MazeGame:
    """Declares factory methods for creating objects like maze, room etc."""
    def __init__(self):
        pass

    def create_maze(self):
        a_maze = self.make_maze()

        r1 = self.make_room(1)
        r2 = self.make_room(2)
        the_door = self.make_door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)
        
        r1.set_side(Room.North, self.make_wall())
        r1.set_side(Room.East, the_door)
        r1.set_side(Room.South, self.make_wall())
        r1.set_side(Room.West, self.make_wall())

        r1.set_side(Room.North, self.make_wall())
        r1.set_side(Room.East, self.make_wall())
        r1.set_side(Room.South, self.make_wall())
        r1.set_side(Room.West, the_door)

        return a_maze

    def make_maze(self):
        return Maze()

    def make_room(self, n):
        return Room(n)

    def make_wall(self):
        return Wall()

    def make_door(self, room_1, room_2):
        return Door(room_1, room_2)


class BombedMazeGame(MazeGame):
    def make_wall(self):
        return BombedWall()

    def make_room(self):
        return RoomWithABomb(n)


class EnchantedMazeGame(MazeGame):
    def make_room(self):
        return EnchantedRoom(n, self.cast_spell())
    
    def make_door(self, room_1, room_2):
        return DoorNeedingSpell(room_1, room_2)

    def cast_spell(self):
        pass