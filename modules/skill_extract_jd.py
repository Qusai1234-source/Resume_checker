import os 
from rapidfuzz import fuzz
import re

def extract_skill_jd(job_description):
    known_skills = {
    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "ruby", 
    "php", "swift", "go", "rust", "r", "matlab", "kotlin", "scala", 
    "perl", "visual basic", "sql", "bash", "shell scripting", "powershell",

    # Data Science & AI
    "machine learning", "deep learning", "data analysis", "data visualization", 
    "statistical modeling", "nlp", "computer vision", "tensorflow", "keras", 
    "pytorch", "scikit-learn", "pandas", "numpy", "matplotlib", "seaborn", 
    "opencv", "huggingface", "transformers", "xgboost", "lightgbm", 

    # Web Development
    "html", "css", "javascript", "react", "angular", "vue.js", "next.js", 
    "node.js", "express.js", "flask", "django", "php", "asp.net", "spring", 
    "graphql", "web3", "tailwind css", "bootstrap", "rest api", "graphql api", "node.js",
    "ppc campaigns",

    # Cloud Computing
    "aws", "azure", "google cloud", "gcp", "heroku", "cloudformation", 
    "terraform", "kubernetes", "docker", "jenkins", "ci/cd", "openstack", 
    "ansible", "cloudwatch", "datadog",

    # DevOps
    "devops", "git", "github actions", "bitbucket", "version control", 
    "jenkins", "circleci", "kubernetes", "docker-compose", "ansible", 
    "terraform", "cloudformation", "helm", "grafana", "prometheus", 
    "elk stack", "splunk", "monitoring tools",

    # Databases
    "mysql", "postgresql", "sqlite", "mongodb", "redis", "elasticsearch", 
    "dynamodb", "cassandra", "neo4j", "oracle db", "sql server", 
    "data warehouse", "etl", "hive", "snowflake", "bigquery",

    # Marketing & SEO
    "seo", "sem", "google analytics", "ppc", "content marketing", 
    "email marketing", "social media marketing", "crm", "hubspot", 
    "salesforce", "lead generation", "brand strategy", "market research",

    # Business & Management
    "project management", "agile", "scrum", "kanban", "jira", "trello", 
    "microsoft project", "business analysis", "risk management", 
    "stakeholder management", "cost estimation", "six sigma",

    # Cybersecurity
    "penetration testing", "vulnerability assessment", "firewalls", 
    "network security", "ethical hacking", "kali linux", "wireshark", 
    "cryptography", "endpoint security", "incident response", 
    "iso 27001", "nist", "compliance",

    "excel", "tableau", "power bi", "qlikview", "autocad", "sap", 
    "sap hana", "sas", "stata", "rpa", "uipath", "blue prism", 
    "jira", "trello", "slack", "microsoft teams", "figma", 
    "adobe photoshop", "adobe illustrator", "canva", "unity", 
    "unreal engine", "solidworks",

    "communication", "teamwork", "problem solving", "critical thinking", 
    "time management", "leadership", "adaptability", "creativity", 
    "negotiation", "conflict resolution"}
    job_description = job_description.lower()
    skill_delimiters = r"[,:;\.\-\n]"  
    potential_skills = re.split(skill_delimiters, job_description)
    extracted_skills = set()

    for skill in potential_skills:
        skill = skill.strip()
        for known_skill in known_skills:
            if fuzz.partial_ratio(skill, known_skill) > 80: 
                extracted_skills.add(known_skill)
                break
    return extracted_skills
