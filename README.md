# Inventory-Management

## Getting Started

These instructions will get you started on running the webserver. 

You need to install django 3.0 first. [Click here](https://docs.djangoproject.com/en/3.0/intro/install/) for instructions
on how to install django.  

Once django is installed, all you need to do is clone this repository.

```bash
$ git clone https://github.com/mankey101/Inventory-Management.git
```

After this, enter the following commands to run the webserver:
```bash
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
```

You can change 8000 to any port you want this server to listen to. 

You might need to allow firewall access to this webserver.

## Functionality

There are two cateogories of users: admin and non-admin. Non-admin users can currently book rooms for 1 hour.

Admin users can issue/return institute inventory (for e.g. Club equipment, sports equipment etc.) to students. 
This can be useful in settings where students have to show their ID cards to get such equipment issued.  

### Creating an admin user

Type:
```bash
$ python manage.py createsuperuser
```
to create a user as admin. 

They can login to the admin panel at http://webserver/admin

## Built With

* django 3.0
* sqlite

## Authors

* Supreet Singh
* Mayank Hooda
* Supraj Bachawala

## License

New BSD License

## Acknowledgements

* Django docs
* Stackoverflow :)