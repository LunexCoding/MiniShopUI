import os
import shutil
from pathlib import Path
import base64
from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)


class _FileSystem:
    def __init__(self):
        pass

    @staticmethod
    def getFilename(path, suffix=False):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_dir():
            raise PathExistsAsDirectoryException(path)
        return path.stem if suffix is False else path.name

    @staticmethod
    def isEmpty(path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if not path.is_dir():
            raise IsNotDirectoryException(path)
        if not len(os.listdir(path)) == 0:
            raise IsNotEmptyException(path)
        return True

    @staticmethod
    def makeDir(path, recreate=False):
        path = Path(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        if path.exists() and recreate is False:
            raise PathExistsException(path)
        path.mkdir(exist_ok=recreate)
        return True

    @staticmethod
    def remove(path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_dir():
            raise PathExistsAsDirectoryException(path)
        path.unlink()
        return True

    @classmethod
    def removeDir(cls, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        if not cls.isEmpty(path):
            raise IsNotEmptyException(path)
        path.rmdir()
        return True

    @classmethod
    def removeTree(cls, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        for child in path.glob("*"):
            if child.is_file():
                child.unlink()
            else:
                cls.removeTree(child)
        path.rmdir()
        return True

    @staticmethod
    def exists(path):
        return Path(path).exists()

    @staticmethod
    def copyFile(path, newPath):
        path = Path(path)
        newPath = Path(newPath)
        if not path.exists():
            raise PathNotFoundException(path)
        if newPath.exists():
            raise PathExistsException(newPath)
        if path.exists() and path.is_dir():
            raise PathExistsAsDirectoryException(path)
        shutil.copy(path, newPath)

    @staticmethod
    def __convertBinaryDataToImage(blob):
        with open("imageToSave.png", "wb") as image:
            image.write(base64.decodebytes(blob))

    @staticmethod
    def __convertImageToBinaryData(path):
        with open(path, 'rb') as file:
            binaryData = file.read()
        return binaryData


fileSystem = _FileSystem()
