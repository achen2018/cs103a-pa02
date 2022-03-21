'''
transaction.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (rowid, 'item #','amount','category','date','description')
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3
import datetime

def to_tran_dict(tran_tuple):
    ''' tran is a transaction tuple ('item #','amount','category','date','description')'''
    tran = {'rowid':tran_tuple[0],'item #':tran_tuple[1], 'amount':tran_tuple[2], 'category':tran_tuple[3], 'date':tran_tuple[4],'description':tran_tuple[5]}
    return tran

def to_tran_dict_list(tran_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_tran_dict(tran) for tran in tran_tuples]

class Transaction():
    ''' Transaction represents a table of transactions'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    ('item #' text, amount int, category text, date text, description text)''')

        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_one(self,rowid):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict(tuples[0])
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)
    
    def add(self,item):
        ''' 
            @author Su Lei Yadanar
            add a transaction to the transactions table.
            this returns the item of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item #'],item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete(self,rowid):
        ''' 
            @author Su Lei Yadanar
            deletes a row to the transactions table.
            this returns the rowid of the deleted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()

    def sumByDate(self, recentFirst = True):
        '''Summarizes the transaction by the date (recent first by default)
            @author Angelo Cataldo'''
        orderString = " desc"
        if not recentFirst:
            orderString = ""
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("select * from transactions order by date" + orderString)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result
    
    def sumByMonth(self, janFirst = False):
        '''Summarizes the transaction by the month (January->Dec by default)
            If there is a tie, the entry in an earlier row goes first
            @author Angelo Cataldo'''
        orderString = " desc"
        if not janFirst:
            orderString = ""
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        #yyyymmdd
        cur.execute("select * from transactions order by SUBSTRING(date,5,2)" + orderString)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result