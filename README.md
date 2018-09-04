aws-lambda-wsgi
===============

A WSGI adapter for AWS API Gateway/Lambda Proxy Integration
-----------------------------------------------------------

AWS-Lambda-WSGI allows you to use WSGI-compatible middleware and frameworks like Bottle, Django and Flask with the [AWS API Gateway/Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html).

[Based on awsgi, by Matthew Wedgwood](<https://github.com/slank/awsgi).

Installation
------------

`aws-lambda-wsgi` is available from PyPI as `aws-lambda-wsgi`:

```
pip install aws-lambda-wsgi
```

Example
-------

```python
import awsgi
from bottle import Bottle

app = Bottle()


@app.route('/')
def index():
    return jsonify(status=200, message='OK')


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
```
