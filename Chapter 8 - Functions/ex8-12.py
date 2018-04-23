def sandwich(*ingredient):
    print("Making your sandwich with:")
    for item in ingredient:
        print("- " + item)

sandwich('meat', 'cheese', 'onion', 'bacon')