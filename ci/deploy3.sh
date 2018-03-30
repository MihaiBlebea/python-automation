echo $(pwd)

ssh pi@192.168.1.23 <<'ENDSSH'
echo $(pwd)
cd ~/Projects/project
rm -rf ~/Projects/project/* 
git pull origin master
ENDSSH