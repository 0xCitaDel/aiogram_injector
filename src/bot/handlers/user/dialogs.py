from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Jinja

from bot import states as st

from . import handlers
from . import getters


main_window = Window(
        Const('Welcome to Injector Files 📁'),
        Button(
            Const('Download'),
            id='get_document_btn',
            on_click=handlers.input_code
        ),
        state=st.MainSG.start,
    )

input_file_code_window = Window(
        Jinja(
            'Input file name🔑\n\n'
            'Example: some_file.rar\n\n'
        ),
        TextInput(
            id='input_file_field',
            type_factory=handlers.doc_check,
            on_success=handlers.get_document,
            on_error=handlers.get_document_error
        ),
        Button(
            Const('⬅️ Back'),
            id='back_btn',
            on_click=handlers.go_back
        ),
        state=st.MainSG.input_code
    )

get_document_window = Window(
        DynamicMedia('file'),
        Button(
            Const('Скачать еще 🔄'),
            id='repeat_btn',
            on_click=handlers.go_back
        ),
        getter=getters.get_document_getter,
        state=st.MainSG.get_document,
    )

main_dialog = Dialog(
    main_window,
    input_file_code_window,
    get_document_window
)
