# cs103a-pa02
Second programming assignment for CS103a in Spring 2022

# Scripts
Script started on Fri Mar 25 07:39:51 2022
Restored session: Fri Mar 25 07:39:31 EDT 2022

# pylint script
(base) sulei@su-leis-air pa02 % pylint tracker.py
************* Module tracker
tracker.py:39:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:53:0: R0914: Too many local variables (17/15) (too-many-locals)
tracker.py:57:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:78:8: W0105: String statement has no effect (pointless-string-statement)
tracker.py:89:8: W0105: String statement has no effect (pointless-string-statement)
tracker.py:103:8: C0103: Variable name "totalQty" doesn't conform to snake_case naming style (invalid-name)
tracker.py:105:12: C0103: Variable name "totalQty" doesn't conform to snake_case naming style (invalid-name)
tracker.py:111:8: C0103: Variable name "totalQty" doesn't conform to snake_case naming style (invalid-name)
tracker.py:113:12: C0103: Variable name "totalQty" doesn't conform to snake_case naming style (invalid-name)
tracker.py:53:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:53:0: R0912: Too many branches (15/12) (too-many-branches)
tracker.py:53:0: R0915: Too many statements (60/50) (too-many-statements)
tracker.py:127:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:150:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:151:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:153:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:154:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:159:25: W0622: Redefining built-in 'list' (redefined-builtin)
tracker.py:159:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:160:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
tracker.py:35:0: W0611: Unused import sys (unused-import)
tracker.py:35:0: C0411: standard import "import sys" should be placed before "from category import Category" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 7.71/10 (previous run: 7.71/10, +0.00)

(base) sulei@su-leis-air pa02 % pylint transactions.py
************* Module transactions
transactions.py:15:0: C0301: Line too long (145/100) (line-too-long)
transactions.py:62:0: C0301: Line too long (147/100) (line-too-long)
transactions.py:120:0: C0301: Line too long (131/100) (line-too-long)
transactions.py:132:0: C0301: Line too long (122/100) (line-too-long)
transactions.py:149:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:84:4: C0103: Method name "sumByDate" doesn't conform to snake_case naming style (invalid-name)
transactions.py:84:24: C0103: Argument name "recentFirst" doesn't conform to snake_case naming style (invalid-name)
transactions.py:87:8: C0103: Variable name "orderString" doesn't conform to snake_case naming style (invalid-name)
transactions.py:89:12: C0103: Variable name "orderString" doesn't conform to snake_case naming style (invalid-name)
transactions.py:98:4: C0103: Method name "sumByMonth" doesn't conform to snake_case naming style (invalid-name)
transactions.py:98:25: C0103: Argument name "janFirst" doesn't conform to snake_case naming style (invalid-name)
transactions.py:102:8: C0103: Variable name "orderString" doesn't conform to snake_case naming style (invalid-name)
transactions.py:104:12: C0103: Variable name "orderString" doesn't conform to snake_case naming style (invalid-name)
transactions.py:114:4: C0103: Method name "sumByYear" doesn't conform to snake_case naming style (invalid-name)
transactions.py:126:4: C0103: Method name "sumByCategory" doesn't conform to snake_case naming style (invalid-name)
transactions.py:138:4: C0103: Method name "totalTransactions" doesn't conform to snake_case naming style (invalid-name)
transactions.py:150:4: C0103: Method name "totalPerMonth" doesn't conform to snake_case naming style (invalid-name)
transactions.py:150:28: C0103: Argument name "janFirst" doesn't conform to snake_case naming style (invalid-name)
transactions.py:154:8: C0103: Variable name "orderString" doesn't conform to snake_case naming style (invalid-name)
transactions.py:156:12: C0103: Variable name "orderString" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 8.06/10 (previous run: 8.06/10, +0.00)

(base) sulei@su-leis-air pa02 % pylint test_transactions.py
************* Module test_transactions
test_transactions.py:26:0: C0301: Line too long (101/100) (line-too-long)
test_transactions.py:27:0: C0301: Line too long (101/100) (line-too-long)
test_transactions.py:48:0: C0301: Line too long (102/100) (line-too-long)
test_transactions.py:13:14: W0621: Redefining name 'dbfile' from outer scope (line 8) (redefined-outer-name)
test_transactions.py:15:4: C0103: Variable name "db" doesn't conform to snake_case naming style (invalid-name)
test_transactions.py:19:20: W0621: Redefining name 'empty_db1' from outer scope (line 13) (redefined-outer-name)
test_transactions.py:44:13: W0621: Redefining name 'empty_db1' from outer scope (line 13) (redefined-outer-name)
test_transactions.py:59:11: W0621: Redefining name 'small_db' from outer scope (line 44) (redefined-outer-name)
test_transactions.py:64:8: C0103: Variable name "s" doesn't conform to snake_case naming style (invalid-name)
test_transactions.py:83:4: C0103: Variable name "a" doesn't conform to snake_case naming style (invalid-name)
test_transactions.py:93:13: W0621: Redefining name 'med_db' from outer scope (line 59) (redefined-outer-name)
test_transactions.py:114:16: W0621: Redefining name 'med_db' from outer scope (line 59) (redefined-outer-name)
test_transactions.py:135:21: W0621: Redefining name 'proper_dates_db' from outer scope (line 19) (redefined-outer-name)
test_transactions.py:139:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
test_transactions.py:147:22: W0621: Redefining name 'proper_dates_db' from outer scope (line 19) (redefined-outer-name)
test_transactions.py:151:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
test_transactions.py:160:21: W0621: Redefining name 'proper_dates_db' from outer scope (line 19) (redefined-outer-name)
test_transactions.py:171:25: W0621: Redefining name 'proper_dates_db' from outer scope (line 19) (redefined-outer-name)
test_transactions.py:181:25: W0621: Redefining name 'proper_dates_db' from outer scope (line 19) (redefined-outer-name)
test_transactions.py:186:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
test_transactions.py:196:19: W0621: Redefining name 'proper_dates_db' from outer scope (line 19) (redefined-outer-name)

------------------------------------------------------------------
Your code has been rated at 8.21/10 (previous run: 8.21/10, +0.00)

# pytest script

(base) sulei@su-leis-air pa02 % pytest test_transactions.py
============================= test session starts ==============================
platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.9.0, pluggy-0.12.0
rootdir: /Users/sulei/Desktop/Fundaments of Software Engineering/cs103a-pa02/pa02, configfile: pytest.ini
plugins: anyio-3.5.0
collectedg7.items

test_transactions.py .......						 [100%]

============================== 7 passed in 0.27s ===============================
# tracker.py script
(base) sulei@su-leis-air pa02 % python3 tracker.py

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

> 4
('item #', 'amount', 'category', 'date', 'description')
----------------------------------------
(1, 3, 50, 'food', '20210912', 'fish')
(2, 4, 2, 'food', '20210814', 'water')
> 5
item #: 5
amount: 5
transaction category name: clothes
transaction date yyyymmdd: 20220915
transaction description: winter boots
> 5
item #: 7
amount: 2
transaction category name: clohtes
transaction date yyyymmdd: 20220815
transaction description: dress
> 6
rowid: 3
> 4
('item #', 'amount', 'category', 'date', 'description')
----------------------------------------
(1, 3, 50, 'food', '20210912', 'fish')
(2, 4, 2, 'food', '20210814', 'water')
(4, 7, 2, 'clohtes', '20220815', 'dress')
> 7
1. (7, 2, 'clohtes', '20220815', 'dress')
2. (3, 50, 'food', '20210912', 'fish')
3. (4, 2, 'food', '20210814', 'water')
> 8
1. (4, 2, 'food', '20210814', 'water')
2. (7, 2, 'clohtes', '20220815', 'dress')
3. (3, 50, 'food', '20210912', 'fish')
> 9
Enter a Year to Summarize: 2021
Total transactions moved in year 2021: 2
Total quantity moved in year 2021: 52
> 10
Enter a Category to Summarize: food
Total transactions in category food: 2
Total quantity moved in category food: 52
> 11

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

> 0
bye
(base) sulei@su-leis-air pa02 % exit
Saving session...
...saving history...truncating history files...
...completed.

Script done on Fri Mar 25 07:44:14 2022
