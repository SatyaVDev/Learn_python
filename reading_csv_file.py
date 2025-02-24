import pandas as pd
from faker import Faker

# Initialize Faker instance
fake = Faker()
profiles = []


for i in range(10):
    profile = fake.profile()

    profiles.append(profile)


df = pd.DataFrame(profiles)

print(df.head(2))
