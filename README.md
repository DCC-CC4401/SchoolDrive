# SchoolDrive

## Pasito a Pasito
### Step 1
Clonar el repositorio.
### Step 2
Crear un ambiente virtual en la carpeta del repo:
```
python -m venv .venv
```

### Step 3
Activar el ambiente:
Windows:
```
. .\.venv\Scripts\Activate.ps1
```
Linux:
```
source .venv/bin/activate
```

### Step 4
Instalar Django
```
pip install Django 
```

### Step 5
Hacer migraciones
```
python manage.py makemigrations

python manage.py migrate
```

### Step 6
Run Run 
```
python manage.py runserver
```
