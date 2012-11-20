"""
Actual connection handles for Mongo; used by dbconn
to create the connections.  
"""
import sys, os
import datetime, time

import pymongo, bson

class MongoConn:
    """
    General handle for making a connection to a local Mongo database
    from within python; utilizes pymongo package;
    """
    def __init__(self, args=None, **dargs):
        conn = pymongo.Connection()
        if db_name in conn.database_names:
            conn = conn[db_name]
            if coll_name in conn.collection_names():
                self.conn = conn
            elif not coll_nam
                self.conn = conn
    ##        else:
    ##    else:


    def MongoInsert(self, data):
        self.__store['lastIDs'], self.__store['lastErr']\
                                 = self.RecursInsert(self, data)

    def RecursInsert(self, data):
        ids = list()
        ers = list()
        N = len(health_list)
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

        elif pageType=='box':
            self.updateBox(self, data)

        elif pageType=='ext':

        else:
            print "Warning! non valid page type; not updating"

class RSSMonConn(MongoConn):
    def __init__(self, **dargs):
        MongoConn.__init__(self, args=dargs)
