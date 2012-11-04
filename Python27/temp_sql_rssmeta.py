import sys, os
import MySQLdb as ms
import connect
from picklingIsEasy import unpickledata
import time
import datetime

def formSQLDateTime(date):
    if date and date!="NULL":
        year = date.tm_year
        mont = date.tm_mon
        days = date.tm_mday
        hour = date.tm_hour
        mins = date.tm_min
        secs = date.tm_sec
        new_date = year + '-' + mont + '-' + days + ' ' +\
                   hour + ':' + mins + ':' + secs
    else:
        new_date = None
    return new_date

def setNulls(d):
    for key in d.keys():
        if not d[key]:
            d[key] = None
    return d


if __name__=="__main__":
    data_file, db, p, table        = sys.argv[1:]
    conn        = connect.handcon(db=db,
                                   p=p)
    if conn:
        BLOG_DATA = unpickledata(data_file)
        cursor = conn.cursor()
        count = 0
        for d in BLOG_DATA:
            if count%50==0: print count
            d = setNulls(d)
            print '''INSERT INTO BasicStoryMeta (Title, DateTime, URL, Source, Author, Keywords, Description, Attrs) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''' % \
                           (d['title'],
                            formSQLDateTime(d['date']),
                            d['link'],
                            d['source'],
                            d['author'],
                            d['tags'],
                            d['summary'],
                            d['attrs'])
            cursor.execute('''INSERT INTO BasicStoryMeta (Title, DateTime, URL, Source, Author, Keywords, Description, Attrs) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''' % \
                           (d['title'],
                            formSQLDateTime(d['date']),
                            d['link'],
                            d['source'],
                            d['author'],
                            d['tags'],
                            d['summary'],
                            d['attrs']))
            count += 1
    conn.close()
                                 

            
