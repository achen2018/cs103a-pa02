'''
transaction.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (rowid, 'item #','amount','category','date','description')
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3

def to_tran_dict(tran_tup):
    ''' tran is a transaction tuple ('item #','amount','category','date','description')'''
    tran = {'rowid':tran_tup[0],'item #':tran_tup[1], 'amount':tran_tup[2], 'category':tran_tup[3], 'date':tran_tup[4],'description':tran_tup[5]}
    return tran

def to_tran_dict_list(tran_tup):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_tran_dict(tran) for tran in tran_tup]

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
            If there is a month tie (same month), the entry in an earlier row goes first
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

    def sumByYear(self, year):
        '''Summarizes the transaction by the year
            @author Joshua liu'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        #yyyymmdd
        cur.execute("select * from transactions where date LIKE '" + str(year) + "%'")  # beginning with date, substring didnt work
        result = cur.fetchall()
        con.commit()
        con.close()
        return result

    def sumByCategory(self, cat):
        '''Summarizes the transaction by the category
            @author Joshua liu'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        #yyyymmdd
        cur.execute("select * from transactions where category LIKE '" + str(cat) + "'")  # no percent, exact match needed
        result = cur.fetchall()
        con.commit()
        con.close()
        return result

    def totalTransactions(self):
        '''Counts all the transactions in the database
            An extra method
            @author Andrew Chen'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT COUNT (*) FROM transactions")
        result = cur.fetchall()
        con.commit()
        con.close()
        return result
    
    def totalPerMonth(self, janFirst = False):
        '''Counts the number of transactions made each month (January->Dec by default)
            An extra method
            @author Andrew Chen'''
        orderString = " desc"
        if not janFirst:
            orderString = ""
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        #yyyymmdd
        cur.execute("SELECT COUNT (*) FROM transactions GROUP BY SUBSTRING(date,5,2)" + orderString)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result
