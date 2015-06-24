import MySQLdb

from lib.base import MySQLBaseAction


class MySQLInsertAction(MySQLBaseAction):

    def run(self, table, data, host, user, passwd, db):
        if not host or not user:
            self.db = self.config_conn(db=db)
        else:
            self.db = self.manual_conn(host=host,
                                       user=user,
                                       passwd=passwd,
                                       db=db)

        return self.insert(table, data)

    def insert(self, table, data):
        columns = self._list_to_string(data.keys(), quotes=False)
        values = self._list_to_string(data.values())

        query = "INSERT INTO %s (%s) VALUES (%s)" % (table, columns, values)
        c = self.db.cursor()
        try:
            c.execute(query)
            count = c.rowcount
            self.db.commit()
            return count
        except MySQLdb.Error, e:
            print str(e)
            return False
