
import MySQLdb
import MySQLdb.cursors

from st2actions.runners.pythonrunner import Action

__all__ = [
    'MySQLBaseAction'
]


class MySQLBaseAction(Action):

    def __init__(self, config):
        super(MySQLBaseAction, self).__init__(config=config)

    def config_conn(self, db):
        self.db_config = self._config.get(db, False)
        self.db = self.manual_conn(host=self.db_config.get('host', None),
                                   user=self.db_config.get('user', None),
                                   passwd=self.db_config.get('pass', None),
                                   db=self.db_config.get('name', None),
                                   cursorclass=MySQLdb.cursors.DictCursor)

    def manual_conn(self, host, user, passwd, db):
        self.db = MySQLdb.connect(host=host,
                                  user=user,
                                  passwd=passwd,
                                  db=db,
                                  cursorclass=MySQLdb.cursors.DictCursor)

    def _list_to_string(self, data):
        output = ""
        for item in data:
            output = "%s, '%s'" % (output, MySQLdb.escape_string(item))

        return output
