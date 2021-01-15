import database
import perfmeter

if __name__ == '__main__':
    connection = database.Connection()
    connection.open()
    perfmeter.measure_performance(connection)
    connection.close()