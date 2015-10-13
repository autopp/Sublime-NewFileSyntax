import sublime_plugin


class NewFileSyntax(sublime_plugin.EventListener):

    def on_new(self, view):
        settings = view.settings()
        new_file_syntax = settings.get('new_file_syntax', None)

        if new_file_syntax is not None:
            view.set_syntax_file(new_file_syntax)
