from unittest.mock import patch

from roll.roll_dice import roll

@patch("random.randint")
def test_single_roll(mockobject, capsys):

    mockobject.return_value = 5
    
    out = roll("1d10")

    mockobject.assert_called()


    assert out == '5\n= 5\n'

    mockobject.return_value = 2
    
    out = roll("d10")

    mockobject.assert_called()

    assert out == '2\n= 2\n'

@patch("random.randint")
def test_multiple_rolls(mockobject, capsys):

    mockobject.return_value = 5
    
    out = roll("5d10")

    mockobject.assert_called()

    assert out == '5 + 5 + 5 + 5 + 5\n= 25\n'
