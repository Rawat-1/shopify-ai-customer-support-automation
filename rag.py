def get_policy_context():

    try:
        with open(
            "data/store_policies.txt",
            "r",
            encoding="utf-8"
        ) as f:
            return f.read()

    except FileNotFoundError:
        print("Policy file not found.")

        return "No company policies available."

    except Exception as e:
        print(f"Policy Retrieval Error: {e}")

        return "No company policies available."