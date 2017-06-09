import configparser
import time
import os.path

import travian4api

CONFIG_FILE = 'config.cfg'
DEBUG_CONFIG_FILE = 'config.debug.cfg'
SLEEP_SEC = 1


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

    with open(output_file, 'a') as file:
        alliance = account.alliance
        loctime = time.time()
        alliance_name = alliance['name']
        data = 'time: {}, alliance: {}\n'.format(
            loctime,
            alliance_name)
        file.write(data)
        members = alliance['members']
        for member in members:
            username = member['name']
            online = member['online']
            data = 'user: {}, online: {}\n'.format(
                username,
                online)
            file.write(data)
        file.write('\n')


def main():
    while True:
        print('write data')
        write_data()
        time.sleep(SLEEP_SEC)


if __name__ == '__main__':
    config = load_config()

    url = config['USER']['server_url']
    username = config['USER']['username']
    password = config['USER']['password']

    print('Url:', url)
    print('User:', username)

    account = open_account()

    main()

