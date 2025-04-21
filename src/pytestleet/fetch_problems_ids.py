import requests
import json

max_num_questions = 3466
url = "https://leetcode.com/graphql"
problems_per_request = 100

skip = 0
question_mapping = {}

while skip < max_num_questions:
    data = {
        "operationName": "problemsetQuestionList",
        "variables": {
            "categorySlug": "all-code-essentials",
            "filters": {},
            "limit": problems_per_request,
            "skip": skip,
        },
        "query": "\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ",
    }

    r = requests.post(url, json=data)

    questions_list = r.json().get("data").get("problemsetQuestionList").get("questions")

    for i, q in enumerate(questions_list):
        question_mapping[skip + i] = q.get("titleSlug")

    skip += problems_per_request

json.dump(question_mapping, open("question_mapping.json", "w"), indent=4)
