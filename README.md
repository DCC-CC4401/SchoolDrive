# SchoolDrive

## Pasito a Pasito
### Step 1
Clonar el repositorio.
```postscript
git clone https://github.com/DCC-CC4401/SchoolDrive.git
```
### Step 2
Crear un ambiente virtual en la carpeta del repo:
```postscript
python -m venv .venv
```

### Step 3
Activar el ambiente:
Windows | Linux
--- | ---
` venv\Scripts\activate ` | ` source .venv/bin/activate `

### Step 4
Instalar requerimientos
```
pip install -r requirements
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

### Adicional
Crear un admin:
```
python manage.py createsuperuser 
```