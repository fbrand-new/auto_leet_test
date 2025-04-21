import pytest
from pytestleet.scrape import fetch_question


@pytest.mark.integration
def test_fetch_test_case():
    """
    Tests that fetch test case returns a valid test case.
    """
    try:
        test_case = fetch_question("two-sum", save_offline=True)
        assert isinstance(test_case, dict)
        assert "question" in test_case
        assert "sampleTestCase" in test_case["question"]
        assert "codeSnippets" in test_case["question"]
        assert "content" in test_case["question"]
        assert isinstance(test_case["question"]["codeSnippets"], list)
        assert isinstance(test_case["question"]["sampleTestCase"], str)
        assert len(test_case["question"]["sampleTestCase"]) > 0
    except Exception as e:
        pytest.fail(f"fetch_problem_test_case failed with exception: {e}")
