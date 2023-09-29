import os
import argparse

class Settings:
    parser = argparse.ArgumentParser()

    inputPath = os.path.abspath(os.getcwd())
    outputFile = './code.txt'
    ignorePaths = []
    
    file_extensions = ['.c', '.h', '.py']

    def init_arguments(self):
        self.parser.add_argument('-i', '--inputPath',       
            help= f'Path with code. Default = {self.inputPath}')
        
        self.parser.add_argument('-o', '--outputFile',      
            help= f'Full file path for output file. Default = {self.outputFile}')
        
        self.parser.add_argument('-e', '--fileExtentions', nargs='+',  
            help= f'A list of file extentions. Ex: \"-e \'.c\' \'.cpp\' \'.h\'\". Default = {self.file_extensions}')
        
        self.parser.add_argument('-d', '--ignorePaths', nargs='+',  
            help= f'A list of folders to ingore. Ex: \"-d \"./Debug\"\" Default = {self.ignorePaths}')

        pass

    def parse_arguments(self):
        args = self.parser.parse_args()
        if args.inputPath:
            self.inputPath = args.inputPath

        if args.outputFile:
            self.outputFile = args.outputFile

        if args.fileExtentions:
            self.file_extensions = args.fileExtentions

        if args.ignorePaths:
            self.ignorePaths = args.ignorePaths
        pass

    def __init__(self) -> None:
        self.init_arguments()
        self.parse_arguments()

class MainFunctionality:
    def __init__(self, settings, outputFileDesc):
        self.settings = settings
        self.outputFileDesc = outputFileDesc
        pass

    def start_proccess(self):
        self.readFolder(settings.inputPath)

    def readFolder(self, folderPath):
        #get folder content
        folderContent = os.listdir(folderPath)

        #for each element in folderContent
        for dirElement in folderContent:
            #create name for element 
            pathName = folderPath + "/" + dirElement
            #check if it file or folder. if file - write down file content
            if os.path.isfile(pathName):
                self.readFile(pathName, dirElement)
            #if folder - run this method again
            else: self.readFolder(pathName)

        pass

    def readFile(self, filePath, place_in_folder):

        if not self.apply_filters_on_file(filePath): return

        file = open(filePath,'r', encoding="utf-8")
        
        self.outputFileDesc.write('\n'+'Имя файла: '+place_in_folder + '\n'+'\n')

        for line in file:
            self.outputFileDesc.write(line)
        file.close()

    def apply_filters_on_file(self, filePath):
        filename, file_extension = os.path.splitext(filePath)

        if file_extension in settings.file_extensions:
            return True
        
        return False
    
    def apply_filters_on_folder(self, folderPath):
        pass


#entry point of app
if __name__ == "__main__":

    settings = Settings()
    print("Settings: ")
    print("inputPath:", settings.inputPath, "\nfileExtentions:", settings.file_extensions, 
          "\noutputFile:", settings.outputFile, "\nignorePaths:", settings.ignorePaths)

    _outputFile = open(settings.outputFile,'w')

    func = MainFunctionality(settings, _outputFile)
    #entry point of going through folder
    func.start_proccess()

    #closing output file. The end
    _outputFile.close()

    print(f'Programm finished it`s work. Result file is placed in {settings.outputFile}')


