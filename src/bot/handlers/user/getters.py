from aiogram.types import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from db.database import Database
from services.injector import Injector

from . import constants as cnst


async def get_document_getter(dialog_manager: DialogManager, db: Database, **kwargs):
    user_id = dialog_manager.event.from_user.id
    file_name = dialog_manager.dialog_data['file']
    some = Injector(file_name, '#!' + str(user_id))
    some_file = some.inject_data()
    
    file = MediaAttachment(ContentType.DOCUMENT, path=some_file)
    return {
        'file': file
    }
