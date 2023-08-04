from os.path import join as join_path

from configs.constants import BASE_URL


def write_user_id(user_id):
    with open(join_path(BASE_URL,'db','users.txt'), 'r') as file:
        users = file.read().split(',')

    if str(user_id) not in users:
        with open(join_path(BASE_URL, 'db', 'users.txt'), 'a') as file:
            users = file.write(str(user_id)+",")


