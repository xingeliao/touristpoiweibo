from flask import Flask, render_template
from datetime import date

app = Flask(__name__)
import create_db

@app.route('/')
def index():
    today = date.today()
    date = today.strftime("%y-%m")
    return create_map(date)

@app.route('/map/<string:date>')
def create_map(date):
    database = "map_db.db"
    conn = create_db.create_connection(database)
    cur = conn.cursor()

    sql_select_all_date = """ SELECT DISTINCT(post_date) AS d FROM post_ocurrences ocu ORDER BY post_date
                                 ; """
    cur.execute(sql_select_all_date)
    date_options = cur.fetchall()

    datesplit = date.split(',')
    date2 = ['\"' + s + '\"' for s in datesplit]
    date2 = ",".join(date2)

    sql_select_point_frequency = """ SELECT loc.latitude, loc.longitude, SUM(frecuency), loc.location
                                    FROM locations loc
                                    LEFT JOIN post_ocurrences ocu
                                    ON loc.id = ocu.location_id
                                    WHERE ocu.post_date IN (""" + date2 + """)
                                    GROUP BY loc.id
                                ; """
    cur.execute(sql_select_point_frequency)


    points_data = cur.fetchall()
    return render_template('map.html', date=date, points_data=points_data, date_options=date_options)

@app.route('/maprange/<string:datefrom>/<string:dateto>')
def create_maprange(datefrom, dateto):
    database = "map_db.db"
    conn = create_db.create_connection(database)
    cur = conn.cursor()

    sql_select_all_date = """ SELECT DISTINCT(post_date) AS d FROM post_ocurrences ocu ORDER BY post_date
                                 ; """
    cur.execute(sql_select_all_date)
    date_options = cur.fetchall()

    #datesplit = date.split(',')
    datefrom = '\"' + datefrom + '\"'
    dateto = '\"' + dateto + '\"'
    #date2 = ",".join(date2)

    sql_select_point_frequency = """ SELECT loc.latitude, loc.longitude, SUM(frecuency), loc.location
                                    FROM locations loc
                                    LEFT JOIN post_ocurrences ocu
                                    ON loc.id = ocu.location_id
                                    WHERE ocu.post_date BETWEEN """ + datefrom + """ AND """ + dateto + """
                                    GROUP BY loc.id
                                ; """
    cur.execute(sql_select_point_frequency)
    points_data = cur.fetchall()
    return render_template('map.html', points_data=points_data, date_options=date_options)


@app.route('/map_provincia/<string:date_provincia>')
def create_map_provincia(date_provincia):
    database = "map_db.db"
    conn = create_db.create_connection(database)
    cur = conn.cursor()
    sql_select_all_date = """ SELECT DISTINCT(post_date) AS d FROM post_ocurrences_provincia ocu ORDER BY post_date
                                 ; """
    cur.execute(sql_select_all_date)
    date_options = cur.fetchall()
    datesplit = date_provincia.split(',')
    date2 = ['\"' + s + '\"' for s in datesplit]
    date2 = ",".join(date2)
    sql_select_point_frequency = """ SELECT loc.latitude, loc.longitude, SUM(frecuency), loc.location
                                    FROM locations_provincia loc
                                    LEFT JOIN post_ocurrences_provincia ocu
                                    ON loc.id = ocu.location_id
                                    WHERE ocu.post_date IN (""" + date2 + """)
                                    GROUP BY loc.id
                                ; """
    cur.execute(sql_select_point_frequency)
    points_data_provincia = cur.fetchall()
    return render_template('map.html', date=date_provincia, points_data=points_data_provincia, date_options=date_options)

@app.route('/maprange_provincia/<string:datefrom_provincia>/<string:dateto_provincia>')
def create_maprange_provincia(datefrom_provincia, dateto_provincia):
    database = "map_db.db"
    conn = create_db.create_connection(database)
    cur = conn.cursor()
    sql_select_all_date = """ SELECT DISTINCT(post_date) AS d FROM post_ocurrences_provincia ocu ORDER BY post_date
                                 ; """
    cur.execute(sql_select_all_date)
    date_options = cur.fetchall()
    datefrom_provincia = '\"' + datefrom_provincia + '\"'
    dateto_provincia = '\"' + dateto_provincia + '\"'
    sql_select_point_frequency = """ SELECT loc.latitude, loc.longitude, SUM(frecuency), loc.location
                                    FROM locations_provincia loc
                                    LEFT JOIN post_ocurrences_provincia ocu
                                    ON loc.id = ocu.location_id
                                    WHERE ocu.post_date BETWEEN """ + datefrom_provincia + """ AND """ + dateto_provincia + """
                                    GROUP BY loc.id
                                ; """
    cur.execute(sql_select_point_frequency)
    points_data_provincia = cur.fetchall()
    return render_template('map.html', points_data=points_data_provincia, date_options=date_options)
