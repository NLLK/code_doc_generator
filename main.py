import os

from settings import Settings

class MainFunctionality:
    def __init__(self, settings, outputFileDesc):
        self.settings = settings
        self.outputFileDesc = outputFileDesc
        pass

    def start_proccess(self):
        self.readFolder(settings.inputPath)

    def readFolder(self, folderPath):

        if  not self.apply_filters_on_folder(folderPath): return

        #get folder content
        folderContent = os.listdir(folderPath)

        #for each element in folderContent
        for dirElement in folderContent:
            #create name for element 
            pathName = folderPath + os.path.sep + dirElement
            #check if it file or folder. if file - write down file content
            if os.path.isfile(pathName):
                rel_path = os.path.relpath(pathName, self.settings.inputPath)
                self.readFile(pathName, rel_path)
            #if folder - run this method again
            else: self.readFolder(pathName)

        pass

    def readFile(self, filePath, place_in_folder):
        if not self.apply_filters_on_file(filePath): return

        file = open(filePath,'r', encoding = self.settings.file_codec)
        
        #file name header
        self.outputFileDesc.write('\n'+'Имя файла: '+place_in_folder + '\n'+'\n')

        for line in file:
            self.outputFileDesc.write(line)
        file.close()

    def apply_filters_on_file(self, filePath):
        filename, file_extension = os.path.splitext(filePath)

        if file_extension in self.settings.file_extensions:
            #dont include this file in listing
            if os.path.abspath(__file__) == filePath: return False 
            return True
        
        return False
    
    def apply_filters_on_folder(self, folderPath):

        if folderPath in self.settings.ignorePaths_ready:
            return False

        return True


#entry point of app
if __name__ == "__main__":

    settings = Settings()
    print("Settings: ")
    print("inputPath:", settings.inputPath)
    print("fileExtentions:", settings.file_extensions)
    
    if settings.extentions_pack:
        print("extentionsPack:",settings.extentions_pack)

    print("outputFile:", settings.outputFile)
    print("ignorePaths:", settings.ignorePaths)

    _outputFile = open(settings.outputFile,'w')

    func = MainFunctionality(settings, _outputFile)
    #entry point of going through folder
    func.start_proccess()

    #closing output file. The end
    _outputFile.close()

    print(f'Programm finished it`s work. Result file is placed in {settings.outputFile}')


