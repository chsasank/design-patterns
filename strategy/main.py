class TextView:
    def __init__(self, text, line_breaker):
        self._line_breaker = line_breaker
        self._text = text

    def update(self, text):
        self._text = text
        self.draw()

    def draw(self):
        lines = self._line_breaker.break_text(self._text)
        print('=> Rendered the following')
        print('\n'.join(lines))


class LineBreaker:
    """Base class for all algorithms which can do line breaking"""
    def __init__(self):
        pass

    def break_text(self, text):
        raise NotImplementedError


class SimpleLineBreaker(LineBreaker):
    """Breaks line based on simple line width rule."""
    def __init__(self, line_width):
        self._line_width = line_width
        super().__init__()

    def break_text(self, text):
        break_point = 0
        lines = []
        while break_point < len(text):
            lines.append(text[break_point: break_point + self._line_width])
            break_point = break_point + self._line_width

        return lines


class WordLineBreaker(LineBreaker):
    """Breaks line based on word boundaries with maximum line width."""
    def __init__(self, line_width):
        self._line_width = line_width

    def break_text(self, text):
        lines = []
        words = text.split()
        current_line = ''
        for word in words:
            new_current_line = current_line + ' ' + word
            if len(new_current_line) > self._line_width:
                lines.append(current_line)
                current_line = ''
            else:
                current_line = new_current_line

        if len(current_line) > 0:
            lines.append(current_line)
        return lines


if __name__ == "__main__":
    print('==> SimpleLineBreaker')
    text_view = TextView(
        text='Hello world',
        line_breaker=SimpleLineBreaker(line_width=20)
    )
    text_view.draw()
    text_view.update('Hello world ' * 10)

    print('==> WordLineBreaker')
    text_view = TextView(
        text='Hello world',
        line_breaker=WordLineBreaker(line_width=20)
    )
    text_view.draw()
    text_view.update('Hello world ' * 10)
