from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


def fetch_question(problem_name: str, save_offline=False) -> str:
    """
    Fetches the test case for a given problem name from LeetCode.
    """
    transport = AIOHTTPTransport(url="https://leetcode.com/graphql")
    client = Client(transport=transport, fetch_schema_from_transport=False)

    query = gql(
        """
        query getTestCase($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                sampleTestCase
                content
                codeSnippets{
                    lang
                    langSlug
                    code
                }
            }
        }
        """
    )

    result = client.execute(
        query, variable_values={"titleSlug": problem_name, "lang": "python3"}
    )

    if save_offline:
        with open(f"{problem_name}.json", "w") as f:
            import json

            json.dump(result, f, indent=4)

    return result
