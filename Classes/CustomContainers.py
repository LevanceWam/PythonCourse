# This class will help us keep track of the # of various tag on a blog
class TagCloud:
    def __init__(self):
        # define the dictionary
        self.tags = {}

    def add(self, tag):
        # use the get method to get a item ny a specified key
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        # this will get the number of a given tag
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        # we can set the number of a given tag
        self.tags[tag.lower()] = count

    def __len__(self):
        # this will give us the number of items
        return len(self.tags)

    def __iter__(self):
        # this will make it iterable
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
