import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )


load_dotenv()
app = Flask(__name__)
mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

about_info = {
    "name": "Joshua Dierickse",
    "bio": "I'm a software engineer passionate about full-stack development, DevOps, and Linux.",
    "location": "Waterloo, Ontario, Canada",
    "title": ["Software Engineer"],
    "interests": ["AI", "Web Dev", "Linux", "Startups"],
    "photo_url": "https://media.licdn.com/dms/image/v2/D4E03AQGFONK6GQyKTw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1709684324180?e=2147483647&v=beta&t=xRyIB-jwikbRnIAw1czP_LCluHiQ41rYPt5qJr8FWL0",
}

experiences_data = [
    {
        "job_title": "Software Engineer",
        "date": "Incoming",
        "location": "Toronto, Ontario, Canada",
        "company_name": "Shopify",
        "company_logo": "https://media.licdn.com/dms/image/v2/D560BAQG_KjTcNcrLVw/company-logo_100_100/B56ZZolTV.HUAc-/0/1745511331439/shopify_logo?e=1756339200&v=beta&t=C4hlhNIEk4Mi5gQfR_RPDDRbU8EJ4MsrJ7qQ1Ka0His",
        "tech_stack": ["Internship"],
        "description": "",
    },
    {
        "job_title": "Product Engineering Fellow",
        "date": "Jun 2025 - Present",
        "location": "Remote",
        "company_name": "Meta & Major League Hacking",
        "company_logo": "https://media.licdn.com/dms/image/v2/D4D0BAQFSdPeChs7mKw/company-logo_100_100/company-logo_100_100/0/1683764485826?e=1756339200&v=beta&t=wxFFwJDW27buk2VecU6MN5bYDKDlMajd6drBSrPuJB0",
        "tech_stack": ["Production Engineering", "Linux", "Python", "Flask"],
        "description": "",
    },
    {
        "job_title": "Software Engineer",
        "date": "Jan 2025 - Apr 2025",
        "location": "Toronto, Ontario, Canada",
        "company_name": "theScore",
        "company_logo": "https://raw.githubusercontent.com/iWolf22/home-server/refs/heads/main/Web-Server/public/work/theScore.png",
        "tech_stack": [
            "PostgreSQL",
            "Kafka",
            "Datadog",
            "ArgoCD",
            "CircleCI",
        ],
        "description": "",
    },
    {
        "job_title": "Software Developer",
        "date": "05/2024 - 08/2024",
        "location": "Kitchener, ON",
        "company_name": "SigmaXL Inc.",
        "company_logo": "https://raw.githubusercontent.com/iWolf22/home-server/refs/heads/main/Web-Server/public/work/sigmaxl.png",
        "tech_stack": [
            "TypeScript",
            "NextJS",
            "PostgreSQL",
            "GPT-4o",
            "Flask",
        ],
        "description": "",
    },
    {
        "job_title": "Backend Developer",
        "date": "04/2024 - 06/2024",
        "location": "Remote",
        "company_name": "Art Vault",
        "company_logo": "https://raw.githubusercontent.com/iWolf22/home-server/refs/heads/main/Web-Server/public/work/art-vault.jpg",
        "tech_stack": ["NextJS", "Vercel Blob", "PostgreSQL", "Prisma ORM"],
        "description": "",
    },
    {
        "job_title": "Software Intern",
        "date": "08/2023",
        "location": "Waterloo, ON",
        "company_name": "Venuiti Solutions Inc.",
        "company_logo": "https://raw.githubusercontent.com/iWolf22/home-server/refs/heads/main/Web-Server/public/work/venuiti.png",
        "tech_stack": ["Spring Boot", "Gradle", "Maven", "Computer Networking"],
        "description": "",
    },
]

education_data = [
    {
        "degree": "Computer Science",
        "date": "09/2023 - 04/2028",
        "location": "Waterloo, ON",
        "institution_name": "University of Waterloo",
        "institution_logo": "https://raw.githubusercontent.com/iWolf22/home-server/refs/heads/main/Web-Server/public/work/uwaterloo.svg",
        "description": "",
    },
    {
        "degree": "High School Diploma",
        "date": "09/2019 - 06/2023",
        "location": "Waterloo, ON",
        "institution_name": "Waterloo Collegiate Institute",
        "institution_logo": "https://raw.githubusercontent.com/iWolf22/home-server/refs/heads/main/Web-Server/public/work/wci.png",
        "description": "",
    },
]

hobbies = [
    {
        "name": "Hockey",
        "image": "https://cdn.shopify.com/s/files/1/0601/9317/7836/files/canada-bedard-1040x572.jpg?v=1714033202",
        "color": "#512DA8",
        "label": "Hockey",
    },
    {
        "name": "Mountain Biking",
        "image": "https://static.wixstatic.com/media/95db5a_7bf68f602a95440eb9a64ac91bc7a6ed~mv2.jpg/v1/fill/w_640,h_400,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/95db5a_7bf68f602a95440eb9a64ac91bc7a6ed~mv2.jpg",
        "color": "#512DA8",
        "label": "Mountain Biking",
    },
    {
        "name": "Running",
        "image": "https://www.news-medical.net/images/Article_Images/ImageForArticle_22980_16600577310868068.jpg",
        "color": "#512DA8",
        "label": "Running",
    },
    {
        "name": "Chess",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chess_pieces_close_up.jpg/960px-Chess_pieces_close_up.jpg",
        "color": "#512DA8",
        "label": "Chess",
    },
    {
        "name": "Traveling",
        "image": "https://a.storyblok.com/f/112937/568x464/884e373bca/travel_pic_unsplash1-568x464.jpg/m/620x0/filters:quality(70)/",
        "color": "#512DA8",
        "label": "Traveling",
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Joshua Dierickse",
        about_info=about_info,
        experiences=experiences_data,
        education=education_data,
        url=os.getenv("URL"),
    )


@app.route("/hobbies")
def hobbies_route():
    return render_template(
        "hobbies.html",
        title="Joshua Dierickse - Hobbies",
        hobby_data=hobbies,
        url=os.getenv("URL"),
    )


@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Joshua Dierickse - Timeline")


@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    return model_to_dict(
        TimelinePost.create(
            name=request.form["name"],
            email=request.form["email"],
            content=request.form["content"],
        )
    )


@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
