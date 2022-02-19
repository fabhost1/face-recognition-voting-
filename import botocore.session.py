import botocore.session
session = botocore.session.get_session()

session.get_credentials().access_key
'AKIAABCDEF6RWSGI234Q'

session.get_credentials().secret_key
'abcdefghijkl+123456789+qbcd'

session.get_config_variable('region')
'us-east-1'
