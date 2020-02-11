# Sample microservices architecture using python flask and sql alchemy

## Movies service

### Run
* To start the micro-service, go in the **movies** directory: <code>$ cd movies</code>
* Create a python3 virtual environment: <code>$ python3 -m venv movies_service</code>
* Install dependencies from requirements.txt file:<code>$ pip install -r requirements.txt</code>
* Initialize the database:<code>$ flask initdb</code>
* Run the server: <code>$ flask run</code>

Movies service runs on http://127.0.0.1:5000/

### Test
To list all available routes you can run <code>$ flask routes</code>

To test the different routes you can do as follows:
* Open a python terminal : <code>$ python</code>
* Import requests package : <code>$ import request</code>
```python
import request
```
* Create a request : <code>$ request = "" import request</code>


* Create a python3 virtual environment: <code>$ python3 -m venv movies_service</code>
* Install dependencies from requirements.txt file:<code>$ pip install -r requirements.txt</code>
* Initialize the database:<code>$ flask initdb</code>
* Run the server: <code>$ flask run</code>