import os
import random
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.moe_db

RMS_PHOTOS = [
    "https://stallman.org/photos/rms-working/mid/mid_p1000844.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_0554.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_1755.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3235.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3658.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_4188.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_working-with-the-devil.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_p1000541.jpg",
]

def populate_db():
    print("HERE MUFUCKA %s " % db.moe_db.find().count())
    if not db.moe_db.find().count():
        for moe_url in RMS_PHOTOS:
            moe_doc = {'url': moe_url}
            db.moe_db.insert_one(moe_doc)

populate_db()

@app.route('/')
def moe():
    _items = db.moe_db.find()
    items = [item for item in _items]
    moe = random.choice(items)
    moe_src = moe['url']
    return render_template('moe.html', moe_src=moe_src)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
