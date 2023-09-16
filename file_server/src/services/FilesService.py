import os

from fastapi import UploadFile
from fastapi import BackgroundTasks
import aiofiles

from .utils import random_str

class FilesService:
    def __init__(self, 
            base_dir: str, 
            chunk_size: int, 
            folder_length: int, 
            path_depth: int,
            file_name_length: int
        ) -> None:

        self.BASE_DIR = base_dir
        self.CHUNK_SIZE = chunk_size
        self.FOLDER_LENGTH = folder_length
        self.PATH_DEPTH = path_depth
        self.FILE_NAME_LENGTH = file_name_length



    async def save_file(
            self,
            file: UploadFile,
            run_in_background: bool = True,
            background_tasks: BackgroundTasks = None,
        ) -> None:

        path = self.generate_random_path(file.filename.split('.')[-1])
        while os.path.isfile(self.BASE_DIR+path):
            path = self.generate_random_path(file.filename.split('.')[-1])
        os.makedirs(os.path.dirname(self.BASE_DIR+path), exist_ok=True)

        if run_in_background:
            background_tasks.add_task(
                self.save_file_in_fs, path, file
            )
        else:
            self.save_file_in_fs(path, file)
        return self.from_path_to_link(path)

    async def save_file_in_fs(self, path:str, file: UploadFile) -> None:
        async with aiofiles.open(self.BASE_DIR+path, 'wb') as out_file:
            while chunk := await file.read(self.CHUNK_SIZE):
                await out_file.write(chunk)

    def generate_random_path(
            self,
            format:str
        ) -> str:

        path = ''
        for depth in range(self.PATH_DEPTH):
            path += random_str(self.FOLDER_LENGTH)+'/'
        path += random_str(self.FILE_NAME_LENGTH)+'.'+format
        return path # ZmfQcrFxxdhXnuYyec.png -> Zm/fQ/cr/FxxdhXnuYyec.png

    def from_link_to_path(self, link: str) -> str:
        path = []
        for i in range(self.PATH_DEPTH):
            path.append(link[0:self.FOLDER_LENGTH])
            link = link[self.FOLDER_LENGTH:]
        path.append(link)
        return self.BASE_DIR+'/'.join(path)

    def from_path_to_link(self, path: str) -> str:
        return path.replace('/','')