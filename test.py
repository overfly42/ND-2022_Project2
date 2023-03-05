'''
    Some tests
'''
from click.testing import CliRunner
from adder import add
from hello import hello

def test_add():
    '''
        testing the add function
    '''
    total = add(2,3)
    assert total == 5

def test_hello():
    '''
        testing Thor
    '''
    runner = CliRunner()
    result = runner.invoke(hello,['--name','Thor','--color','blue'])
    assert 'Thor' in result.output

def test_hello2():
    '''
        testing Bob
    '''
    runner = CliRunner()
    result = runner.invoke(hello,['--name','Bob','--color','blue'])
    assert 'Bob' in result.output
    