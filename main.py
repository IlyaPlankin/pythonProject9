from sqlalchemy import create_engine
engine=create_engine('postgresql+psycopg2://postgres:123456@10.10.101.193:5432/mydb')
connection =engine.connect()
print(engine)