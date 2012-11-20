"""
Handles data transfers between MySQL / Mongo dbs and source docs via
connection objects and web interface objects; Connection objects for
interactig with MySQL and MongoDB interfaces,
for a variety of tasks (NBA stats, RSS / WebPage text analysis, etc);
meant to ghandle inserting objects, tracking ids. querying, etc.
"""

import sys, os
import math

import pymongo, bson
import MySQLdb as ms

import connect


class DBConnection:
    def __init__(self):
        self.__store = dict()


class NBAConn(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)
        self.__mdbConn = connect.makeMongoConn('NBA')
        self.__sqlConn = connect.makeMySQLConn('NBA')


class RSSConn(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)
        self.__mdbConn = connect.makeMongoConn('RSS')
        self.__sqlConn = connect.makeMySQLConn('RSS')
