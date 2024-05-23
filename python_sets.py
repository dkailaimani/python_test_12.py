# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes 
# of your airline with a competitor. You have two sets of flight destinations, 
# one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
print()
print("{:>60}".format("**********FLIGHT ROUTE COMPARISON**********\n"))
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

duplicateRoutes = our_routes.intersection(competitor_routes)
print(f"SHARED ROUTES BETWEEN COMPETITORS: {duplicateRoutes}")
print()

allRoutes = our_routes | competitor_routes
print(f"UNIQUE ROUTES BETWEEN COMPETITORS: {allRoutes}")
print()

neitherRoutes = set({})
for route in our_routes:
    if not route in competitor_routes:
        neitherRoutes.add(route)
for route in competitor_routes:
    if not route in our_routes:
        neitherRoutes.add(route)
print(f"UNSHARED ROUTES BETWEEN COMPETITORS: {neitherRoutes}")
print()

# Task 1: Duplicate Entries Cleanup
# You are given a list of customer IDs, some of which are duplicated.
# Write a Python script to remove duplicates and display the unique customer IDs.
print()
print("{:>65}".format("**********DUPLICATE CUSTOMER ID CLEAN-UP**********\n"))

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
print(f"ORIGINAL LIST OF IDS: {customer_ids}")
print()
for i in customer_ids:
    countSameId = customer_ids.count(i)
    if countSameId > 1:
        customer_ids.remove(i)
    customer_ids.sort()
print(f"UPDATED LIST OF UNIQUE IDS: {customer_ids}")
print()

# Task 1: Artist Lineup Compilation
# You are provided with a list of artist names scheduled to perform at
# different stages of the music festival. Using a loop, compile these artist
# names into a set to create a unique lineup without duplicates.
print()
print("{:>60}".format("**********ARTIST LINEUP COMPILATION **********\n"))

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers",
 "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

duplicate = False
for artist in artist_names:
    numOfAppearances = artist_names.count(artist)
    if numOfAppearances > 1:
        duplicate = True
        artist_names.remove(artist)
        unique_artists = artist_names
if duplicate:
            print("Duplicates Found in Playlist!")
artist_names.sort()
print()
print(f"OFFICIAL FESTIVAL PLAYLIST: {unique_artists}")
print()







