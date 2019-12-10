import file_operations, random
from letters_mapping import runic_letters
from faker import Faker

fake = Faker("ru_RU")

skills = []
with open('skills.txt') as file:
  for skill in file:
    for letter in skill:
      if letter in runic_letters:
        skill = skill.replace(letter, runic_letters[letter])
    skills.append(skill)

for number in range(10): 
  monstr_skills = random.sample(skills, 3)
  context = {
    "first_name": fake.first_name_male(),
    "last_name": fake.last_name_male(),
    "town": fake.city(),
    "job": fake.job(),
    "strength": random.randint(8, 14),
    "agility": random.randint(8, 14),
    "endurance": random.randint(8, 14),
    "intelligence": random.randint(8, 14),
    "luck": random.randint(8, 14),
    "skill_1": monstr_skills[0],
    "skill_2": monstr_skills[1],
    "skill_3": monstr_skills[2]
    }
  file_operations.render_template("template/charsheet.svg", f'monstres/charsheet-{number}.svg', context)
