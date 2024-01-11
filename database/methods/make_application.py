from datetime import datetime

from database.methods.main import parseOne, updateDB, parseAll


async def get_app_id(user_id):
    application = await parseOne(
        """SELECT id FROM 'applications' where by_user = :user_id""",
        {'user_id': user_id})
    return application


async def check_app(user_id):
    application = await parseOne(
        """SELECT * FROM 'applications' where by_user = :user_id""",
        {'user_id': user_id})
    if application is None:
        await create_new_app(user_id)
        return False
    else:
        return True


async def get_all_completed_apps():
    applications = await parseAll(
        """SELECT * FROM 'applications' where is_complete = 1"""
    )
    return applications


async def get_one_not_in_work():
    applications = await parseAll(
        """SELECT * FROM 'applications' where is_complete = 1 and in_work = 0 limit 1"""
    )
    return applications[0]

async def create_new_app(user_id):
    await updateDB(
        "INSERT INTO 'applications' (by_user, timestamp) VALUES (?, ?)",
        (user_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    )


async def update_app_for_who(user_id, for_who):
    await updateDB(
        "UPDATE 'applications' SET for_who = :for_who WHERE by_user = :user_id",
        {'for_who': for_who, 'user_id': user_id}
    )


async def update_app_theme(user_id, theme):
    await updateDB(
        "UPDATE 'applications' SET theme = :theme WHERE by_user = :user_id",
        {'theme': theme, 'user_id': user_id}
    )


async def update_app_data(user_id, data_type, data):
    await updateDB(
        f"UPDATE 'applications' SET {data_type} = :data WHERE by_user = :user_id",
        {'data': data, 'user_id': user_id}
    )


async def update_app_data_by_id(app_id, data_type, data):
    await updateDB(
        f"UPDATE 'applications' SET {data_type} = :data WHERE id = :app_id",
        {'data': data, 'app_id': app_id}
    )