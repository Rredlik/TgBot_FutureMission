# import aiohttp
import aiosqlite
import pendulum as pendulum

ADMIN_IDS = [351931465]  # 351931465
ADMIN_LINK = ['@skidikis']

# [-1001665320015]  # ачо а ничо
# [-1001681978222]  # OKO NETWORK  https://t.me/okobrand
# [-1001774944385]  # https://t.me/marinailalova
CHANNEL_ID = [-1001681978222]  # OKO NETWORK
CHANNEL_LINK = "https://t.me/okobrand"

first_photo = 'AgACAgIAAxkBAAMLZZCMGI7Jn6siRNDPuNIS7R80hAoAAivZMRu454FIDF3pbybAt20BAAMCAAN5AAM0BA'
self_doc = 'BQACAgIAAxkBAAICP2WTNno-HC3zckWkUDuBOOJh3mB9AAIRSAACUYWYSLIjzZWYhDNBNAQ'
child_doc = 'BQACAgIAAxkBAAICPWWTNmmzQC0kmVGALU0mRzIwX0KEAAIOSAACUYWYSDJbA03GujDxNAQ'


DESCRIPTION = 'СЕМЕЙНЫЙ КОНСУЛЬТАНТ ПО ТАЛАНТАМ'

def set_datetime(record):
    record['extra']['datetime'] = pendulum.now('Asia/Yekaterinburg').strftime('%d-%m-%Y %H:%M:%S')
