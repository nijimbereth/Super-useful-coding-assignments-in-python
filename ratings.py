#creating function that helps counts the ratings a service or products has recieved

ratings = ["5_star","1_star", "2_star", "3_star", "4_star", "3_star", "4_star", "5_star", "5_star"]

total_ratings = {}

for rating in ratings:
    if rating in total_ratings:
        total_ratings[rating] += 1
    else:
        total_ratings[rating] = 1

print("Our rating is:")
print(total_ratings)