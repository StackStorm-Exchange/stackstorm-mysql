import MySQLdb
import MySQLdb.cursors
import six

from datetime import datetime
from st2common.runners.base_action import Action

__all__ = [
    'MySQLBaseAction'
]

try:  # Python 2
    unicode = unicode
except NameError:  # Python 3
    unicode = str


class MySQLBaseAction(Action):

    def __init__(self, config):
        super(MySQLBaseAction, self).__init__(config=config)
        self.config = config

    def config_conn(self, connection):
        self.db_config = self.config['connections'].get(connection)
        return self.manual_conn(host=self.db_config.get('host', None),
                                user=self.db_config.get('user', None),
                                passwd=self.db_config.get('pass', None),
                                db=self.db_config.get('db', None),
                                cursorclass=MySQLdb.cursors.DictCursor)

    def manual_conn(self, host, user, passwd, db,
                    cursorclass=MySQLdb.cursors.DictCursor):
        return MySQLdb.connect(host=host,
                               user=user,
                               passwd=passwd,
                               db=db,
                               cursorclass=cursorclass)

    def _escape_string(self, item):
        return six.ensure_str(
            MySQLdb.escape_string(unicode(item).encode('utf-8')))  # pylint: disable=no-member

    def _list_to_string(self, data, quotes=True):
        output = ""
        if quotes:
            output = ','.join(["'{}'".format(self._escape_string(item))
                              for item in data])
        else:
            output = ','.join([self._escape_string(item)
                              for item in data])

        return output.lstrip(',')

    def _format_results(self, cursor):
        if cursor.rowcount < 1:
            return None
        rows = []
        for row in cursor.fetchall():
            d = {}
            for k, v in six.iteritems(row):
                if isinstance(v, datetime):
                    d[k] = str(v)
                else:
                    d[k] = v
            rows.append(d)
        return rows
