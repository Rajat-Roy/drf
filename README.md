# Install DRF
python3 -m venv venv

source venv/bin/activate

or

venv\Scripts\activate.bat

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
