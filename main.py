from ctypes.wintypes import WORD
from tkinter import W
import yaml
from yaml import SafeLoader
from jinja2 import Template

first_name = 0
last_name = 0
occupation = 0
contact_email = 0
education = 0
education_beginning = 0
education_end = 0
skills = []
work_experience = []

file = open("index.html", "r").read()

with open('resume.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    try:
        for elem in data:
            if elem == "basic_info": 
                for item in data[elem]:
                    print(item)
                    if item == "first_name":
                        first_name = data[elem][item]
                    elif item == "last_name":
                        last_name = data[elem][item]
                    elif item == "occupation":
                        occupation = data[elem][item]
                    elif item == "contact_email":
                        contact_email = data[elem][item]
                    elif item == "education":
                        education = data[elem][item]
                    elif item == "education_beginning":
                        education_beginning = data[elem][item]
                    elif item == "education_end":
                        education_end = data[elem][item]
            elif elem == "skills": 
                for item in data[elem]:
                    skills.append(item)
            else:
                for item in data[elem]:
                    work_experience.append(item)
    except:
        pass
    finally:
        template = Template(file)
        html_copy = template.render(first_name=first_name, last_name=last_name, occupation=occupation, contact_email=contact_email, education=education, education_beginning=education_beginning, education_end=education_end, skills=skills, work_experience=work_experience)
        with open("result.html", "w") as f:
            f.write(html_copy)
            f.close()