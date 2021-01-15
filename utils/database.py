import os
import time
import psycopg2 
import psycopg2.extras
import configparser

import logging

logging.basicConfig(level=logging.DEBUG)
          
class TimeLogHandler(logging.Handler):
    def __init__(self, redirect):
        self.filters = []
        self.lock = None
        self.level = logging.DEBUG
        self.redirect_func = redirect

    def emit(self, record):
        self.redirect_func(record.msg)

    def setLevel(self, level):
        return super().setLevel(level)
                   
class TimeLoggingConnection(psycopg2.extras.LoggingConnection):
    def filter(self, msg, curs):
        return str((time.time() - curs.timestamp) * 1000)

    def cursor(self, *args, **kwargs):
        kwargs.setdefault('cursor_factory', TimeLoggingCursor)
        return psycopg2.extras.LoggingConnection.cursor(self, *args, **kwargs)

class TimeLoggingCursor(psycopg2.extras.LoggingCursor):
    def execute(self, query, vars=None):
        self.timestamp = time.time()
        return psycopg2.extras.LoggingCursor.execute(self, query, vars)

    def callproc(self, procname, vars=None):
        self.timestamp = time.time()
        return psycopg2.extras.LoggingCursor.callproc(self, procname, vars)
        
class DatabaseError(Exception):
	pass

def get_config_values(section = "database"):
	parser = configparser.ConfigParser()
	parser.read(os.path.join(os.path.dirname(__file__) ,"..", "config.ini"))
	config_dict = {}
	if not parser.has_section(section):
		raise DatabaseError("Priovided section could not be found")
	for key, value in parser.items(section):
		config_dict[key] = value	
	return config_dict

db_config = get_config_values()

class Connection:
    def __init__(self):
        self.logger = logging.getLogger("bd2.database.timelogger")
        self.logger.addHandler(TimeLogHandler(self._save_time))
        self.logger.propagate = False
        self.execution_time = 0.0
        self.db_connection = None
        self.db_cursor = None

    def _save_time(self, time_text):
        self.execution_time = float(time_text)
            
    def open(self):
        self.db_connection = psycopg2.connect(
            connection_factory = TimeLoggingConnection, **db_config)
        self.db_connection.initialize(self.logger)
        self.db_connection.set_session(autocommit = True)
        self.db_cursor = self.db_connection.cursor()

    def execute(self, query, params = ()):
        if self.db_cursor is None:
            raise DatabaseError("Connection is not opened")
        self.db_cursor.execute(query, params)
        return self.db_cursor

    def get_last_time(self):
        return self.execution_time
        
    def close(self):
        if self.db_cursor is not None:
            self.db_cursor.close()
            self.db_cursor = None
        if self.db_connection is not None:
            self.db_connection.close()
            self.db_connection = None
    
    def __del__(self):
        self.close()