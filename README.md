# Property Geo Insights

This is a Django-based backend platform for managing real estate properties along with geospatial intelligence on nearby amenities (schools, hospitals, malls, etc) and surrounding regions (parks, lakes, treatment plants, etc).

It leverages POSTGIS, GeoDjango, and Django REST Framework to power spatial queries and APIs for smart property discovery.

# Features

- Property Management with Geolocation
- Nearby Amenities
- Surrounding Regions
- API support via DRF


# Tech Stack

- Django, Django REST Framework, PostgreSQL, PostGIS



<!-- GETTING STARTED -->
## Getting Started

# 1. Install System Packages

You’ll need:

* PostgreSQL

* PostGIS extension

* Python 3.10+

* virtualenv or venv

### Ubuntu / Debian:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib postgis libpq-dev
```

### Mac OS:
```
brew install postgresql
brew install postgis
brew services start postgresql
```

### Create Database & PostGIS Extension
```
# Login to Postgres
sudo -u postgres psql

# In psql shell:
CREATE DATABASE <DB_NAME>;
CREATE USER <DB_USER> WITH PASSWORD '<DB_PASSWORD>';
GRANT ALL PRIVILEGES ON DATABASE <DB_NAME> TO <DB_USER>;
ALTER DATABASE <DB_NAME> OWNER TO <DB_USER>;
\c <DB_NAME>
CREATE EXTENSION postgis;
\q
```



### Project Setup
1. Clone Repository

```
git clone https://github.com/akshaybabu09/property-geo-insights.git
cd property-geo-insights
```

2. Set Up Python Environment

```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run Migrations and create superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Run Server
```
python manage.py runserver
```
Go to http://127.0.0.1:8000/admin/



### Troubleshooting
If you need to install GEOS, GDAL, etc

On Ubuntu
```
sudo apt install binutils libproj-dev gdal-bin libgdal-dev libgeos-dev
```

Mac OS
```
brew install gdal proj geos
```

