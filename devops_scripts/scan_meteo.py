import psycopg2
import json
import pathlib
from getpass import getpass

def pgsql_new_connection(login, password, hostname, db = "postgres"):
    try:
        if(db != 'postgres'):
            print("Connection with server: {0}, database: {1}".format(hostname, db))
        connection = psycopg2.connect(user = login, password = password, host = hostname, database = db, connect_timeout =  10 )
        cursor = connection.cursor()
        return 0, cursor
    except (Exception, psycopg2.Error) as error:
        return 2, error

def pgsql_closeconnection(mycursor):
    mycursor.close()

def pgsql_fetchquery(mycursor,query_to_exec):
    try:
        mycursor.execute(query_to_exec)
    except (Exception, psycopg2.Error) as Error:
        return Error.pgcode
    return mycursor.fetchall()

if __name__ == "__main__":
    login = "pdepretz"
    print('Please enter the password (login: {0}): '.format(login))
    password = getpass()
    folder_path = "/home/users/pdepretz/Documents/Python/"
    results = {}

    with open("{0}/server_list".format(folder_path),"r") as server_list:
        hostnames = server_list.readlines()

    for hostname in [ hostname.strip() for hostname in hostnames if not hostname.startswith("#") ]:
        status_default, cursor_default = pgsql_new_connection(login, password, hostname)
        if(status_default == 0):
            results[hostname] = {}
            query = "SELECT datname FROM pg_database WHERE datname NOT IN ('powa','postgres','template0','template1');"
            list_dbs = pgsql_fetchquery(cursor_default, query)
            pgsql_closeconnection(cursor_default)
            for row in list_dbs:
                db = row[0]
                status_db, cursor_db = pgsql_new_connection(login, password, hostname, db)
                if(status_db == 0):
                    results[hostname][db] = {}
                    #DBSIZE
                    query = "SELECT pg_size_pretty(pg_database_size('{0}'));".format(db)
                    db_size = pgsql_fetchquery(cursor_db, query)
                    results[hostname][db]["db_size"] = db_size[0][0]

                    #METEO RELEASE
                    query = "SELECT MAX(RELEASE) as pg96_ready FROM meteo.release where release != '_no_ref';"
                    pg96_ready = pgsql_fetchquery(cursor_db, query)
                    pgsql_closeconnection(cursor_db)

                    if(pg96_ready == '42P01'):
                        results[hostname][db]["pg96_ready"] = False
                        results[hostname][db]["error"] = "meteo schema is missing"
                    elif(isinstance(pg96_ready, list) and pg96_ready[0][0] == None):
                        results[hostname][db]["pg96_ready"] = False
                        results[hostname][db]["error"] = "meteo.release is empty"
                    elif(isinstance(pg96_ready, list) and pg96_ready[0][0] != None):
                        pg96_lastrelease = pg96_ready[0][0]
                        if('-' in pg96_lastrelease):
                            pg96_lastrelease = pg96_ready[0][0].split("-")[0]
                        pg96_lastrelease = int(eval(pg96_lastrelease.replace('.','')))
                        if(db.startswith('axis') and pg96_lastrelease >= 300):
                            results[hostname][db]["pg96_ready"] = True
                            results[hostname][db]["last_version"] = pg96_ready[0][0]
                        elif(db.startswith('axis') and pg96_lastrelease < 300):
                            results[hostname][db]["pg96_ready"] = False
                            results[hostname][db]["last_version"] = pg96_ready[0][0]
                            results[hostname][db]["error"] = "meteo.release is too old for Axis database ({0} < 3.0.0)".format(pg96_ready[0][0])
                        elif(pg96_lastrelease < 270):
                            results[hostname][db]["pg96_ready"] = False
                            results[hostname][db]["last_version"] = pg96_ready[0][0]
                            results[hostname][db]["error"] = "meteo.release is too old for none Axis database ({0} < 2.7.0)".format(pg96_ready[0][0])  
                        elif(pg96_lastrelease >= 270):
                            results[hostname][db]["pg96_ready"] = True
                            results[hostname][db]["last_version"] = pg96_ready[0][0]
                    else:
                        results[hostname][db]["pg96_ready"] = False
                        results[hostname][db]["error"] = "unknown error ({0})".format(pg96_ready)
        elif(status_default == 2):
            print(" Connection with server: {0}\n!!! error while connecting to PostgreSQL, error {1}".format(hostname,cursor_default))
    
    with open("{0}/results.json".format(folder_path), "w", encoding='utf-8') as results_json:
        json.dump(results, results_json, ensure_ascii=False, indent=4)
