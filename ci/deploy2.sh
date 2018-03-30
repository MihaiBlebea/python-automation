
FTP_USER=pi
FTP_PASSWORD=highprotein07

FTP_HOST=192.168.1.23
REMOTE_PATH=./Projects/project

lftp -c "open -u $FTP_USER,$FTP_PASSWORD $FTP_HOST; set ssl:verify-certificate no; mirror -R ./ $REMOTE_PATH"