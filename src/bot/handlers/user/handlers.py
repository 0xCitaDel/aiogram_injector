from aiogram import types
from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot import states as st
from db.database import Database
from db.models.file import File


async def go_main(
        callback: CallbackQuery,
        widjet: Button,
        dialog_manager: DialogManager
    ):
    await dialog_manager.switch_to(st.MainSG.start)


async def go_back(
        callback: CallbackQuery,
        widjet: Button,
        dialog_manager: DialogManager
    ):
    await dialog_manager.back()

async def input_code(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    await manager.switch_to(st.MainSG.input_code)

def doc_check(text: str):
        return text

async def get_document(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        text: str
    ):
    db = manager.middleware_data['db']
    file = (await db.file.get_by_where(File.file_code == text)).one_or_none()
    if file:    
        manager.dialog_data['file'] = file.file_name
        await manager.switch_to(st.MainSG.get_document)
    else:
        await manager.switch_to(st.MainSG.start)


async def get_document_error(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        error: ValueError
    ):
    await manager.switch_to(st.MainSG.start)
