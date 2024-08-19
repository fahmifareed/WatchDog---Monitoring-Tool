#Check command in Zabbix: sed -n 's/^real\ //p' /tmp/ftp_gfk_time

LSTIMER="ls[[:space:]]/sbobj/FTP/gfk"
TIMEOP="/tmp/ftp_gfk_time"
FTPPATH="/sbobj/FTP/gfk"

ps -ef| grep -v grep |grep -e "$LSTIMER" > /dev/null
result=$?
if [ "${result}" -ne 0 ] ; then
        /usr/bin/time -p -o $TIMEOP ls $FTPPATH 1> /dev/null
else
        echo "real 600.00" > $TIMEOP
fi