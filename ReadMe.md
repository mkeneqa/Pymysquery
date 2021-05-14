## PySQuery Database Module

Formerly known as _MyPyDb Database Class_

A Python3 Object Oriented Database wrapper class for the **[PyMySQL]([https://pypi.org/project/PyMySQL/](https://pypi.org/project/PyMySQL/))** module. 

This is a compilation of commonly used database functions I've used over the years when using the PyMySQL module for querying Maria/MySQL databases.

Some Benefits of Using this class:
- Plug-and-play
- Out-of-the-box support of database transactions - commit and rollbacks
- Clear database functions calls: fetch, update, delete, truncate
- Easily manage multiple database connections by object instantiation
- and more!

**DISCLAIMER:** This is a WIP and requires testing and better documentation.

## Get Started
### Option 1 - Clone The Repo:
 - `git clone https://github.com/mkeneqa/mypydb.git`
 - `python3 -m venv venv` (unix) or `py -m venv venv` (win)
 - Activate Environment:
	 - **UNIX**: `source venv/bin/activate` 
     - **WINDOWS**: `.\venv\Scripts\activate`
 - **Optional:** `python -m pip install --upgrade pip`
 - `python -m pip install PyMySQL`
 - `python -m pip install pandas`

### Option 2 - Download the `pymydb` file :

 - Download the [`mypydb.py` ](https://github.com/mkeneqa/mypydb/blob/master/mypydb.py) file and place it in your project
- `python -m pip install PyMySQL`
- `python -m pip install pandas`

## Usage
 
 
**Initialize Database Connection**
```python
import pymydb

host_ip = '192.168.10.10'
db_name = 'my_db'

pymydb.Database.DBUSR = 'db_user'
pymydb.Database.DBPSWD = 'db_pswd'

_db = pymydb.Database(host_ip,db_name)

_db.Connect()
```

**Truncate Table**
```python
_db.TruncateTable('users')
```

**Fetch All**
```python
# returns a list of coloumn names as Tuples
rows = _db.FetchAll("SELECT * FROM users")

for row in rows:
    rid,first_name,last_name,is_active = row
    # do something ...
```

**Fetch One**
```python
_db.FetchOne("SELECT `id` FROM users LIMIT 1")
```

**Close Connection**
```python
_db.CloseConn()
```