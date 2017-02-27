import datetime


class File:
    now = datetime.datetime.now()

    def __init__(self, name="Empty", values=None):
        self.name = name
        self._update_time()
        self.data = []
        self.size = len(self.data)
        if values is not None:
            for g in values:
                self.data.append(g)
                self.size += len(g)

    def __add__(self, string):
        self._update_time()
        self.size += len(string)
        self.data.append(string)

    def __len__(self):
        return self.size

    def getModified(self):
        return self.lastModified

    def getData(self):
        return self.data

    def getName(self):
        return self.name

    def _update_time(self):
        self.lastModified = str(File.now.month) + "/" + str(File.now.day) + "/" + str(File.now.year)

    def printContents(self):
        for s in self.data:
            print(s)


class Folder:

    def __init__(self, name, values=None):
        self.name = name
        self.files = []
        if values is not None:
            for i in values:
                self.files.append(i)

    def __add__(self, fileObj):
        self.files.append(fileObj)

    def getName(self):
        return self.name

    def printFilenames(self):
        if not self.files:
            print("Folder", self.name, "is empty!")
        else:
            print("Folder", self.name, "contains:")
            for i in self.files:
                print("File Name:", self.name + " |", "File size:", i.__len__(), "bytes. (ASCII) | Last Modified:",
                      i.getModified())

    def deleteFiles(self, name="", lastModified="", size=0):
        counter = 0
        files_deleted = 0
        while counter != len(self.files):
            if name == self.files[counter].getName() \
                    or lastModified == self.files[counter].getModified() or self.files[counter].__len__() == size:
                del self.files[counter]
                files_deleted += 1
            else:
                counter += 1
        print(files_deleted, "files were deleted from", self.name+".")

