python -m venv myvenv
myvenv\Scripts\activate
cd my-first-blog
python -m pip install --upgrade pip
pip install django

pip freeze > requirements.txt
pip install -r requirements.txt
python -m pip install -r requirements.txt

python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver

git init
git config --global user.name "Steve"
git config --global user.email sjpearce@gmail.com

$commit = get-date
git status
git add --all .
git commit -m $commit
git push -u origin master

