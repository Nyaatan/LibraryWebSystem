import os
import generator

if __name__ == '__main__':
    with open(os.path.join("..", "sql", "example_data.sql"), "w", encoding="utf-8") as file:
        file.write(generator.generate())