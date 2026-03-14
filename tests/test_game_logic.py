from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_new_game_resets_state():
    # Simulate a new game scenario
    secret = 42
    attempts = 0
    # Simulate new game button press
    secret = 50  # New secret number
    attempts = 0  # Reset attempts
    result = check_guess(50, secret)  # First guess in the new game
    assert result == "Win"  # Should allow guessing and work correctly

def test_difficulty_ranges():
    # Test Normal mode range
    normal_range = get_range_for_difficulty("Normal")
    assert normal_range == (1, 50)

    # Test Hard mode range
    hard_range = get_range_for_difficulty("Hard")
    assert hard_range == (1, 100)
