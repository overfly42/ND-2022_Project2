from adder import add
from hello import hello
from click.testing import CliRunner

def test_add():
    total = add(2,3)
    assert total == 5

def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello,['--name','Thor','--color','blue'])
    assert 'Thor' in result.output

def test_hello2():
    runner = CliRunner()
    result = runner.invoke(hello,['--name','Thor','--color','blue'])
    assert 'Bob' in result.output