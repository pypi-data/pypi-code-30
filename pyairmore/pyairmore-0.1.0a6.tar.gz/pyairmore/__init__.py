"""
Pyairmore package
"""  # todo [1] package doc

__version__ = "0.1.0a6"
__author__ = "Eray Erdin"


class Refreshable:
    # todo doc

    def refresh(self) -> None:
        raise NotImplementedError("This method needs to be overriden by children.")
