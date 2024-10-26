# RESTful API - Python
This section of code is to create a RESTful API using Python which transmit the input CSV file data into a transformed version.

## Python as FLASK server
The whole code is developed in Python with the help of the module 'FLASK' which aids in creating and maintaining a FLASK web server to host the data.

### Data Transfromation
The raw CSV file is taken as the input in Python and transformed according to the needs.
Hourly average speed of the CARS are being caluculated using 'GROUPBY()' method and transmitted as JSON in the FLASK WEB SERVER.

## Browser as the client
After being transformed and hosted in the web server, browser (other any other API tool) is used as the client to request the data using GET method.
The data is hosted in 'http://127.0.0.1:5000/message' route path.
As being requested by the client, the result transformed JSON is being shown in the site.

## Output
The output is a nested json where the first level represents the 'CAR TYPE' and the next level represents 'DAY' and the next represents 'Hour'.
```
Output JSON
├─── Car Type
│    └─── Day
|       └─── Hour
|          └─── Average speed value
```

