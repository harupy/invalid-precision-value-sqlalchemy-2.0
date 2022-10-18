import sqlalchemy as sa

import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, VARCHAR

print(sa.__version__)

engine = create_engine(os.getenv("DB_URI"), echo=True)
meta = MetaData()

students = Table(
    "students",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(5000)),
)
meta.create_all(engine)

# Insert a row to the table
with  engine.connect() as conn:
    conn.execute(students.insert().values(name="x" * 5000))

print("SUCCESS")