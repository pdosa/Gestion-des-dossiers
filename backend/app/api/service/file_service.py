import shutil
from fastapi import File,UploadFile


def upload_file(file:UploadFile=File()):
    with open(f"uploads/{file.filename}","wb") as file_upload:
        shutil.copyfileobj(file.file,file_upload)
    return {
        "file name":file.filename,
        "element":file.content_type
    }