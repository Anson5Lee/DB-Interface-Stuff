'''
Basic stuff for interacting w/ MongoDB via python's pymongo
driver;
'''
import sys
import csv, math
import pymongo

'''
Grab .csv file, put into dict w/ csv.DictReader; need to use 'rU' b/c of '\r'
linebreak;
'''
def loadfile():
    fpath = \
          '/media/FreeForAll/Data/Contestant Package/Datasets/2010 SAS Shootout Dataset.csv'
    with open(fpath, 'rU') as csvfile:
        health_list = list()
        health_read_dict = csv.DictReader(csvfile, lineterminator='\r')
        for row in health_read_dict:
            for key in row.keys():
                row[key] = float(row[key])
            health_list.append(row)
    return health_list

def failtosave(health_list):
    conn = pymongo.Connection()
    db = conn['PlayData']
    try:
        db.Healthcare.insert(health_list)
        t = ''
    except:
        t = sys.exc_info()
        print t
    return t
##'''
##Error returned from 1st try:
##
##InvalidDocument: BSON document too large (61691025 bytes) -
##the connected server supports BSON document sizes up to 16777216 bytes.
##
##whoops...need to create a file that handles this, merges equiv of
##'t_out', below, for output from MDB; use these keys l8r in SQL
##'''
##
##
##db = pymongo.Connection().PlayData        # creates conn to Healthcare db
##N = len(health_list)                        # healthcare too large, split into chunks
##db_index = range(0,N,int(math.floor(N/6)))  
##db_index.append(N)
##for i in range(len(db_index)-1):
##    temp_dict = health_dict[db_index[i]:db_index[i+1]]
##    t_out = db.Healthcare.insert(temp_dict)


if __name__=="__main__":
    health_list = loadfile()
    t = failtosave(health_list)
    print t
