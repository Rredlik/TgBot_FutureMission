import os
from abc import ABC
from typing import Final
from environs import Env


class Env(ABC):
    env = Env()
    env.read_env()
    BOT_TOKEN: Final = env.str("BOT_TOKEN")  # Забираем значение типа str
    first_photo = env.str('FIRST_PHOTO')
    file_self = env.str('FILE_SELF')
    file_child = env.str('FILE_CHILD')
    channel_id = env.list('CHANNEL_ID') # Список каналов, записывается через запятую
    channel_link = env.str('CHANNEL_LINK')
    ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
    # IP = env.str("ip")  # Тоже str, но для айпи адреса хоста