
import sys, os
import datetime, time

import pymongo, bson


def MongoConn(db_name, coll_name):
    conn = pymongo.Connection()
    if db_name in conn.database_names:
        conn = conn[db_name]
        if coll_name in conn.collection_names():
            return conn
##        else:
##    else:

def MongoInsert(db, coll_name, data):
    coll = db[coll_name]
    ids, err = RecursInsert(coll, data)
    return {'IDs':ids, 'Errors':err}

def RecursInsert(coll, data):
    ids = list()
    ers = list()
    N = len(health_list)
    db_index = math.floor(N/2.0)
    try:
        ids1 = coll.insert(data[:db_index])
        ids2 = coll.insert(data[db_index:])
        err = []
    except:
        err = sys.exc_info()
        if type(err[1]) in [pymongo.errors.AutoReconnect,
                            bson.errors.InvalidDocument]:
            ids1, err_lst1 = recInsert(coll, data[:db_index])
            ids2, err_lst2 = recInsert(coll, data[db_index:])
            err = [err, [err_lst1+err_list2]]
        else:
            ids1 = ids2 = []
            err = [err, 'Fatal']
    ids.append(ids1 + ids2)
    ers.append(err)
    return ids, ers

##for p in posts:
##    p['date'] = time.strftime("%a, %d %b %Y %H:%M:%S +0000", p['date'])
##    db.Wired.insert(p)
