from threading import Lock

bot_file_lock = Lock()

def get_file_lock():
    return bot_file_lock