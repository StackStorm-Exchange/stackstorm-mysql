import MySQLdb

from lib.base import MySQLBaseAction

class MySQLSelectAction(MySQLBaseAction):

    def run(self, connection, query, data, host, user, passwd, db):
        if connection:
            self.db = self.config_conn(connection=connection)
        else:
            self.db = self.manual_conn(host=host,
                                       user=user,
                                       passwd=passwd,
                                       db=db)

        return self.update(query, data)

    def update(self, query, data):
        q = query
        if data:
            values = self._list_to_string(data)
            q = q.format(values)

        c = self.db.cursor()
        try:
            c.execute(q)
            count = c.rowcount
            self.db.commit()
            return count
        except MySQLdb.Error, e:  # pylint: disable=no-member
            raise Exception(e)
