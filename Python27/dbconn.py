"""
Handles data transfers between MySQL / Mongo dbs and source docs via
connection objects and web interface objects; Connection objects for
interactig with MySQL and MongoDB interfaces,
for a variety of tasks (NBA stats, RSS / WebPage text analysis, etc);
meant to ghandle inserting objects, tracking ids. querying, etc.
"""
import sys, os
import math

import connectSQL
import connectMon


class DBConnection:
    def __init__(self):
        self.__store = dict()

    def makeMySQLConn(self, mens):
        '''
        Create MySQLConn object with connection to SQL database of type 'mens';
        return object
        '''
        if mens=='NBA':
            conn = NBASQLConn(db   = 'NBA_temp',
                              h    = 'localhost',
                              u    = 'sinn',
                              p    = 't')
        elif mens=='RSS':
            conn = connectSQL.RSSSQLConn()
        else:
            # error shit
            pass
        return conn

    def makeMongoConn(self, mens, **dargs):
        '''
        Create MongoConn object with connection to Mongo database of type 'mens';
        return object
        '''
        if mens=='NBA':
            conn = NBAMonConn(db_name, coll_name)
        elif mens=='RSS':
##            coll_name = 'Wired'
##            if 'coll' in dargs.keys():
##                coll_name = dargs_coll
            ## fix this stupud shit, yo
            conn = connectMon.RSSMonConn(**{'db_name':'WebPages',
                                         'coll_name':'TestPages'})
        return conn

class NBAConn(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)
        self.__mdbConn = self.makeMongoConn('NBA')
        self.__sqlConn = self.makeMySQLConn('NBA')


class RSSConn(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)
        self.mdbConn = self.makeMongoConn('RSS')
       # self.__sqlConn = self.makeMySQLConn('RSS')
