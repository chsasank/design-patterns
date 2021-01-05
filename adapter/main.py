class Shape:
    """Bounding box defined by corners"""
    def __init__(self):
        print('init shape')

    def bounding_box(self, bottom_left_point, top_right_point):
        pass

    def create_manipulator(self):
        """Returns manipulator object to animate the shape"""
        pass


class TextView:
    """Defined by origin, height, width"""
    def __init__(self):
        print('init textview')

    def get_origin(self, x, y):
        pass

    def get_extent(self, width, height):
        pass

    def is_empty(self):
        pass


class TextShape(TextView, Shape):
    """Make a text view look like shape."""
    def __init__(self, text_view):
        self._text_view = text_view

    def bounding_box(self, bottom_left_point, top_right_point):
        """Converts Textview interface to confirm to shape."""
        
if __name__ == "__main__":
    TextShape()