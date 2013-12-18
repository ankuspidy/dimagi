# Dimagi [applicant exercises](http://www.dimagi.com/about/careers/exercises/)

Setup:
```sh
$ git clone https://github.com/millerdev/dimagi.git
$ mkvirtualenv dimagi
```


## Numeric Converter

```sh
$ pip install nose
$ nosetests numconvert.py # run tests to verify functionality
$ python -c 'from numconvert import *; print(convert_to_spoken(7291642))'
```

Review [source code](numconvert.py) if desired.


## Math Engine

```sh
$ pip install bottle
$ python -m bottle matheng # start web server
```

1. Open `http://localhost:8080/?values=[1, 4, 7, -2]` in a web browser.
2. Next go to `http://localhost:8080/entry` and submit a list of numbers such
   as `[2, 2]`.
3. Use the Back button to go back and post a few more.
4. Go to `http://localhost:8080/history` to see details about most recent
   calculation.
5. Go to `http://localhost:8080/history/3` to see three most recent
   calculations.

Finally, have a look at [the code](matheng.py). It is minimal, but should meet
all the requirements outlined on the exercises page.
