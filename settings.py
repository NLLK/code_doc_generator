import argparse
import os

class FileExtentionPack:
    qtQml = ['.c', '.cpp', '.h', '.pro', '.qrc', '.qml', '.js']
    simpleCpp = ['.c', '.cpp', '.h']
    qt = ['.c','.cpp','.h', '.ui', '.pro']

class Settings:
    parser = argparse.ArgumentParser()

    inputPath = os.path.abspath(os.getcwd())
    outputFile = 'code.txt'
    ignorePaths = []
    ignorePaths_ready = []
    
    extentions_pack = None

    file_extensions = ['.c', '.h', '.py']
    file_codec = "utf-8"

    def init_arguments(self):
        self.parser.add_argument('-i', '--inputPath',       
            help= f'Path with code. Default = {self.inputPath}')
        
        self.parser.add_argument('-o', '--outputFile',      
            help= f'Full file path for output file. Default = {self.outputFile}')
        
        self.parser.add_argument('-e', '--fileExtentions', nargs='*',  
            help= f'A list of file extentions. Ex: \"-e \'.c\' \'.cpp\' \'.h\'\". Default = {self.file_extensions}')
        
        self.parser.add_argument('-p', '--fileExtentionPack', 
            help= f'Predefined list of file extentions. Variants: qtQml, simpleCpp, qt')
        
        self.parser.add_argument('-d', '--ignorePaths', nargs='+',  
            help= f'A list of folders to ingore. Ex: \"-d \"./Debug\"\" Default = {self.ignorePaths}')

        self.parser.add_argument('-c', '--encoding',  
            help= f'File codec. Default = {self.file_codec}')


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

        if args.fileExtentionPack:
            if "qtQml" in args.fileExtentionPack :
                self.file_extensions = FileExtentionPack.qtQml
                self.extentions_pack = args.fileExtentionPack
            elif "simpleCpp" in args.fileExtentionPack:
                self.file_extensions = FileExtentionPack.simpleCpp
                self.extentions_pack = args.fileExtentionPack
            elif "qt" in args.fileExtentionPack:
                self.file_extensions = FileExtentionPack.qt
                self.extentions_pack = args.fileExtentionPack

        if args.encoding:
            self.file_codec = args.encoding

        pass

    def precompile_ignore_paths(self):
        for pathEl in self.ignorePaths:
            if "~" in pathEl:
                path = os.path.expanduser(pathEl)
            else:
                path = os.path.abspath(pathEl)
            self.ignorePaths_ready.append(path)
        pass

    def __init__(self) -> None:
        self.init_arguments()
        self.parse_arguments()
        self.precompile_ignore_paths()
