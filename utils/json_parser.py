import json


def parse_llm_json(response: str):

    response = response.strip()

    if response.startswith("```json"):
        response = response.replace(
            "```json",
            "",
            1
        )

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    return json.loads(response)