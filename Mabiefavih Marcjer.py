# Mabiefavih Marcjer — Dinner Invitation Program (Tasks 3-4 to 3-7)

# 3-4: create an initial guest list
invite_list = ["Richard Bona", "Blanche Bailly", "Jovi"]

# send first round of invitations
for guest in invite_list:
    print("Hello " + guest + ", you are invited to join me for dinner.")

print()

# 3-5: one person can't attend
print(invite_list[1] + " just informed me that they won’t be able to make it.")

# replace the unavailable guest
invite_list[1] = "Samuel Eto'o Jr"

# send updated invitations
for guest in invite_list:
    print("Hello " + guest + ", you are still invited to dinner.")

print()

# 3-6: more space found
print("Good news! I managed to get a bigger dinner table!")

# adding more well-known Cameroonian names
invite_list.insert(0, "Coco Argentée")  # add at the start
invite_list.insert(len(invite_list) // 2, "Ko-C")  # add in the middle
invite_list.append("Mimie")  # add at the end

# send invites again
for guest in invite_list:
    print("Greetings " + guest + ", please join me for the dinner gathering.")

print()

# 3-7: only two guests can be invited
print("Sadly, the large table won’t arrive in time. I must limit the list to two guests.")

while len(invite_list) > 2:
    removed_name = invite_list.pop()
    print("Sorry " + removed_name + ", I won’t be able to host you this time.")

print()

# final two guests
for guest in invite_list:
    print("Hello " + guest + ", you are still on the final guest list!")

# empty the final list
del invite_list[0]
del invite_list[0]

print()
print(invite_list)  # expected output: []
