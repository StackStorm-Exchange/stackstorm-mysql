# Changelog
# 0.6.3

- Addresses #20 - Fixing compatibility for Str/Byte data (Py 2.7 -> 3.x).

# 0.6.2

- update iteritems() to be compatible with python 3.6 and backwards compatible with 2.7

# 0.6.1

- Password fields are now secrets

# 0.6.0

- Use mysqlclient package instead of MySQLdb1

# 0.5.2

- Fix Unicode issues with mysql.insert

# 0.5.0

- Updated action `runner_type` from `run-python` to `python-script`

## 0.4.1

- Raise Exception if MySQL returns an error

## 0.4.0

- Rename `config.yaml` to `config.schema.yaml` and update to use schema.
- Existing users will need to update configuration
