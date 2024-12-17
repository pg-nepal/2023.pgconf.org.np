import os
import sqlalchemy as sa
from db.base import Base
from db.proposals import *

url = sa.URL.create(
    "postgresql",
    username="postgres",
    password="1234",
    host="localhost",
    database="pgconf",
)

engine = sa.create_engine(
    url=url,
    future=True,
    echo=True,
)

Session = sa.orm.sessionmaker(bind=engine)

Base.metadata.create_all(engine)

print("Tables created successfully")
print(Base.metadata.tables.keys())


inspector = sa.inspect(engine)
tables = inspector.get_table_names()
print("Tables in the database:", tables)

print("Tables in base metadata:", Base.metadata.tables.keys())
# Show columns for a specific table (e.g., 'proposals')
table_name = 'proposals'
columns = inspector.get_columns(table_name)

# Print column details
print(f"Columns in the '{table_name}' table:")
for column in columns:
    print(f"Column name: {column['name']}, Type: {column['type']}, Nullable: {column['nullable']}, Default: {column.get('default')}")