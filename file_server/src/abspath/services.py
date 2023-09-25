import os

from fastapi import UploadFile
from fastapi import BackgroundTasks
import aiofiles

from ..rndpath.utils import random_str

class RPathService:
    @classmethod
    async def save_file(
            cls,
            file: UploadFile,
            run_in_background: bool = True,
            background_tasks: BackgroundTasks = None,
        ) -> None:

        path = cls.generate_random_path(file.filename.split('.')[-1])
        while os.path.isfile(cls.BASE_DIR+path):
            path = cls.generate_random_path(file.filename.split('.')[-1])
        os.makedirs(os.path.dirname(cls.BASE_DIR+path), exist_ok=True)

        if run_in_background:
            background_tasks.add_task(
                cls.save_file_in_fs, path, file
            )
        else:
            cls.save_file_in_fs(path, file)
        return path

    @classmethod
    async def save_file_in_fs(cls, path:str, file: UploadFile) -> None:
        async with aiofiles.open(cls.BASE_DIR+path, 'wb') as out_file:
            while chunk := await file.read(cls.CHUNK_SIZE):
                await out_file.write(chunk)

    @classmethod
    def generate_random_path(
            cls,
            format:str
        ) -> str:

        path = ''
        for depth in range(cls.PATH_DEPTH):
            path += random_str(cls.FOLDER_LENGTH)+'/'
        path += random_str(cls.FILE_NAME_LENGTH)+'.'+format
        return path # ZmfQcrFxxdhXnuYyec.png -> Zm/fQ/cr/FxxdhXnuYyec.png

    @classmethod
    def from_link_to_path(cls, link: str) -> str:
        path = []
        for i in range(cls.PATH_DEPTH):
            path.append(link[0:cls.FOLDER_LENGTH])
            link = link[cls.FOLDER_LENGTH:]
        path.append(link)
        return cls.BASE_DIR+'/'.join(path)

    @staticmethod
    def from_path_to_link(cls, path: str) -> str:
        return path.replace('/','')