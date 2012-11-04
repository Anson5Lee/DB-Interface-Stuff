#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


if __name__=="__main__":
    
    con = mdb.connect('localhost', 'sinn', 't', 'sampdb');

    with con:
        
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS \
            Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
        cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
