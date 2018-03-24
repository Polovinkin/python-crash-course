invite_list = ["Bobby", "Albert", "Donald"]

print("\nDear " + invite_list[0] + ", I kindly invite you to my dinner that evening at my mansion!")
print(invite_list[1] + ", it would be a honor to see you on my dinner that evening.")
print("Sir " + invite_list[2] + ", I'd like to invite you to the dinner at my house that evening.")

print("\nUnfortunately " + invite_list[2] + " is to busy to attend the dinner, and we are inviting more guests")

invite_list.insert(0, "Antonio")
invite_list.insert(2, "Fidel")
invite_list.append("Vladimir")

print("\nWell, it's boring to spend time on this simple exercise, going further for real stuff, so it's the final list:")
print(invite_list)