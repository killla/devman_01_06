import file_operations, random
from letters_mapping import runic_letters
from faker import Faker

fake = Faker("ru_RU")
ability = {
    "min_lvl": 8,
    "max_lvl": 14
}
count_of_monstres = 10
count_of_skills = 3

skills = []
with open('skills.txt') as file:
  for skill in file:
    for letter in skill:
      if letter in runic_letters:
        skill = skill.replace(letter, runic_letters[letter])
    skills.append(skill)

for number in range(count_of_monstres):
  monstr_skills = random.sample(skills, count_of_skills)
  context = {
    "first_name": fake.first_name_male(),
    "last_name": fake.last_name_male(),
    "town": fake.city(),
    "job": fake.job(),
    "strength": random.randint(ability['min_lvl'], ability['max_lvl']),
    "agility": random.randint(ability['min_lvl'], ability['max_lvl']),
    "endurance": random.randint(ability['min_lvl'], ability['max_lvl']),
    "intelligence": random.randint(ability['min_lvl'], ability['max_lvl']),
    "luck": random.randint(ability['min_lvl'], ability['max_lvl']),
    "skill_1": monstr_skills[0],
    "skill_2": monstr_skills[1],
    "skill_3": monstr_skills[2]
    }
  file_operations.render_template("template/charsheet.svg", f'monstres/charsheet-{number}.svg', context)
