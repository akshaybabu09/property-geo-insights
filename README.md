# Property Geo Insights

This is a Django-based backend platform for managing real estate properties along with geospatial intelligence on nearby amenities (schools, hospitals, malls, etc) and surrounding regions (parks, lakes, treatment plants, etc).

It leverages POSTGIS, GeoDjango, and Django REST Framework to power spatial queries and APIs for smart property discovery.


# Problem Statement

Consider a Spatial data platform where you are writing the backend APIs to perform different spatial Queries and storing spatial datasets. Please use any backend technology like Node.js or Python to design and develop the REST API or Graph QL to achieve the below-mentioned features.

1. Create a backend API for storing, updating and retrieving the spatial based multiple point data.
2. Create a backend API for storing, updating and retrieving the spatial based multiple polygon data.


# Features

- Property Management with Geolocation
- Nearby Amenities
- Surrounding Regions
- API support via DRF


# Tech Stack

- Django, Django REST Framework, PostgreSQL, PostGIS



<!-- GETTING STARTED -->
# Getting Started

## 1. Install System Packages

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

## 2. Create Database & PostGIS Extension
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



## 3. Project Setup
### 1. Clone Repository

```
git clone https://github.com/akshaybabu09/property-geo-insights.git
cd property-geo-insights
```

### 2. Set Up Python Environment

```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Add Environment Variables

.env
```
SECRET_KEY=<SECRET_KEY>
DB_NAME=<DATABASE_NAME>
DB_USER=<DATABASE_USER>
DB_PASSWORD=<DATABASE_PASSWORD>
DB_HOST=<DATABASE_HOST>
```

### 4. Run Migrations and create superuser

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run Server

```
python manage.py runserver
```
Go to http://127.0.0.1:8000/admin/



## 4. Troubleshooting
If you need to install GEOS, GDAL, etc

On Ubuntu
```
sudo apt install binutils libproj-dev gdal-bin libgdal-dev libgeos-dev
```

Mac OS
```
brew install gdal proj geos
```

