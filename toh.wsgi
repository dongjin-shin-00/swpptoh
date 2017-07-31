[uwsgi]
chdir=/home/lastone817/toh
module=toh.wsgi:application
master=true
processes=10
vacuum=true
max-requests = 5000
socket = /tmp/toh.sock
chmod-socket = 666
daemonize=/home/lastone817/toh/toh.log
pidfile=/home/lastone817/toh/toh.pid
