import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> str:
        if os.path.isfile(self.filename):
            self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if hasattr(self, "file"):
            self.file.close()
        os.remove(self.filename)
