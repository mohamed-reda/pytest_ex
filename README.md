#Running all tests:

cd tests

pytest


----
The -x flag: stop after first failure:

pytest -x

----
Run the test class TestRowToList :

pytest data/test_processing_helpers.py::TestRowToList

----
Run the unit test fun():

pytest data/test_preprocessing_helpers.py::TestRowToList::fun

----
Supports Python logical operators (run all in TestSplit but not fun):

pytest -k "TestSplit and not fun"

----

to run jupyter:

jupyter notebook

(Use Control-C to stop this server)
----
pip install -r requirements.txt

pip install notebook

python -m notebook

---
memory profile:

@memory_profiler.profile

python -m memory_profiler main.py

---

from line_profiler_pycharm import profile

@profile

python -m line_profiler main.py.lprof > results.txt
