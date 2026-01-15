def assess_risk(age: int, cholesterol: int) -> str:
    if age > 40 and cholesterol > 200:
        return "high"
    return "low"


# The assess_risk function takes two integer parameters: age and cholesterol.
# basic logic function to assess health risk based on age and cholesterol levels.