class VisualComponent:
    def __init__(self):
        pass

    def draw(self):
        pass


class Decorator(VisualComponent):
    """Decorates a visual component.

    Defines a default implementation that pass the request to the component.
    """
    def __init__(self, visual_component):
        self._component = visual_component

    def draw(self):
        self._component.draw()


class BorderDecorator(Decorator):
    def __init__(self, visual_component, border_width):
        self._width = border_width
        super().__init__(visual_component)

    def draw(self):
        super().draw()
        self._draw_border(self._width)

    def _draw_border(self, width):
        print(f"Drew border of width {width} to {self._component}")


class ScrollDecorator(Decorator):
    def draw(self):
        super().draw()
        self._draw_scroll()

    def _draw_scroll(self):
        print(f"Drew scroll to {self._component}")


class TextView(VisualComponent):
    """A simple text visual component which we'll decorate."""
    def __init__(self, text):
        self._text = text
        super().__init__()

    def draw(self):
        print(f'Drew TextView with text "{self._text}"')


if __name__ == "__main__":
    text_view = BorderDecorator(
        ScrollDecorator(TextView('Hello world')),
        border_width=10
    )
    text_view.draw()
