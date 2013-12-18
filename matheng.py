#! /usr/bin/env python
"""A web service that takes in a single parameter GET or POST* called
"values", which is a JSON-formatted list of numbers. The response is
a JSON dictionary with two values, the "sum" and the "product".

Usage:
$ mkvirtualenv dimagi
$ pip install bottle
$ python -m bottle [--help] matheng
"""
import json
from collections import deque
from datetime import datetime
from functools import reduce
from itertools import islice

from bottle import request, response, route, run

history = deque(maxlen=100)

@route("/", method=["GET", "POST"])
def index():
    """Perform calculations on a sequence of "values"

    The "values" parameter may be submitted using either POST or GET.
    If the submitted values can be parsed as a JSON-formatted list of
    numbers, then the response will be a JSON dictionary. Otherwise
    it will be a short text/html message describing this web service.
    """
    values = request.params.get("values")
    try:
        values = json.loads(values)
    except Exception:
        values = None
    else:
        if not isinstance(values, list):
            values = None
        if not all(isinstance(v, (int, float)) for v in values):
            values = None

    if not values:
        # print description of service
        return __doc__.split("Usage:")[0].rstrip()

    result = {
        "sum": sum(values),
        "product": reduce((lambda a, b: a * b), values, 1),
    }
    data = {
        "ip": request['REMOTE_ADDR'],
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "values": values,
    }
    data.update(result)
    history.append(data)
    return result


@route("/history")
@route("/history/<num_items:int>")
def history_(num_items=1):
    """Get a JSON-formatted list up to 100 most recent calculations

    By default, this endpoint returns a JSON-formatted list containing
    details about the most recent calculation. A second element may be
    added to the path specifying the number of items to return from
    history.

    Example: ``/history/10`` retrieve 10 most recent calculations.
    """
    response.content_type = "application/json"
    start = len(history) - num_items
    if start < 0:
        start = 0
    return json.dumps(list(islice(history, start, None)), indent=2)


@route("/entry")
def entry():
    """Entry for for testing POST method"""
    return ENTRY_FORM


ENTRY_FORM = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Entry Form</title>
  </head>
  <body>
    <form method="POST" action="/">
      <label for="values">Enter a JSON-formatted list of numbers</label>
      <input type="text" name="values" value="">
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
"""