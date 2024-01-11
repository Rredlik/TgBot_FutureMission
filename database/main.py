import aiosqlite
from loguru import logger

PATH_DATABASE = "main.db"


def connectToDB():
    connection = aiosqlite.connect(PATH_DATABASE)
    return connection


async def create_db():
    async with connectToDB() as db:

        try:
            users = await (await db.execute("PRAGMA table_info(users)")).fetchall()
            applications = await (await db.execute("PRAGMA table_info(applications)")).fetchall()
            config = await (await db.execute("PRAGMA table_info(config)")).fetchall()

            if len(users) == 7:
                logger.success("DB was found (1/3)")
            else:
                logger.warning("DB was not found (1/3) | Creating...")
                await db.execute('create table users('
                                 'user_id  TEXT not null primary key unique,'
                                 'username text default 0,'
                                 'is_admin BOOLEAN default 0,'
                                 'is_active BOOLEAN default 1,'
                                 'is_subscriber BOOLEAN default 0,'
                                 'get_gift BOOLEAN default 0,'
                                 'reg_date INTEGER not null)')
                logger.success("DB was create (1/3)")

            if len(applications) == 10:
                logger.success("DB was found (2/3)")
            else:
                logger.warning("DB was not found (2/3) | Creating...")
                await db.execute('create table applications('
                                 'id          INTEGER not null primary key autoincrement unique,'
                                 'by_user     TEXT not null,'
                                 'for_who     TEXT,'
                                 'theme       TEXT,'
                                 'user_name   TEXT,'
                                 'user_number TEXT,'
                                 'user_email  TEXT,'
                                 'timestamp DATETIME not null,'
                                 'is_complete BOOLEAN default 0,'
                                 'in_work BOOLEAN default 0)')
                logger.success("DB was create (2/3)")

            if len(config) == 2:
                logger.success("DB was found (3/3)")
            else:
                logger.warning("DB was not found (3/3) | Creating...")
                await db.execute('create table config('
                                 'setting TEXT,'
                                 'value   TEXT)')
                logger.success("DB was create (3/3)")

        except Exception as er:
            logger.error(f"{er}")
        finally:
            await db.commit()
