# In-memory storage
storage = {}


def store_data(data):
    global storage
    storage = data


def get_data():
    return storage
