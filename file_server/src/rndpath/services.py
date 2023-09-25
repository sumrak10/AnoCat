import os

from fastapi import UploadFile
from fastapi import BackgroundTasks
import aiofiles

from .utils import random_str
from ..utils.input_file import URLInputFile

from ..config import files_settings, bot_setttings


class RndPathService:
    BASE_DIR = files_settings.BASE_DIR+'rndpath/'
    @classmethod
    async def save_file_from_bytes(
        cls,
        file: UploadFile,
        background_tasks: BackgroundTasks = None,
    ) -> str:

        path = cls.generate_random_path(
            os.path.splitext(file.filename)
        )

        cls.save_file_in_fs(path, file, background_tasks)

        return path.replace('/','')
    
    @classmethod
    async def save_file_from_telegram_api(
        cls, 
        file_path: str,
        ext: str,
        background_tasks: BackgroundTasks = None,
    ) -> str:
        
        path = cls.generate_random_path(ext)

        file = URLInputFile(
            url=f"https://api.telegram.org/file/bot{bot_setttings.TOKEN}/{file_path}"
        )

        cls.save_file_in_fs(path, file, background_tasks)

        return path.replace('/','')

    @classmethod
    async def save_file_in_fs(cls, path, file, background_tasks: BackgroundTasks) -> None:
        if background_tasks is not None:
            background_tasks.add_task(
                cls._save_file_in_fs, path, file
            )
        else:
            cls._save_file_in_fs(path, file)

    @classmethod
    async def _save_file_in_fs(cls, path:str, file: UploadFile) -> None:
        async with aiofiles.open(cls.BASE_DIR+path, 'wb') as out_file:
            while chunk := await file.read(files_settings.CHUNK_SIZE):
                await out_file.write(chunk)


    @classmethod
    def generate_random_path(
        cls,
        ext: str
    ) -> str:
        path = cls._generate_random_path()
        while os.path.isfile(cls.BASE_DIR+path):
            path = cls._generate_random_path()
        path + ext

        os.makedirs(os.path.dirname(cls.BASE_DIR+path), exist_ok=True)

        return path

    @classmethod
    def _generate_random_path(
        cls
    ) -> str:

        path = ''
        for depth in range(files_settings.PATH_DEPTH):
            path += random_str(files_settings.FOLDER_LENGTH)+'/'
        path += random_str(files_settings.FILE_NAME_LENGTH)
        
        return path # ZmfQcrFxxdhXnuYyec.png -> Zm/fQ/cr/FxxdhXnuYyec.png

    @classmethod
    def from_link_to_path(cls, link: str) -> str:
        path = []
        for i in range(files_settings.PATH_DEPTH):
            path.append(link[0:files_settings.FOLDER_LENGTH])
            link = link[files_settings.FOLDER_LENGTH:]
        path.append(link)
        path = cls.BASE_DIR+'/'.join(path)
        if not os.path.isfile(path):
            raise FileNotFoundError()
        return path