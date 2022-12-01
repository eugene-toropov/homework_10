import json


def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for candidate in load_candidates():
        if pk == candidate["pk"]:
            return candidate
    return


def get_by_skill(skill_name):
    candidates_with_skill = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate["skills"].lower().split(','):
            candidates_with_skill.append(candidate)
    return candidates_with_skill









