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
    def __init__(self, args=dict(), **dargs):
        self._store = dict()
        self.conn = pymongo.Connection()
        db_name = args['db_name'] \
                  if 'db_name' in args.keys() else None
        coll_name = args['coll_name'] \
                    if 'coll_name' in args.keys() else None

        self.makeDBConn(db_name)
        if 'db' in self.__dict__.keys():
            self.makeCollConn(coll_name)
        
    def makeDBConn(self, db_name):
        if db_name in self.conn.database_names():
            self.db = self.conn[db_name]
        elif not db_name:
            print("No db name provided; only conn to mdb privided.")
        elif db_name not in self.conn.database_names():
            print('Database "%s" does not currently exist' % db_name)
        else:
            print('Failure to make connection to db, uknw reason')

    def makeCollConn(self, coll_name):
        if coll_name in self.db.collection_names():
            self.coll = self.db[coll_name]
        elif not coll_name:
            print("No collection name provided; only conn to db privided.")
        elif coll_name not in self.db.collection_names():
            print('Collection "%s" does not currently exist' % coll_name)
        else:
            print('Failure to make connection to coll, uknw reason')

    def MongoInsert(self, data, verbose=False):
        """
        Default insert for dict objects into mongo with this class
        """
        try:
            ids = self.coll.insert(data)
            self._store['lastIDs'] = ids
            if verbose: return ids
        except AttributeError:
            print("No collection name has been defined; \ndata not inserted.")
        except:
            print("Breaking data into parts")
            self._store['lastIDs'], self._store['lastErr']\
                                    = self.RecursInsert(data)

    def RecursInsert(self, data):
        """
        Mongo has a maximum batch insert size; instead of trying
        to figure out the size of the data, just try, try again.
        Split after each fail, recursively.
        """
        ids,ers = list(),list()
        db_index = int(math.floor(len(data)/2.0))
        try:
            ids1 = self.coll.insert(data[:db_index])
            ids2 = self.coll.insert(data[db_index:])
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
