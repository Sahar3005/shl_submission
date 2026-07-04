from services.recommendation import recommend

results = recommend(
    "Hiring a Java developer with stakeholder communication skills"
)

for r in results:
    print("-" * 50)
    print("Name:", r["name"])
    print("URL:", r["url"])
    print("Duration:", r["duration"])
    print("Remote:", r["remote"])
    print("Keywords:", r["keywords"])