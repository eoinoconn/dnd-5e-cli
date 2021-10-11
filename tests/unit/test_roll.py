from unittest.mock import patch

from roll.roll_dice import roll_dice

@patch("random.randint")
def test_single_roll(mockobject, capsys):

    mockobject.return_value = 5
    
    roll_dice("1d10")

    mockobject.assert_called()

    captured = capsys.readouterr()
    assert captured.out == '5\n= 5\n\n\n'

    mockobject.return_value = 2
    
    roll_dice("d10")

    mockobject.assert_called()

    captured = capsys.readouterr()
    assert captured.out == '2\n= 2\n\n\n'

@patch("random.randint")
def test_multiple_rolls(mockobject, capsys):

    mockobject.return_value = 5
    
    roll_dice("5d10")

    mockobject.assert_called()

    captured = capsys.readouterr()
    assert captured.out == '5 + 5 + 5 + 5 + 5\n= 25\n\n\n'
