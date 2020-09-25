songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])
print(songs[1:2])

songs[2] = "I've Been Flushed From the Bathroom of Your Heart"

songs.append("Satan Gave Me a Taco")
songs.extend(["You're the Reason Our Kids Are So Ugly",
              "If You Don't Believe I Love You, Just Ask My Wife", "She Never Told Me She Was a Mime"])
songs.insert(2, "If the Phone Doesn't Ring, It's Me")

songs.remove("Do It")