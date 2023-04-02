# supervisor<https://liyangliang.me/posts/2015/06/using-supervisor/>

> Linux 运维工具 Supervisor 的安装使用（进程管理工具）
> supervisor 管理进程，是通过 fork/exec 的方式将这些被管理的进程当作 supervisor 的子进程来启动，所以我们只需要将要管理进程的可执行文件的路径添加到 supervisor 的配置文件中就好了。此时被管理进程被视为 supervisor 的子进程，若该子进程异常中断，则父进程可以准确的获取子进程异常中断的信息，通过在配置文件中设置 autostart=ture，可以实现对异常中断的子进程的自动重启。

## 安装

> pip install supervisor

> sudo apt-get install supervisor

## 配置文件

> echo_supervisord_conf: 查看配置文件

> echo_supervisord_conf > /etc/supervisord.conf 导出默认配置

> cat /etc/supervisord/supervisord.conf: 查看配置文件

```ini
; supervisor config file
[unix_http_server] ; 设置HTTP服务器监听的UNIX domain socket
file=/var/run/supervisor.sock;指向UNIX domain socket,(the path to the socket file)
chmod=0700         ; 权限，sockef file mode (default 0700)

[supervisord]; 与supervisord有关的全局配置
logfile=/var/log/supervisor/supervisord.log ; (main log file;default $CWD/supervisord.log)
pidfile=/var/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
childlogdir=/var/log/supervisor            ; ('AUTO' child log dir, default $TEMP)

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock ; use a unix:// URL  for a unix socket

; The [include] section can just contain the "files" setting.  This
; setting can list multiple files (separated by whitespace or
; newlines).  It can also contain wildcards.  The filenames are
; interpreted as relative to this file.  Included files *cannot*
; include files themselves.

[include]
files = /etc/supervisor/conf.d/*.conf
[program:x];配置文件必须包括至少一个program，x是program名称，必须写上，不能为空
; command:
; directory
; startsecs
; redirect_stderr
; stdout_logfile
; stdout_logfile_maxbytes
; stdout_logfile_backups
```

## 启动

> sudo supervisord -c supervisor.conf

## supervisor 基本命令

- `supervisord -c supervisor.conf`启动 supervisor
- `supervisorctl [-c supervisor.conf] status`查看状态
- `supervisorctl [-c supervisor.conf] reload`重新载入配置文件
- `supervisorctl [-c supervisor.conf] start [all]|[x]`启动所有指定的程序进程
- `supervisorctl [-c supervisor.conf] stop [all]|[x]` 关闭所有指定的程序进程
