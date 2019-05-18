#! /usr/bin/env python
#coding=utf-8
import pytest
import codecs


@pytest.mark.datafiles(
    'test1.txt',
    'test2.txt',
    'test3.txt'
    )
def test_find_borders(datafiles):
    for txt in datafiles.listdir():
        with codecs.open(txt,'r',encoding='utf8') as f:
            content = f.read()
            assert "Hello" in content

