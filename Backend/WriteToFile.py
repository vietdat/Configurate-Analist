
class WriteToFile:
    def WriteToFileText(self, url, content):
        with open(url, 'a') as myfile:
            myfile.write(content + '\n')
            myfile.close()
