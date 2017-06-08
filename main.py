import configparser
import os.path

import travian4api

CONFIG_FILE = 'config.cfg'
DEBUG_CONFIG_FILE = 'config.debug.cfg'


def load_config():
    config = configparser.ConfigParser()

    if os.path.exists(DEBUG_CONFIG_FILE):
        config.read(DEBUG_CONFIG_FILE)
        print('Debug mode')
    else:
        config.read(CONFIG_FILE)

    return config


def open_account():
    account = travian4api.Account(url, username, password)

    if account.login.login():
        print('Login success!')
    else:
        print('Login failed!')

    return account


def write_data():
    output_file = config['OUTPUT']['file_path']

    with open(output_file, 'w') as file:
        for v in account.villages:
            file.write(v.name)


if __name__ == '__main__':
    config = load_config()

    url = config['USER']['server_url']
    username = config['USER']['username']
    password = config['USER']['password']

    print('Url:', url)
    print('User:', username)

    account = open_account()

    write_data()

