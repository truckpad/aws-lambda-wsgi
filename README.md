aws-lambda-wsgi
===============

A WSGI adapter for AWS API Gateway/Lambda Proxy Integration
-----------------------------------------------------------

AWS-Lambda-WSGI allows you to use WSGI-compatible middleware and frameworks like Bottle, Django and Flask with the [AWS API Gateway/Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html).

Based on [awsgi, by Matthew Wedgwood](https://github.com/slank/awsgi).

Installation
------------

`aws_lambda_wsgi` is available from PyPI as `aws_lambda_wsgi`:

```
pip install aws_lambda_wsgi
```

Example
-------

```python
import aws_lambda_wsgi
from bottle import Bottle

app = Bottle()


@app.route('/')
def index():
    return {'message': 'OK'}


def lambda_handler(event, context):
    return aws_lambda_wsgi.response(app, event, context)
```