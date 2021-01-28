import MySQLdb
import six

from lib.base import MySQLBaseAction


class MySQLInsertAction(MySQLBaseAction):

    def run(self, connection, table, data, host, user, passwd, db):
        if connection:
            self.db = self.config_conn(connection=connection)
        else:
            self.db = self.manual_conn(host=host,
                                       user=user,
                                       passwd=passwd,
                                       db=db)

        return self.insert(table, data)

    def insert(self, table, data):
        columns = self._list_to_string(data.keys(), quotes=False)
        values = self._list_to_string(data.values())

        query = "INSERT INTO {} ({}) VALUES ({})".format(
            six.ensure_str(table.encode('utf-8')), columns, values)
        c = self.db.cursor()
        try:
            c.execute(query)
            count = c.rowcount
            self.db.commit()
            return count
        except MySQLdb.Error as e:  # pylint: disable=no-member
            raise Exception(e)
