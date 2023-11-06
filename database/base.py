from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://user_api:aI7vG6bE9v@web.hosting-minecraft.pro/ccd')

meta = MetaData()
session = sessionmaker(bind=engine)

autme_user = Table("autme_user", meta,
                   Column("id", Integer, primary_key=True),
                   Column("login", String(100), nullable=False),
                   Column("password", String(250), nullable=False),
                   Column("role", String(25), nullable=False),
                   Column("date_create", String(40)),
                   )

account = Table("account", meta,
                Column("id", Integer, primary_key=True),
                Column("login", String(100), nullable=False),
                Column("password", String(250), nullable=False),
                Column("access_modifier", String(25), nullable=False),
                Column("date_attachments", String(40), nullable=False),
                Column("date_parish", String(40), nullable=False),
                Column("cach", Integer, nullable=True, default=0),
                )

history_account = Table("history", meta,
                        Column("id", Integer, primary_key=True),
                        Column("login", String(100), nullable=False),
                        Column("id_user", String(40), nullable=False),
                        Column("success", String(250), default="В процессе"),
                        Column("date_parish", String(40), nullable=False),
                        Column("time_parish", String(40), nullable=False),
                        Column("date_expiration", String(40)),
                        Column("type_operation", String(40))
                        )


def base_connect():
    meta.create_all(engine)
    connect = engine.connect()
    return connect
