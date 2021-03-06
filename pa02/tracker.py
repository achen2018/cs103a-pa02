#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''
from category import Category
from transactions import Transaction
import sys


# here is the menu for the tracker app
menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''
def process_choice(choice):
    '''Menu Choices'''
    category = Category('tracker.db')
    transactions=Transaction('tracker.db')
    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice=='4':
        trans = transactions.select_all()
        print_transactions(trans)
    elif choice=='5':
        '''@author Su Lei Yadanar
            add transaction
        '''
        item=int(input("item #: "))
        amount=int(input("amount: "))
        category=input("transaction category name: ")
        date = input("transaction date yyyymmdd: ")
        desc = input("transaction description: ")
        tran = {'item #':item,'amount':amount, 'category':category, 'date':date, 'description':desc}
        transactions.add(tran)
    elif choice=='6':
        '''@author Su Lei Yadanar
            delete transaction
        '''
        rowid = int(input("rowid: "))
        transactions.delete(rowid)
    elif choice == '7':
        result = transactions.sumByDate()
        print_list_with_nums(result)
    elif choice == '8':
        result = transactions.sumByMonth()
        print_list_with_nums(result)
    elif choice == '9':
        year = input("Enter a Year to Summarize: ")
        result = transactions.sumByYear(year)
        totalQty = 0
        for row in result:
            totalQty = totalQty + row[1]
        print("Total transactions moved in year " + str(year) + ": " + str(len(result)))
        print("Total quantity moved in year " + str(year) + ": " + str(totalQty))
    elif choice == '10':
        cat = input("Enter a Category to Summarize: ")
        result = transactions.sumByCategory(cat)
        totalQty = 0
        for row in result:
            totalQty = totalQty + row[1]
        print("Total transactions in category " + str(cat) + ": " + str(len(result)))
        print("Total quantity moved in category " + str(cat) + ": " + str(totalQty))
    elif choice == '11':
        print(menu)

    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return choice
def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#
def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print((
        'item #','amount','category','date','description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values())
        print(values)

def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)

def print_list_with_nums(list):
    for i in range(len(list)):
        num = i + 1
        print(str(num) + ". " + str(list[i]))

# here is the main call!

toplevel()
