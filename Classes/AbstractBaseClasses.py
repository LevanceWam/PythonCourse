from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        # To check to see if a stream is already open
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading Data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading Data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


stream = Stream()
stream.open
()
