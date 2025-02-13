from faker import Faker
import pandas as pd

# Initialize Faker instance
fake = Faker()
profiles = []


for i in range(10):
    profile = fake.profile()
    profiles.append(profile)


df = pd.DataFrame(profiles)

print(df.head(2))
