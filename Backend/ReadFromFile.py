
class ReadFromFile:
    def ReadFileText(self, url):
        with open(url, 'r') as myfile:
            data=myfile.readlines()
            return data
    def PrintData(self, url):
        print(self.ReadFileText(url))
