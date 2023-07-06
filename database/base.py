from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mssql+pyodbc://DESKTOP-2NFCDE2/BCST?driver=ODBC Driver 11 for SQL Server')
engine = create_engine('mysql+pymysql://root:root@localhost:3306/ccd')

meta = MetaData()
session = sessionmaker(bind=engine)

autme_user = Table("autme_user", meta,
                   Column("id", Integer, primary_key=True),
                   Column("login", String(100), nullable=False),
                   Column("password", String(250), nullable=False),
                   Column("date_create", String(40)),
                   )

def base_connect():
    meta.create_all(engine)
    connect = engine.connect()
    print("base connect")
    return connect