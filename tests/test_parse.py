import pytest
from pytestleet.parse import parse_result


def test_parse_result_correct():
    """
    Tests that parse_result returns a valid test case.
    """
    test_case = {
        "question": {
            "sampleTestCase": "Input: [1,2,3]\nOutput: 6",
            "codeSnippets": [
                {
                    "lang": "python3",
                    "langSlug": "python3",
                    "code": "def add(a, b): return a + b",
                }
            ],
            "content": "<p>Given an array of integers, return the sum.</p>",
        }
    }

    try:
        result = parse_result(test_case)
        assert isinstance(result, str)
        assert len(result) > 0
    except Exception as e:
        pytest.fail(f"parse_result failed with exception: {e}")


def parse_result_incorrect():
    """
    Tests that parse_result raises ValueError for incorrect test case format.
    """
    test_case = {
        "question": {
            "sampleTestCase": "Input: [1,2,3]\nOutput: 6",
            "codeSnippets": [
                {
                    "lang": "python3",
                    "langSlug": "python3",
                    "code": "def add(a, b): return a + b",
                }
            ],
        }
    }

    with pytest.raises(ValueError):
        parse_result(test_case)
