class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud["PYTHON"])  # Will print 3
# this will not work because we dont have this key in the dictionary we need to hide it from the outside
# by adding __ will make it private we can still access it tho
print(cloud.__tags["PYTHON"])
