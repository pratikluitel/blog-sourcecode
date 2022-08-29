"""
Generates a fake dataset of momo reviews by restaurant
and saves as csv
"""

import pandas as pd
import numpy as np

locations = ["Kathmandu", "Delhi", "Darjeeling"]

# represents only the restaurant location and the corresponding id
momo_data = {
    "restaurant_id": [i for i in range(15000)],
    "location": [locations[np.random.randint(0, 3)] for i in range(15000)],
}

momo_ratings = []

for location in momo_data["location"]:
    # generated as (variance * approx p value + mean)
    if location == "Kathmandu":
        rating = round(0.19 * np.random.randn() + 3.75, 2)
    elif location == "Delhi":
        rating = round(0.28 * np.random.randn() + 3.25, 2)
    elif location == "Darjeeling":
        rating = round(0.22 * np.random.randn() + 3.6, 2)
    momo_ratings.append(rating)

momo_data["momo_rating"] = momo_ratings

momo_ratings_df = pd.DataFrame(momo_data)

momo_ratings_df.to_csv("data/momo_ratings.csv", encoding="utf-8")
