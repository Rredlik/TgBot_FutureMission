import asyncio
from datetime import datetime

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ChatMemberStatus, CallbackQuery, Update
from loguru import logger

from config import first_photo, CHANNEL_ID, self_doc, child_doc, CHANNEL_LINK
from database.main import connectToDB
from database.methods.user import give_gift, is_have_gift, update_sub_status
from filters.main import IsSubscriber
from handlers.keyboards import *
from utils.methods import send_message


async def __start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    bot: Bot = message.bot

    await is_registered(message=message)
    msg_txt = ("Приветствую вас! Меня зовут Марина Илалова. Я - профориентолог, семейный консультант по талантам."
               "Я разработала авторскую методику выявления природных способностей и превращения их в любимое дело!")

    markup = InlineKeyboardMarkup().add(InlineKeyboardButton('Чем мне это будет полезно?',
                                                             callback_data='first_step'))
    await bot.send_photo(chat_id=message.from_user.id, photo=first_photo, caption=msg_txt, reply_markup=markup)


async def attention_to_sub(query: CallbackQuery, type):
    user_id = query.from_user.id

    have_gift = await is_have_gift(user_id)
    if have_gift:
        return
    if query.data != 'check_sub_status':
        await asyncio.sleep(5 * 60)
    bot: Bot = query.bot
    query_data = query.data
    await send_attention(user_id, bot, query_data)


async def send_attention(user_id, bot: Bot, query_data):
    sub_status = await bot.get_chat_member(chat_id=CHANNEL_ID[0], user_id=user_id)
    print(CHANNEL_ID[0])
    if type == 'self':
        doc = self_doc
    else:
        doc = child_doc
    if sub_status.status == ChatMemberStatus.LEFT:
        await update_sub_status(user_id, 0)
        msg_txt = ("Предлагаю подписаться на мой телеграмм канал, где я рассказываю примеры из практики и истории "
                   "ребят и их родителей. За подписку вы получите полезный подарок\n"
                   f"{CHANNEL_LINK}")
        if query_data == 'check_sub_status':
            msg_txt = ('Не вижу вашей подписки на канал\n'
                       f'{CHANNEL_LINK}')
        markup = (InlineKeyboardMarkup()
                  .add(InlineKeyboardButton('Проверить подписку',
                                            callback_data='check_sub_status')))
        await bot.send_message(user_id, msg_txt, reply_markup=markup)
    else:
        await update_sub_status(user_id, 1)
        msg_txt = "Спасибо за подписку на мой канал! А вот и ваш подарок. Приятного чтения❤️"
        await bot.send_document(user_id, document=doc, caption=msg_txt)
    await give_gift(user_id)

async def is_registered(user_id=None, message: Message = None):
    if message is not None:
        user_id = message.from_user.id
    async with connectToDB() as db:
        try:
            command = await db.execute(
                """SELECT * FROM 'users' WHERE user_id = :user_id""",
                {'user_id': user_id}
            )
            await db.commit()
            values = await command.fetchone()

            if values is None:
                await create_new_user(user_id, message)
                return False
            else:
                return True
        except Exception as er:
            logger.error(f"{er}")
        finally:
            await db.commit()


async def create_new_user(user_id=None, message: Message = None):
    username = 'admin'
    if message is not None:
        user_id = str(message.from_user.id)
        username = message.from_user.username.lower()
        print(username)
    async with connectToDB() as db:
        try:
            await db.execute(
                "INSERT INTO 'users' (user_id, username, reg_date) VALUES (?, ?, ?)",
                (user_id, username, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            )
            logger.info(f"New user registered: {user_id}")
            await db.commit()
        except Exception as er:
            logger.error(f"{er}")
        finally:
            await db.commit()


def _register_register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands=["start"], state='*')

    dp.register_callback_query_handler(attention_to_sub, lambda c: c.data == 'check_sub_status', state='*')
