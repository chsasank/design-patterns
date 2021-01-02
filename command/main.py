class Command:
    def __init__(self):
        pass

    def execute(self):
        pass


class OpenCommand(Command):
    def __init__(self, application):
        self._application = application
        self._response = None
        super().__init__()

    def execute(self):
        name = self.ask_user()

        if name:
            document = Document(name)
            self._application.add(document)
            document.open()

    def ask_user(self):
        return input('Input document name: ')


class PasteCommand(Command):
    def __init__(self, document):
        self._document = document
        super().__init__()

    def execute(self):
        self._document.paste()


class MacroCommand(Command):
    def __init__(self):
        self._commands = []
        super().__init__()

    def add(self, command):
        self._commands.append(command)

    def remove(self, command):
        self._commands.remove(command)

    def execute(self):
        for cmd in self._commands:
            cmd.execute()
