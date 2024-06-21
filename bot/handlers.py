import json
from datetime import datetime

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.states import IncludeDataState
from db import get_list_dates
from services import get_payments

router = Router()

ERROR_MSG = (
    'Невалидный запрос. Пример запроса: {"dt_from": "2022-09-01T00:00:00", '
    '"dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
)
VALID_KEYS = ['dt_from', 'dt_upto', 'group_type']


@router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    await state.set_state(IncludeDataState.include_data)
    await message.answer(f'Hi {message.from_user.full_name}!')


@router.message(IncludeDataState.include_data)
async def echo_handler(message: types.Message):
    msg = message.text

    try:
        msg = json.loads(msg)
        isinstance(msg, dict) and all(key in msg for key in VALID_KEYS)
    except Exception as e:
        await message.answer(ERROR_MSG)
        print(e)

    dt_from = datetime.fromisoformat(msg.get('dt_from'))
    dt_upto = datetime.fromisoformat(msg.get('dt_upto'))
    group_type = msg.get('group_type')

    db_data = await get_list_dates(dt_from, dt_upto)
    payments_to_period = get_payments(db_data, dt_from, dt_upto, group_type)

    await message.reply(text=json.dumps(payments_to_period))
