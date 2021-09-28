import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)

def drop_table(conn, table_name):
    c = conn.cursor()
    c.execute("DROP TABLE " + table_name + ";")

def main():
    database = "map_db.db"
    sql_create_locationdata_table = """ CREATE TABLE IF NOT EXISTS locations (
                                        id integer PRIMARY KEY,
                                        location text NOT NULL,
                                        latitude text NOT NULL,
                                        longitude text NOT NULL
                                    ); """
    sql_create_frecuencydata_table = """ CREATE TABLE IF NOT EXISTS post_ocurrences (
                                        id integer PRIMARY KEY,
                                        location_id integer,
                                        post_date text,
                                        frecuency integer,
                                        FOREIGN KEY (location_id) REFERENCES locations (id)
                                    ); """
    sql_create_locationdata_table_provincia = """ CREATE TABLE IF NOT EXISTS locations_provincia (
                                        id integer PRIMARY KEY,
                                        location text NOT NULL,
                                        latitude text NOT NULL,
                                        longitude text NOT NULL
                                    ); """
    sql_create_frecuencydata_table_provincia = """ CREATE TABLE IF NOT EXISTS post_ocurrences_provincia (
                                        id integer PRIMARY KEY,
                                        location_id integer,
                                        post_date text,
                                        frecuency integer,
                                        FOREIGN KEY (location_id) REFERENCES locations (id)
                                    ); """
    conn = create_connection(database)
    #drop_table(conn, 'locations')
    #drop_table(conn, 'post_ocurrences')
    #drop_table(conn, 'locations_provincia')
    #drop_table(conn, 'post_ocurrences_provincia')
    create_table(conn, sql_create_locationdata_table)
    create_table(conn, sql_create_frecuencydata_table)
    create_table(conn, sql_create_locationdata_table_provincia)
    create_table(conn, sql_create_frecuencydata_table_provincia)


if __name__ == '__main__':
    main()
