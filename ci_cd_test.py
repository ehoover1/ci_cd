import pytest
from ci_cd_script import main

def test_main():
    df = main()
    assert df.iloc[0, 2] == 1952