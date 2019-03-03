from sqlalchemy import create_engine
import pandas as pd


class DB:
    def __init__(self):
        url = 'mysql+mysqldb://alvaropc@localhost/instabot'
        engine = create_engine(url,)
        conn = engine.connect()
        table = pd.read_sql("select * from token", conn)
        self.instabot_token = table[table["platform"] == "instabot"]["token"].iloc[0]


