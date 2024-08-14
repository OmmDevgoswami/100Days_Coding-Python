with open("Mail Merge Project Start\\Input\\Letters\\starting_letter.txt", "r") as file:
    letter = file.readlines()
with open("Mail Merge Project Start\\Input\\Names\\invited_names.txt", "r") as file:
    names = file.readlines()
    
for invitee in names:
    invitee = invitee.strip()
    with open (f"Mail Merge Project Start\\Output\\{invitee}_invited.txt", "w") as file:
        for _ in letter:
            _ = _.replace("[name]", invitee)
            # _ = _.strip()
            file.write(_)
            print ("done")