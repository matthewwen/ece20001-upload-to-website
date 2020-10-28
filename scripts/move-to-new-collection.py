import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
import os


def set_env(env):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../firebase-key.json" if env == "prod" else \
        "../firebase-key-test.json"


set_env("dev")
db = firestore.Client()


def get_data_by_ref(name):
    ref = db.collection(name)
    return [(i.id, i.to_dict(),) for i in ref.get()]


def set_data_by_ref(name, items):
    ref = db.collection(name)
    for k, v in items:
        ref.document(k).set(v)


# pages_data = get_data_by_ref("ece20001\pages")
# set_data_by_ref("ece20001_pages", pages_data)
# print(pages_data)
#
# practice_data = get_data_by_ref("ece20001\practice")
# set_data_by_ref("ece20001_practice", practice_data)
# print(practice_data)

fix_collection = [
    ("ece20001\lessons", "ece20001_lessons",),
    ("ece20001\pages", "ece20001_pages",),
    ("ece20001\practice", "ece20001_practice",)
]

for k, v in fix_collection:
    data = get_data_by_ref(k)
    set_data_by_ref(v, data)
