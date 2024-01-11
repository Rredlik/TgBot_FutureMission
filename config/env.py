import os
from abc import ABC
from typing import Final
from environs import Env


class Env(ABC):
    env = Env()
    env.read_env()
    # BOT_TOKEN: Final = os.environ.get('BOT_TOKEN', 'define me!')
    BOT_TOKEN: Final = env.str("BOT_TOKEN")  # Забираем значение типа str
    # ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
    # IP = env.str("ip")  # Тоже str, но для айпи адреса хоста