import lab7q3
from io import StringIO
from sys import stderr

def generate_value(a=0, b=0):
  if a == 5 and b == 20:
    return 10
  elif a == 5 and b ==30:
    return 6
  elif a == 25 and b == 50:
    return 26
  elif a == 1 and b ==25:
    return 5
  else:
    return 8
  
def test_case1(monkeypatch, capsys):
    
    number_inputs = StringIO('1\n16\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'Correct') != -1


def test_case2(monkeypatch, capsys):
    
    number_inputs = StringIO('1\n18\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'16') != -1

def test_case3(monkeypatch, capsys):
    
    number_inputs = StringIO('2\n21\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'Correct') != -1

def test_case4(monkeypatch, capsys):
    
    number_inputs = StringIO('2\n28\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'21') != -1

def test_case5(monkeypatch, capsys):
    
    number_inputs = StringIO('4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    ans, cor = lab7q3.showAddition()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert ans == 4
    assert cor == 16

def test_case6(monkeypatch, capsys):
    
    number_inputs = StringIO('4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    ans, cor = lab7q3.showSubstraction()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert ans == 4
    assert cor == 21

def test_case7(monkeypatch, capsys):
    
    number_inputs = StringIO('4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q3.evaluation(12, 12)
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'Correct!') != -1

def test_case8(monkeypatch, capsys):
    
    number_inputs = StringIO('4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q3.evaluation(12, 13)
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'13') != -1