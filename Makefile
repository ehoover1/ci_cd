install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

lint:
    pylint --disable=R,C ci_cd_script.py

test:
    python -m pytest -vv --cov=hello ci_cd_test

make install lint test
