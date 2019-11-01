# REPORT

## To Build
This app has a simple dockerisation, to build run;
```bash
docker-compose build
```

## To Run
To start the app run
```bash
docker-compose up -d
```

## To upload data
To upload data, exec into the backend via;
```bash
docker-compose build
```

and then run the upload command
```bash
python manage.py import --user_filepath <user_filepath> --consumption_folderpath <consumption_folderpath>
```
You can choose to upload  one or both data types at a time.

## To View
Navigate to http://localhost:3000/


## To View Logs
```bash
docker-compose logs -f <container_name>
```
Where containers are backend and frontend


## To Stop
```bash
docker-compose down
```


## Notes on decisions

### Backend

* Used pandas to open csvs (backed/src/consumption/utils.py csv_to_df) because can create dict with header name
* Created the function get_or_create (backend/src/consumption/operations/import_data.py), with a lookup dict to avoid using djangos get_or_create continuously, since this is less efficient than a dictionary lookup
* Created a dict with the foreign key obj instead of name for speed, could also have done this via a custom serializer with a Slug that loads from the name
* input df into import_user_data and import_consumption_data because easier to test than a file, file opening handled a level above
* Removed zone by setting USE_TZ = False, didn't seem necessary here

### Frontend

* Simple material ui theme
* Using functions and hooks instead of containers
* Not very pretty because of short time... but functional skeleton?
* Could be improvements to make it more function + typing
* Actions are very verbose and repetitive -> would be better to have a general factory for this


## Screenshots
There are two screen shots in the documentation folder at the top level.