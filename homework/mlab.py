import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds157574.mlab.com:57574/bikes

host = "ds157574.mlab.com"
port = 57574
db_name = "bikes"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())