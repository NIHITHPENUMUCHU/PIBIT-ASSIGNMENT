import json

resume_content = """
Penumuchu Nihith
Email: ns2995@srmist.edu.in
Phone: ##### 77530
LinkedIn: https://www.linkedin.com/in/nihith-penumuchu-132219253/

Education:
B.Tech in Computer Science With Specialization in AIML, SRM University KTR Campus, 2025

Skills:
- Python
- Machine Learning
- NLP
- HTML
- CSS
- JavaScript
- ReactJS
- C
- C++
"""

prompt = f"""
Given the following resume, parse the content and return it in JSON format:

{resume_content}

Expected JSON format:
{{
    "Name": "Full Name",
    "Contact Information": {{
        "Email": "email@example.com",
        "Phone": "123-456-7890",
        "LinkedIn": "https://www.linkedin.com/in/username/"
    }},
    "Education": [
        {{
            "Degree": "Degree Name",
            "University": "University Name",
            "Graduation Year": "Year"
        }}
    ],

    "Skills": ["Skill 1", "Skill 2", "Skill 3", "skill 4", "skill 5", "skill 6", "skill 7", "skill 8", "skill 9"]
}}
"""

parsed_resume = {
    "Name": "PENUMUCHU NIHITH",
    "Contact Information": {
        "Email": "ns2995@srmist.edu.in",
        "Phone": "##### 77530",
        "LinkedIn": "https://www.linkedin.com/in/nihith-penumuchu-132219253/"
    },
    "Education": [
        {
            "Degree": "B.Tech in Computer Science",
            "University": "SRM INSTITUTE OF SCIENCE AND TECHNOLOGY, KTR CAMPUS",
            "Graduation Year": "2025"
        }
    ],

    "Skills": ["Python", "Machine Learning", "NLP", "HTML", "CSS", "JavaScript", "ReactJS", "C", "C++"]
}

print(json.dumps(parsed_resume, indent=4))
