import os
import database

if __name__ == '__main__':
	database.open()
	with open(os.path.join("..", "sql", "create_schema.sql"), "r", encoding="utf-8") as file:
		database.execute(file.read())
	database.close()
