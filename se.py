import sqlite3

class crawler:
    def __init__(self,dbname='search.db'):
        self.con=sqlite.connect(dbname)
    def __del__(self):
        pass
    def dbcommit(self):
        pass
    
    def getentryid(self,table,field,value,createnew=True):
        return None
    
    def createindextables(self):
        pass
    def addtoindex(self,url,soup):
        print('Indexing %s' % url)
    
    def gettextonly(self,soup):
        return None
    def separatewords(self,text):
        return None
    
    def isindexed(self,url):
        return False
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass
    def crawl(self,pages,depth=2):
        pass
    
    