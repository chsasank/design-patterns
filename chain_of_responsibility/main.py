HELP_TOPICS = {
    1: "This is a button. You can click it.",
    2: "Welcome to my application"
}


class HelpHandler:
    def __init__(self, successor_help_handler=None, help_topic=None):
        self._successor = successor_help_handler
        self._help_topic = help_topic

    def has_help(self):
        return self._help_topic is not None

    def set_handler(self, help_handler, help_topic):
        pass

    def handle_help(self):
        if self._successor:
            return self._successor.handle_help()


class Widget(HelpHandler):
    def __init__(self, parent_widget, help_topic=None):
        self._parent = parent_widget
        super().__init__(
            successor_help_handler=self._parent, help_topic=help_topic
        )


class Button(Widget):
    def handle_help(self):
        if self.has_help():
            print('==> Button help being shown')
            print(HELP_TOPICS[self._help_topic])
        else:
            super().handle_help()


class Application(HelpHandler):
    """End of chain. Note the inheritance from HelpHandler, not widget."""
    def handle_help(self):
        if self.has_help():
            print('==> Application help being shown')
            print(HELP_TOPICS[self._help_topic])
        else:
            super().handle_help()


if __name__:
    app = Application(help_topic=2)
    button = Button(app, help_topic=1)
    Widget = Widget(app)

    button.handle_help()
    Widget.handle_help()
