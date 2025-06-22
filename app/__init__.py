import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

about_info = {
    "name": "Jenny Cheng",
    "bio": "I'm a software engineer passionate about AI and full-stack development.",
    "location": "San Francisco, CA",
    "title": ["Software Engineer", "Software Developer"],
    "interests": ["AI", "Web Dev", "Hackathons", "Startups"],
    "photo_url": "/static/img/logo.jpg",
}

experiences_data = [
    {
        "job_title": "Senior Software Engineer",
        "date": "2022 - Present",
        "location": "San Francisco, CA",
        "company_name": "Google",
        "company_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_%22G%22_logo.svg/800px-Google_%22G%22_logo.svg.png",
        "tech_stack": ["Python", "Docker", "AWS", "Kubernetes", "React", "Node.js"],
        "description": "Led a team to build scalable cloud-native applications. Improved CI/CD pipelines, mentored junior developers, and collaborated with cross-functional teams to deliver high-impact products.",
    },
    {
        "job_title": "Quantitative Researcher",
        "date": "2020 - 2022",
        "location": "New York, NY",
        "company_name": "Jane Street",
        "company_logo": "https://ocaml.janestreet.com/ocaml-core/v0.12/doc/logo.png",
        "tech_stack": ["Python", "OCaml", "Pandas"],
        "description": "Developed and backtested trading strategies, analyzed large datasets, and collaborated with traders to optimize performance.",
    },
    {
        "job_title": "Backend Developer",
        "date": "2018 - 2020",
        "location": "Bozeman, MT",
        "company_name": "Snowflake",
        "company_logo": "https://logos-world.net/wp-content/uploads/2022/11/Snowflake-Symbol.png",
        "tech_stack": ["Go", "PostgreSQL", "Docker"],
        "description": "Designed and implemented RESTful APIs, optimized database queries, and maintained microservices infrastructure.",
    },
]

education_data = [
    {
        "degree": "M.Sc. Computer Science",
        "date": "2016 - 2018",
        "location": "Stanford, CA",
        "institution_name": "Stanford University",
        "institution_logo": "https://identity.stanford.edu/wp-content/uploads/sites/3/2020/07/block-s-right.png",
        "description": "Specialized in Artificial Intelligence and Machine Learning. Graduated with honors.",
    },
    {
        "degree": "B.Sc. Computer Science",
        "date": "2012 - 2016",
        "location": "Cambridge, MA",
        "institution_name": "MIT",
        "institution_logo": "https://download.logo.wine/logo/Massachusetts_Institute_of_Technology/Massachusetts_Institute_of_Technology-Logo.wine.png",
        "description": "Focused on software engineering principles and data structures. Active member of the coding club.",
    },
]

hobbies = [
    {
        "name": "Foodie",
        "image": "/static/img/food.jpg",
        "color": "#B39DDB",
        "label": "Foodie",
    },
    {
        "name": "Driving",
        "image": "/static/img/drive.jpg",
        "color": "#9575CD",
        "label": "Driving",
    },
    {"name": "Tech", "image": "wifi.png", "color": "#7E57C2", "label": "Tech"},
    {"name": "Design", "color": "#673AB7", "label": "Design"},
    {
        "name": "Fitness",
        "image": "/static/img/gym.jpg",
        "color": "#5E35B1",
        "label": "Fitness",
    },
    {"name": "Cafe", "color": "#512DA8", "label": "Coffee Time"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="MLH Fellow",
        about_info=about_info,
        experiences=experiences_data,
        education=education_data,
        url=os.getenv("URL"),
    )


@app.route("/hobbies")
def hobbies_route():
    return render_template(
        "hobbies.html",
        title="MLH Fellow",
        hobby_data=hobbies,
        url=os.getenv("URL"),
    )
