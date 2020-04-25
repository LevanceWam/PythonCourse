class Text(str):
    # we are inheriting from the string method
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    # we are inheriting from the list methods
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
