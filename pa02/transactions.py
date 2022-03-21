'''
transaction.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (rowid, 'item #','amount','category','date','description')
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3

def to_tran_dict(tran_tuple):
    ''' tran is a transaction tuple ('item #','amount','category','date','description')'''
    tran = {'row id':tran_tuple[0],'item #':tran_tuple[1], 'amount':tran_tuple[2], 'category':tran_tuple[3], 'date':tran_tuple[4],'description':tran_tuple[5]}
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
        ''' add a transaction to the transactions table.
            this returns the item# of the inserted element
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
        ''' this removes a transaction from the transactions table.
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()