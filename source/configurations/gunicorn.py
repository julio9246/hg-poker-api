access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
accesslog = '-'
bind = '0.0.0.0:5000'
errorlog = '-'
loglevel = 'info'
timeout = 60
worker_class = 'sync'
workers = 4
