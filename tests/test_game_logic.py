import sys
from unittest.mock import MagicMock

# Mock streamlit before importing app so module-level st.* calls don't crash pytest
sys.modules["streamlit"] = MagicMock()

from app import check_guess, update_score, get_range_for_difficulty, parse_guess


# ---------------------------------------------------------------------------
# check_guess — BUG FIX: hint messages were swapped
# "Too High" used to say "Go HIGHER!" and "Too Low" used to say "Go LOWER!"
# ---------------------------------------------------------------------------

def test_check_guess_win_returns_correct_outcome():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_win_returns_correct_message():
    _, message = check_guess(50, 50)
    assert "Correct" in message

def test_check_guess_too_high_outcome():
    # Guess is above secret — outcome must be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_check_guess_too_high_message_says_lower():
    # BUG FIX: was "Go HIGHER!" — must now direct player downward
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_check_guess_too_low_outcome():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_too_low_message_says_higher():
    # BUG FIX: was "Go LOWER!" — must now direct player upward
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# ---------------------------------------------------------------------------
# check_guess — BUG FIX: secret was cast to str on even attempts,
# causing string-based ordering ("9" > "50" is True alphabetically)
# ---------------------------------------------------------------------------

def test_check_guess_integer_comparison_not_string():
    # "9" > "50" alphabetically (string bug) but 9 < 50 numerically (correct)
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low", "Integer 9 is less than 50 — must use numeric comparison"

def test_check_guess_two_digit_boundary():
    # Another case where string sort differs: "19" < "9" but 19 > 9 numerically... wait no
    # "100" < "50" alphabetically but 100 > 50 numerically
    outcome, _ = check_guess(100, 50)
    assert outcome == "Too High"


# ---------------------------------------------------------------------------
# update_score — BUG FIX: "Too High" on even attempts awarded +5 points.
# A wrong guess should NEVER increase the score.
# ---------------------------------------------------------------------------

def test_update_score_too_high_always_deducts_on_even_attempt():
    # BUG FIX: even attempt numbers used to return current_score + 5
    score = update_score(100, "Too High", attempt_number=2)
    assert score < 100, "Wrong guess on even attempt must not award points"

def test_update_score_too_high_always_deducts_on_odd_attempt():
    score = update_score(100, "Too High", attempt_number=3)
    assert score < 100

def test_update_score_too_low_always_deducts():
    score = update_score(100, "Too Low", attempt_number=2)
    assert score < 100

def test_update_score_win_awards_points():
    score = update_score(0, "Win", attempt_number=1)
    assert score > 0

def test_update_score_win_minimum_10_points():
    # Win on a very late attempt should still award at least 10 points
    score = update_score(0, "Win", attempt_number=100)
    assert score >= 10


# ---------------------------------------------------------------------------
# get_range_for_difficulty — BUG FIX: hint message and new game button
# both hardcoded (1, 100) regardless of difficulty
# ---------------------------------------------------------------------------

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20)

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert (low, high) == (1, 50)

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 100)

def test_easy_range_is_smaller_than_normal():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high

def test_normal_range_is_smaller_than_hard():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert normal_high < hard_high


# ---------------------------------------------------------------------------
# parse_guess — validates input parsing handles edge cases correctly
# ---------------------------------------------------------------------------

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_none_input():
    ok, value, _ = parse_guess(None)  # type: ignore[arg-type]
    assert ok is False
    assert value is None

def test_parse_guess_empty_string():
    ok, _, _ = parse_guess("")
    assert ok is False

def test_parse_guess_non_number():
    ok, _, err = parse_guess("abc")
    assert ok is False
    assert err is not None
    assert "not a number" in err.lower()

def test_parse_guess_float_string_truncates_to_int():
    # "3.9" should parse as 3, not raise an error
    ok, value, _ = parse_guess("3.9")
    assert ok is True
    assert value == 3
