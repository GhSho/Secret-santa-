import random

# List of participants and their base names
participants_base = [
    "Vivek", "Hema", "Pachu", "Gehnna", "Acchu", "Deepi", "Shaunak",
    "Lalitha", "Prashant", "Shalu", "Radhika", "Sapna", "Hemi",
    "Vaishu", "Charmee", "Satish", "Usha", "Nayan", "Smitha"
]

# Generate random two-digit numbers (not 1-20 and no duplicates)
random_numbers = random.sample(range(21, 100), len(participants_base))

# Assign usernames by combining names with numbers
usernames = [f"{name}{num}" for name, num in zip(participants_base, random_numbers)]

# Shuffle the recipients
recipients = participants_base.copy()
while True:
    random.shuffle(recipients)
    # Ensure no one is gifting to themselves
    if all(giver.split(str(giver[-2:]))[0] != recipient for giver, recipient in zip(usernames, recipients)):
        break

# Create the gifting mapping
gifting_mapping = dict(zip(usernames, recipients))

# Save the gifting mapping to a file
gifting_mapping_file = "gifting_mapping.py"
with open(gifting_mapping_file, "w") as f:
    f.write("gifting_mapping = " + str(gifting_mapping))

# Save the unique user IDs to a separate file
user_ids_file = "user_ids.txt"
with open(user_ids_file, "w") as f:
    for user_id in usernames:
        f.write(user_id + "\n")

print(f"Gifting mapping has been saved to {gifting_mapping_file}.")
print(f"User IDs have been saved to {user_ids_file}.")
