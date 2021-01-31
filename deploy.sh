#!/bin/zsh
cat ~/iCloud/passwd/ssh | read passwd
echo '\n1. ---pull db.sqlite3 from server---'
sshpass -p $passwd scp root@119.28.186.136:/var/www/django_blog/db.sqlite3 ~/iCloud/django_blog/db.sqlite3
echo '\n2. ---collect static files---'
echo 'yes' | python3 manage.py collectstatic
echo '\n3. ---migrate to database---'
python3 manage.py makemigrations blog
python3 manage.py migrate
echo '\n4. ---push django_blog to server---'
sshpass -p $passwd rsync -av --exclude={'blog_env','__pycache__'} ~/iCloud/django_blog/ root@119.28.186.136:/var/www/django_blog
