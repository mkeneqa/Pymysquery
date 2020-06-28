import pymysql
import pandas


class Database(object):
    DBPSWD = ""
    DBUSR = ""
    CALGARYIP = ""
    HOUSTONIP = ""
    CURSR = ""
    CONN = ""
    HOST = ""
    DBNAME = ""
    DBO = ""
    _query_string = ""

    def __init__(self, the_host='', the_db=''):
        self.HOST = the_host
        self.DBNAME = the_db
        self.DBO = self.Connect()
        self.CURSR = self.DBO.cursor()

    def Connect(self):
        return pymysql.connect(
            host=self.HOST,
            user=self.DBUSR,
            passwd=self.DBPSWD,
            db=self.DBNAME
        )

    def SetHost(self, hostname):
        self.HOST = hostname

    def SetPassword(self, password):
        self.DBPSWD = password

    def SetDbName(self, dbname):
        self.DBNAME = dbname

    def GetDbName(self):
        return self.DBNAME

    def GetHost(self):
        return self.HOST

    def ResetQryStr(self):
        self._query_string = None

    def SetQryStr(self, qry, reset=False):
        if reset:
            self.ResetQryStr()

        self._query_string = qry

    def GetLastInsertID(self):
        return self.CURSR.lastrowid

    def GetQryStr(self):
        return self._query_string

    def CloseConn(self):
        self.DBO.close()

    def query(self, query, params):
        return self.CURSR.execute(query, params)

    def UpdateTableWhereIn(self, db_table: str, set_cols: list, where_vals: list, where_key='`id`', verbose_print=True):
        """
        Updates defined database table using the Where In clause
        :param db_table: database table name
        :param set_cols: col vals to override
        :param where_vals: [123,456,1232]
        :param where_key: key to use to update coloumn. defaults to the id coloumn
        :param verbose_print: to print out extra messages on console

        eg. _db.UpdateTableWhereIn(
            db_table= 'project_list',
            set_cols= ['skip = 1'],
            where_vals= [12,13,24],
            where_key= '`pk_id`'
        )
        """

        set_cols = ",".join(set_cols)

        # stringify elements within list (src: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/)
        where_vals = ",".join(map(str, where_vals))
        qry = "UPDATE {0} SET {1} WHERE {2} IN ({3})".format(db_table, set_cols, where_key, where_vals)

        try:
            self.CURSR.execute(qry)
            self.DBO.commit()
        except Exception as e:
            self.DBO.rollback()
            print("!!Error Updating Table Where In: " + str(e))
        finally:
            if verbose_print:
                print("Update Where In Query = {0}".format(qry))

    def UpdateTableValues(self, db_table: str, set_cols: list, where_cols: list, verbose_print=True):

        """
            Updates defined database table. Don't include WHERE statement
            :param db_table: database table name
            :param set_cols: col vals to overrode
            :param where_cols: ['col_id=val_number','col_str="val_str"']
            :param verbose_print: to print out extra messages on console

            eg. _db.UpdateTableValues(
                'project_list',
                ['skip = 1'],
                ['id = ' + str(schm[0])]
            )
        """

        qry = "UPDATE " + db_table
        qry += " SET " + ",".join(set_cols)

        if len(where_cols) > 0:
            qry += " WHERE " + " AND ".join(where_cols)

        try:
            self.SetQryStr(qry)
            self.CURSR.execute(qry)
            self.DBO.commit()
        except Exception as e:
            self.DBO.rollback()
            print("!!Error Updating Table: " + str(e))
        finally:
            if verbose_print:
                print("Update QRY = {0}".format(self.GetQryStr()))

    def InsertDictionaryValues(self, db_table: str, insert_dict: dict, verbose_print=False):
        col_names = insert_dict.keys()
        col_vals = insert_dict.values()
        self.InsertTableValues(db_table, col_names, col_vals, verbose_print)

    def InsertTableValues(self, db_table, cols, vals, verbose_print=False):
        sQry = "INSERT INTO `" + db_table + "` "
        sQry += "(" + ",".join(cols) + ") "
        sQry += "VALUES (" + ",".join(['%s'] * len(cols)) + ")"
        
        try:
            self.SetQryStr(sQry)
            self.CURSR.execute(sQry, tuple(vals))
            self.DBO.commit()
            if verbose_print:
                print("Added Record @ id: " + str(self.CURSR.lastrowid))
        except Exception as e:
            self.DBO.rollback()
            print("!!Error Inserting Record : " + str(e))

    def FetchAllWithPandas(self, qry):
        return pandas.read_sql_query(qry, self.Connect())

    def GetUnbuffQryCursorObject(self, qry):
        """"
        Returns cursor object. Useful for looping through large datasets
        will do one row at a time unbuffered

        Usage:
            cursor = db.GetUnbuffQryCursorObject(qry)
            for row in cursor.fetchall_unbuffered():
                do something with row  ...
        """
        cursor = pymysql.cursors.SSCursor(self.Connect())
        self.SetQryStr(qry)
        # db = self.Connect()
        # cursor = db.cursor()
        cursor.execute(qry)
        return cursor
        # def updateTable_NoBuff(self, db_table, set_cols, where_cols ):

    def FetchAll(self, sQry):
        rows = None
        try:
            self.SetQryStr(sQry)
            db = self.Connect()
            cursor = db.cursor()
            cursor.execute(sQry)
            rows = cursor.fetchall()

        except pymysql.err.InternalError as e:
            err = [str(e), " in db: " + str(self.DBNAME)]
            print("".join(err))
            rows = None

        except Exception as e:
            rows = None
            print("ERR FETCH ROWS", str(rows), True)

        return rows

    def FetchOne(self, sQry, print_verbosity=True):
        row = None

        try:
            # print("TRY BLOCK")
            db = self.Connect()
            cursor = db.cursor()
            cursor.execute(sQry)
            row = cursor.fetchone()

        except pymysql.err.InternalError as e:
            if print_verbosity:
                print('Internal Error:' + str(e))
            row = None
        except Exception as e:
            print("ERROR FETCH ON RESULT", str(row), True)
            self.DBO.rollback()

            if print_verbosity:
                print("!!Error executing query: " + str(e))
        finally:
            if print_verbosity:
                print("qry = " + sQry)
                print("FETCH ON RESULT", str(row))

        if row is None:
            return 0
        else:
            return row[0]

    def TruncateTable(self, db_table):

        try:
            self.CURSR.execute("TRUNCATE TABLE " + db_table)
            self.DBO.commit()

            self.CURSR.execute("ALTER TABLE " + db_table + " AUTO_INCREMENT = 1")
            self.DBO.commit()

            print("SUCCESSFULLY Truncated " + db_table + " table and reset increments!")

        except Exception as e:
            self.DBO.rollback()
            print("!!Error Truncating Table " + db_table + " : " + str(e))

    def DeleteFromDB(self, db_table: str, where_cols: list, where_and=True):
        """Generic Delete Query. Don't declare WHERE statement just cols and values
            :param db_table: db table name
            :param where_cols:  ['col_id=val_number','col_str="val_str"']
            :param where_and: if more than one where coloums are they connected with an AND or OR
        """

        qry = "DELETE FROM " + self.DBNAME + "." + db_table

        if where_and:
            qry += " WHERE " + " AND ".join(where_cols)
        else:
            qry += " WHERE " + " OR ".join(where_cols)

        try:
            print("try block")
            self.CURSR.execute(qry)
            self.DBO.commit()

        except Exception as e:
            self.DBO.rollback()
            print("!!Error Deleting : " + str(e))

        finally:
            print("Delete Query : " + str(qry))
