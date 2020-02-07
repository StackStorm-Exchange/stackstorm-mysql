import MySQLdb

from lib.base import MySQLBaseAction
from st2client.client import Client
from st2client.models import KeyValuePair


class MySQLSelectAction(MySQLBaseAction):

    def run(self, connection, query, data, host, user, passwd, db, key):
        if connection:
            self.db = self.config_conn(connection=connection)
        else:
            self.db = self.manual_conn(host=host,
                                       user=user,
                                       passwd=passwd,
                                       db=db)

        return self.select(query, data, key)

    def select(self, query, data, key):
        q = query
        if data:
            values = self._list_to_string(data)
            q = q.format(values)

        c = self.db.cursor()
        try:
            c.execute(q)
            output = self._format_results(c)
            if key is not None:
                client = Client(base_url='http://localhost')
                client.keys.update(KeyValuePair(name=key, value=str(output)))
                return key
            else:
                return output
        except MySQLdb.Error as e:  # pylint: disable=no-member
            raise Exception(e)
