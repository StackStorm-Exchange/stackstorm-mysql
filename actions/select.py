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

        return self.select(query, data)

    def select(self, query, data):
        values = self._list_to_string(data)
        q = query.format(values)
        self.logger.debug("Generated query: %s" % q)

        c = self.db.cursor()
        try:
            c.execute(q)
            output = self._format_results(c)
            return output
        except MySQLdb.Error, e:
            print str(e)
            return False
