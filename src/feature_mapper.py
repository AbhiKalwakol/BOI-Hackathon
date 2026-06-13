def categorize_features(feature_names):

    categories = {
        "permissions": [],
        "intents": [],
        "apis": [],
        "other": []
    }

    for feature in feature_names:

        if feature.startswith("android.intent"):
            categories["intents"].append(feature)

        elif feature.isupper():
            categories["permissions"].append(feature)

        elif "." in feature:
            categories["apis"].append(feature)

        else:
            categories["other"].append(feature)

    return categories