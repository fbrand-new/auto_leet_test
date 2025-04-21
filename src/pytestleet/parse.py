def parse_result(result: dict) -> str:
    if "question" not in result:
        raise ValueError("Invalid test case format: 'question' key not found.")
    if "sampleTestCase" not in result["question"]:
        raise ValueError("Invalid test case format: 'sampleTestCase' key not found.")
    if "codeSnippets" not in result["question"]:
        raise ValueError("Invalid test case format: 'codeSnippets' key not found.")
    if "content" not in result["question"]:
        raise ValueError("Invalid test case format: 'content' key not found.")

    content = result["question"]["content"]

    return content


def extract_tests(content: str) -> list:
    """
    Extracts test cases from the content string.
    """
