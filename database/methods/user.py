from database.methods.main import parseAll, parseOne, updateDB


async def parseAllUsers():
    allUsers = await parseAll("SELECT user_id FROM 'users'")
    return allUsers


async def parseAllAdmins():
    allUsers = await parseAll("SELECT user_id FROM 'users' where is_admin = 1")
    return allUsers


async def is_subscriber(user_id):
    have_gift = await parseOne("SELECT is_subscriber FROM 'users' where user_id = :user_id",
                              {"user_id": user_id})
    return int(have_gift[0])


async def update_sub_status(user_id, status):
    await updateDB(
        "UPDATE 'users' SET is_subscriber = :status WHERE user_id = :user_id",
        {'user_id': user_id, 'status': status}
    )


async def isAdmin(user_id):
    is_admin = await parseOne("SELECT is_admin FROM 'users' where user_id = :user_id",
                              {"user_id": user_id})
    return int(is_admin[0])


async def make_new_admin(user_id):
    await updateDB(
        "UPDATE 'users' SET is_admin = 1 WHERE user_id = :user_id",
        {'user_id': user_id}
    )


async def give_gift(user_id):
    await updateDB(
        "UPDATE 'users' SET get_gift = 1 WHERE user_id = :user_id",
        {'user_id': user_id}
    )


async def is_have_gift(user_id):
    have_gift = await parseOne("SELECT get_gift FROM 'users' where user_id = :user_id",
                              {"user_id": user_id})
    return int(have_gift[0])
