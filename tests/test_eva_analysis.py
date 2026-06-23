import pytest
from eva_data_analysis import text_to_duration, calculate_crew_size

def test_text_to_duration_integer():
    """Test function returns expected true value for durations
    with whole hour durations."""
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

def test_text_to_duration_float():
    """Test that function returns expected ground truth values
    with a non-zero minute componant."""
    assert text_to_duration("10:20") == pytest.approx(10.333333)

@pytest.mark.parametrize(
    "input_value, expected_result",
    [
        ("Valentina Tereshkova;", 1),
        ("Judith Resnik; Sally Ride;", 2),
    ],
)
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected ground truth values
    for edge case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None
