#!/usr/bin/env bash

. ~/local_vars.sh
cd ~/backups/
FILENAME="ttn_`date +'%Y%m%d_%H%M%S'`.sql.gz"
mysqldump $MYSQL_DB -u $MYSQL_USER -p$MYSQL_PASSWORD | gzip > ttn_`date +"%Y%m%d_%H%M%S"`.sql.gz
scp -P $BACKUP_PORT $FILENAME "$BACKUP_SERVER"
