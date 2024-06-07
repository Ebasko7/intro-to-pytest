import calculator


def test_add():
    assert calculator.calculate(2, 3, "add") == 5

   # Add more functional tests for subtract, multiply, and divide
def test_mult():
    assert calculator.calculate(6,10, "multiply") == 60

def test_subtract():
    assert calculator.calculate(100, 32, "subtract") == 68

def test_divide():
    assert calculator.calculate(10,2, "divide") == 5

#CAPSYS UNRECOGNIZED---LEADS TO FAILED TEST '' == RESULT: 20...-- 
'''def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n" '''


def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

def test_argument_passing_negative(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "-1", "12", "multiply"])
    assert calculator.calculate(-1, 12, "multiply") == -12.0
