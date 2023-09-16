from .FilesService import FilesService

from .config import settings

files_service = FilesService(
    base_dir=settings.BASE_DIR, 
    chunk_size=settings.CHUNK_SIZE, 
    folder_length=settings.FOLDER_LENGTH, 
    path_depth=settings.PATH_DEPTH,
    file_name_length=settings.FILE_NAME_LENGTH
)