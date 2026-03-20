# Criar um ambiente virtual para instalar o django dentro dele
python -m venv venv
./venv/Scripts/Activate.ps1
pip install django

# para rodar o server
python manage.py runserver