'''
test_categories runs unit and integration tests on the category module
'''

from ast import FloorDiv
import pytest
from transactions import Transaction, to_tran_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tran1 = {'item #':1002,'amount':20,'category':'food','date':'03/14/2022','description':'fresh food'}
    tran2 = {'item #':1003,'amount':30,'category':'donation','date':'03/10/2022','description':'charity'}
    tran3 = {'item #':1004,'amount':40,'category':'window','date':'03/24/2022','description':'broken glass'}
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 transactions
    for i in range(10):
        s = str(i)
        tran ={'item #':'item #'+s,
               'amount':'amount '+s,
               'category':'category '+s,
               'date':'date '+s,
               'description':'description '+s,
                }
        rowid = small_db.add(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 transactions
    for j in range(10):
        small_db.delete(rowids[j])

@pytest.mark.simple
def test_to_tran_dict():
    ''' teting the to_cat_dict function '''
    a = to_tran_dict((7,3,4,'food','02/13/2022','frozen food'))
    assert a['rowid']==7
    assert a['item #']==3
    assert a['amount']==4
    assert a['category']=='food'
    assert a['date']=='02/13/2022'
    assert a['description']=='frozen food'
    assert len(a.keys())==6

@pytest.mark.add
def test_add(med_db):
    ''' add a transaction to db, the select it, then delete it'''

    tran0 = {'item #':1002,'amount':20,'category':'food','date':'03/14/2022','description':'fresh food'}
    tran0 = med_db.select_all()
    rowid = med_db.add(tran0)
    trans1 = med_db.select_all()
    assert len(trans1) == len(tran0) + 1
    tran1 = med_db.select_one(rowid)
    assert tran1['item #']==tran0['item #']
    assert tran1['amount']==tran0['amount']
    assert tran1['category']==tran0['category']
    assert tran1['date']==tran0['date']
    assert tran1['description']==tran0['description']


@pytest.mark.delete
def test_delete(med_db):
    ''' add a transaction to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.select_all()

    # then we add this transaction to the table and get the new list of rows
    cat0 = {'item #':1002,'amount':20,'category':'food','date':'03/14/2022','description':'fresh food'}
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    cats2 = med_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1
