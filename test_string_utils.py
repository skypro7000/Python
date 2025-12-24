import pytest
from string_utils import StringUtils

class TestStringUtils:

    
    @pytest.mark.parametrize("input_value, expected", [
        ("", True),
        (None, True),
        ("Тест", False),
        (" ", False)
    ])
    def test_is_empty(self, input_value, expected):
        assert StringUtils.is_empty(input_value) == expected

    
    @pytest.mark.parametrize("input_value, expected", [
        ("", True),
        (None, True),
        (" ", True),
        ("Тест", False),
        ("  Тест  ", False)
    ])
    def test_is_blank(self, input_value, expected):
        assert StringUtils.is_blank(input_value) == expected

    
    @pytest.mark.parametrize("input_value, expected", [
        ("abc", "cba"),
        ("123", "321"),
        ("", ""),
        (None, None)
    ])
    def test_reverse(self, input_value, expected):
        assert StringUtils.reverse(input_value) == expected

    
    @pytest.mark.parametrize("input_value, expected", [
        ("abc", "ABC"),
        ("Тест", "ТЕСТ"),
        ("", ""),
        (None, None)
    ])
    def test_to_upper(self, input_value, expected):
        assert StringUtils.to_upper(input_value) == expected

    
    @pytest.mark.parametrize("input_value, sep, expected", [
        (["a", "b", "c"], ",", "a,b,c"),
        (["123", "456"], "-", "123-456"),
        ([], ",", None),
        (None, ",", None)
    ])
    def test_join_strings(self, input_value, sep, expected):
        assert StringUtils.join_strings(input_value, sep) == expected
