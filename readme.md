
```
tox
```
will create new test env to test the full pipeline or test cases

for updating requirment.txt file on tox run this
```bash
tox -r
``` 
on terminal



to run pwd package or local package install

```bash
pip install -e .

```

create tar file for other machine install -- on terminal

```
python setup.py sdist bdist_wheel

``` 
Note: the dist file is missing on repository

```
flake8

``` 
is library to formatting the code. by following pep8 standerd