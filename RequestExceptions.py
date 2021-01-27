from __future__ import print_function

class Error404(Exception):
    def __init__(self, url: str, time: float, msg: str = "Request to {} timed out in {}") -> None:
        self.url = url
        self.time = time
        self.msg = msg.format(url, time)
        super().__init__(self.msg)



