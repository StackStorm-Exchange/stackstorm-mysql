# MySQL Integration Pack

Query and Update MySQL

## Pre-Requisites

You must install the `libmysqlclient-dev` system package, e.g. with `sudo apt install libmysqlclient-dev`

## Configuration

Copy the example configuration in [mysql.yaml.example](./mysql.yaml.example)
to `/opt/stackstorm/configs/mysql.yaml` and edit as required.

It can contain an array of one or more sets of MySQL connection parameters, like this:

```yaml
---
connections:
  community:
    host: "hostname"
    user: "user"
    pass: "password"
    db: "database"
  exchange:
    host: "mydb.local"
    user: "bob"
    pass: "PassW0rd"
    db: "st2"
```

Each entry should contain

* ``host`` - Database hostname
* ``user`` - Username to authenticate to DB
* ``pass`` - Password for DB authentication
* ``db`` - Database to use

When running actions, you can pass in the name of a connection, e.g.
``st2 run mysql.select connection="community" query="select * from foobar"``

Alternatively, when running an action, you can pass in the hostname, db, user, passwd
parameters.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* ``select`` - Run a DB query
* ``insert`` - Insert new entries
