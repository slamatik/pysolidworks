import win32com.client as win32


class Com:
    class __Com:
        def __init__(self, pid):
            self.pid = pid
            self.com = win32.Dispatch(self.pid)

    instance = None

    def __new__(cls, pid):
        if not cls.instance:
            cls.instance = cls.__Com(pid).com
        return cls.instance
