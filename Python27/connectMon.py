"""
Actual connection handles for Mongo; used by dbconn
to create the connections.  
"""
import sys, os
import datetime, time
import math

import pymongo, bson

class MongoConn:
    """
    General handle for making a connection to a local Mongo database
    from within python; utilizes pymongo package;
    """
    def __init__(self, args, **dargs):
        self._store = dict()
        if 'db_name' in args.keys():
            db_name = args['db_name']
            coll_name = args['coll_name'] if 'coll_name' in args.keys() else ''
            conn = pymongo.Connection()
            if db_name in conn.database_names():
                conn = conn[db_name]
                if coll_name in conn.collection_names():
                    self.conn = conn[coll_name]
                elif not coll_nam:
                    self.conn = conn
                else:
                    print('Failure to make connections...')
        ##        else:
        ##    else:


    def MongoInsert(self, data):
        try:
            ids = self.conn.insert(data)
            self._store['lastIDs'] = ids
        except:
            print("Breaking data into parts")
            self._store['lastIDs'], self._store['lastErr']\
                                    = self.RecursInsert(data)

    ## something wrong with this portion...figure it out..
    def RecursInsert(self, data):
        ids = list()
        ers = list()
        N = len(data)
        print(N)
        db_index = math.floor(N/2.0)
        try:
            ids1 = self.conn.insert(data[:db_index])
            ids2 = self.conn.insert(data[db_index:])
            err = []
        except:
            err = sys.exc_info()
            if type(err[1]) in [pymongo.errors.AutoReconnect,
                                bson.errors.InvalidDocument]:
                ids1, err_lst1 = self.recInsert(self, data[:db_index])
                ids2, err_lst2 = self.recInsert(self, data[db_index:])
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

class NBAMonConn(MongoConn):
    def __init__(self, **dargs):
        MongoConn.__init__(self, args=dargs)

    def addInfo(self, pageType ,data):
        '''
        Handles the general call to the fucntions for updating the
        MySQL database with new information;
        '''
        if pageType=='pbp':
            pass
        elif pageType=='box':
            self.updateBox(self, data)

        elif pageType=='ext':
            pass
        else:
            print "Warning! non valid page type; not updating"

class RSSMonConn(MongoConn):
    def __init__(self, **dargs):
        MongoConn.__init__(self, args=dargs)
