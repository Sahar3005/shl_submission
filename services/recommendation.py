from services.retrieval import search


def recommend(query, top_k=10):

    results = search(query, top_k * 2)

    recommendations = []

    seen = set()

    query_lower = query.lower()

    for item in results:

        score = 0

        # Name match
        if any(word in item["name"].lower() for word in query_lower.split()):
            score += 3

        # Description match
        if any(word in item["description"].lower() for word in query_lower.split()):
            score += 2

        # Keywords match
        if any(word in " ".join(item["keywords"]).lower() for word in query_lower.split()):
            score += 4

        # Remote support
        if item["remote"] == "Yes":
            score += 1

        if item["name"] not in seen:

            recommendations.append((score, item))

            seen.add(item["name"])

    recommendations.sort(key=lambda x: x[0], reverse=True)

    return [x[1] for x in recommendations[:top_k]]