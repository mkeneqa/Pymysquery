## MyPyDb Database Class

A Python3 Object Oriented Database wrapper class for the **[PyMySQL]([https://pypi.org/project/PyMySQL/](https://pypi.org/project/PyMySQL/))** module.

This is a compilation of commonly used database functions I've used over the years when using the PyMySQL module for querying Maria/MySQL databases.

**DISCLAIMER:** This is a WIP and requires testing and better documentation. Please use at your own risk.

## Get Started
### Option 1 - Clone The Repo:
 - `git clone https://github.com/mkeneqa/mypydb.git`
 - `python3 -m venv env` (unix) or `py -m venv env` (win)
 - Activate Environment:
	 - **UNIX**: `source env/bin/activate` 
     - **WINDOWS**: `.\env\Scripts\activate`
 - **Optional:** `python -m pip install --upgrade pip`
 - `python -m pip install PyMySQL`
 - `python -m pip install pandas`

### Option 2 - Download the `pymydb `file :

 - Download the [`mypydb.py` ](https://github.com/mkeneqa/mypydb/blob/master/mypydb.py) file and place it in your project
- `python -m pip install PyMySQL`
- `python -m pip install pandas`

## Usage
 
 
**Initialize Database Connection**
```python
import pymydb as _db
_db.DBUSR = 'db_user'
_db.DBPSWD = 'db_pswd'
host_ip = '192.168.10.10'
db_name = 'my_db'
_db = DB.Database(host_ip,db_name)
_db.Connect()
```

**Truncate Table**
```
_db.TruncateTable('my_db')
```

**Fetch All**
```
_db.FetchAll("SELECT * FROM users")
```

**Fetch One**
```
_db.FetchOne("SELECT `id` FROM users LIMIT 2")
```