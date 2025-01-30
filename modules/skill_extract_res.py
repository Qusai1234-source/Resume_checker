import rapidfuzz as fuzz
import os 
import re
def extract_skill_res(text,jd_skills):
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
    extracted_skills={skill for skill in known_skills if re.search(rf"\b{re.escape(skill)}\b",text,re.IGNORECASE)}

    skills_pattern = r"(?:skills|technologies|expertise|proficient in|Computer Skills)[:\s]+([\w\s,]+)"
    skills_match = re.search(skills_pattern, text, re.IGNORECASE)
    if skills_match:
        matched_skills=[skill.strip().lower() for skill in re.split(r"[,\s]+", skills_match.group(1))]
        extracted_skills.update(matched_skills)
    skills = {skill for skill in extracted_skills if skill.strip()}
    return skills