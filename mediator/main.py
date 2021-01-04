class DialogDirector:
    """Subclasses do the mediation"""
    def __init__(self):
        pass

    def show_dialog(self):
        pass

    def widget_changed(self, widget):
        pass

    def _create_widgets(self):
        """Override and construct the widgets in the dialogue."""
        pass


class Widget:
    """Base class for all widgets. Knows its director."""
    def __init__(self, dialog_director):
        self._director = dialog_director
    
    def changed(self):
        """Informs the director of the change."""
        self._director.widget_changed(widget=self)

    def handle_mouse(self, event):
        pass


class ListBox(Widget):
    """Subclass of widget for UI element."""
    def __init__(self, dialog_director):
        super().__init__(dialog_director)
        self._list = []

    def get_selection(self):
        pass

    def set_list(self, list_items):
        self._list = list_items

    def handle_mouse(self, event):
        pass


class EntryField(Widget):
    def set_text(self, text):
        pass

    def get_text(self):
        pass

    def handle_mouse(self, event):
        pass


class Button(Widget):
    def set_text(self, text):
        pass
    
    def handle_mouse(self, event):
        self.changed()


class FontDialogDirector(DialogDirector):
    """Mediates between widgets in the dialog box."""
    def _create_widgets(self):
        self._ok = Button(dialog_director=self)
        self._cancel = Button(dialog_director=self)
        self._font_list = ListBox(dialog_director=self)
        self._font_name = EntryField(dialog_director=self)

        available_fonts = ['Helvetica', 'Georgia']
        self._font_list.set_list(available_fonts)

    def widget_changed(self, widget):
        if widget == self._font_list:
            self._font_name.set_text(self._font_list.get_selection())
        elif widget == self._ok:
            print('Set font name as', self._font_name.get_text())
            print('Closed the dialog box')
        elif widget == self._cancel:
            print('Closed the dialog box')
