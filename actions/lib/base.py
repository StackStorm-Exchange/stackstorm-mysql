
import MySQLdb
import MySQLdb.cursors

from st2actions.runners.pythonrunner import Action

__all__ = [
    'MySQLBaseAction'
]


class MySQLBaseAction(Action):

    def __init__(self, config):
        super(MySQLBaseAction, self).__init__(config=config)
        self.config = config

    def config_conn(self, db):
        self.db_config = self.config.get(db, False)
        return self.manual_conn(host=self.db_config.get('host', None),
                                user=self.db_config.get('user', None),
                                passwd=self.db_config.get('pass', None),
                                db=db,
                                cursorclass=MySQLdb.cursors.DictCursor)

    def manual_conn(self, host, user, passwd, db,
                    cursorclass=MySQLdb.cursors.DictCursor):
        return MySQLdb.connect(host=host,
                               user=user,
                               passwd=passwd,
                               db=db,
                               cursorclass=cursorclass)

    def _list_to_string(self, data, quotes=True):
        output = ""
        if quotes:
            output = ','.join(["'{}'".format(MySQLdb.escape_string(str(item)))
                              for item in data])
        else:
            output = ','.join([MySQLdb.escape_string(str(item))
                              for item in data])

        return output.lstrip(',')
