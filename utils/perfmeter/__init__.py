import os
import time
import yaml

drop_index_sql = 'DROP INDEX IF EXISTS {};'

def measure_performance(db_connection):
    measurement_dict = {}
    with open(os.path.join(os.path.dirname(__file__), "measure_data.yaml"), "r") as file:
        measurement_dict = yaml.load(file, Loader = yaml.Loader)
    measure_indexes_peformance(db_connection, measurement_dict)

def measure_indexes_peformance(db_connection, measurement_dict):
    for entry_name, entry_data in measurement_dict.items():
        index_name = entry_name + "_index"
        create_sql = entry_data["create_sql"].format(index_name)
        test_sql = entry_data["test_sql"]
        drop_sql = drop_index_sql.format(index_name)
        db_connection.execute(drop_sql)
        print("Testing {}..".format(index_name))
        print("without query time: {} ms".format(measure_query_time(db_connection, test_sql)))
        db_connection.execute(create_sql)
        print("with query time: {} ms".format(measure_query_time(db_connection, test_sql)))
        print()

def measure_query_time(db_connection, sql_query, repeat_count = 10000):
    total_time = 0.0
    for _ in range(0, repeat_count):
        start_time = time.time()
        m = list(db_connection.execute(sql_query).fetchall())
        v2 = db_connection.get_last_time()
        v1 = (time.time() - start_time) * 1000
        total_time = total_time + v1
    total_time = total_time / repeat_count
    return total_time
