'''
transaction.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    ('item #','amount','category','date','description')
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3

def to_tran_dict(tran_tuple):
    ''' tran is a transaction tuple ('item #','amount','category','date','description')'''
    tran = {'item #':tran_tuple[0], 'amount':tran_tuple[1], 'category':tran_tuple[2], 'date':tran_tuple[3],'description':tran_tuple[4]}
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
                    (item# int, amount int, category text, date text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    #not sure if we'll need these??
    # def select_all(self):
    #     ''' return all of the transactions as a list of dicts.'''
    #     con= sqlite3.connect(self.dbfile)
    #     cur = con.cursor()
    #     cur.execute("SELECT rowid,* from categories")
    #     tuples = cur.fetchall()
    #     con.commit()
    #     con.close()
    #     return to_cat_dict_list(tuples)

    # def select_one(self,rowid):
    #     ''' return a category with a specified rowid '''
    #     con= sqlite3.connect(self.dbfile)
    #     cur = con.cursor()
    #     cur.execute("SELECT rowid,* from categories where rowid=(?)",(rowid,) )
    #     tuples = cur.fetchall()
    #     con.commit()
    #     con.close()
    #     return to_cat_dict(tuples[0])


    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the item # of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['name'],item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete(self,rowid):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM categories
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()
