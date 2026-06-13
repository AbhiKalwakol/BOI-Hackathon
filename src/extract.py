from androguard.misc import AnalyzeAPK


def extract_features(apk_path):

    with open("data/feature_list.txt", "r") as f:
        feature_names = [line.strip() for line in f]

    a, d, dx = AnalyzeAPK(apk_path)

    feature_set = set()

    # ----------------------------------
    # Permissions
    # ----------------------------------

    permissions = a.get_permissions()

    for permission in permissions:

        permission = permission.split(".")[-1]

        feature_set.add(permission)

    # ----------------------------------
    # Activities
    # ----------------------------------

    for activity in a.get_activities():
        feature_set.add(activity)

    # ----------------------------------
    # Services
    # ----------------------------------

    for service in a.get_services():
        feature_set.add(service)

    # ----------------------------------
    # Receivers
    # ----------------------------------

    for receiver in a.get_receivers():
        feature_set.add(receiver)

    # ----------------------------------
    # API Calls / Class References
    # ----------------------------------

    for method in dx.get_methods():

        try:

            method_analysis = method.get_method()

            class_name = str(
                method_analysis.get_class_name()
            )

            method_name = str(
                method_analysis.get_name()
            )

            feature_set.add(method_name)

            feature_set.add(class_name)

        except Exception:
            pass

    # ----------------------------------
    # Build Vector
    # ----------------------------------

    vector = []

    for feature in feature_names:

        if feature in feature_set:
            vector.append(1)

        else:
            vector.append(0)
    print("\nSample Extracted Features:\n")

    count = 0

    for feature in feature_set:

        print(feature)

        count += 1

        if count >= 100:
            break

    return vector