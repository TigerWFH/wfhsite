import multiprocessing

bind = "127.0.0.1:8080"  # The socket to bind
workers = multiprocessing.cpu_count(
) * 2 + 1  # The number of worker processes（进程） for handling requests
threads = 4  # The number of worker threads（线程） for handling requests.
timeout = 1800  # Workers silent for more than this many seconds are killed and restarted
graceful_timeout = 10
worker_class = 'gevent'  # 使用gevent(协程)模式，还可以使用sync 模式，默认的是sync模式
loglevel = 'debug'
# 进程名称
proc_name = "wfhsite"

# LOG_DIR=str(Path(__file__).resolve().parent / )
# access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# errorlog = LOG_DIR
# infolog = LOG_DIR
# max_requests = 12  # The maximum number of requests a worker will process before restarting.
# keepalive = 2  # The number of seconds to wait for requests on a Keep-Alive connection.
