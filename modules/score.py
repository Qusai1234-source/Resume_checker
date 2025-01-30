import os
import re
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util
import numpy as np
import spacy
from rapidfuzz import fuzz
from modules.skill_extract_res import extract_skill_res
from modules.skill_extract_jd import extract_skill_jd
from modules.resume_parser import extract_text_pdf

# Load models
model = SentenceTransformer("all-MiniLM-L6-v2")
nlp = spacy.load("en_core_web_sm")



# Patterns
exp_pattern = r"(\d+)\s*(?:year[s]?|yr[s]?)?\s*(?:and\s*(\d+)\s*month[s]?)?"
edu_pattern = re.compile(r"\b(?:Bachelor|Master|PhD|MBA|B\.Tech|M\.Tech|B\.Sc|M\.Sc|M\.Eng|B\.Eng|M\.Ed|B\.Ed)\b", re.IGNORECASE)

# Weights
weights = {
    "semantic": 30,
    "skills": 45,
    "experience": 20,
    "education": 5
}

def semantic_scoring(text, jd):
    res_embeddings = model.encode(text, convert_to_tensor=True)
    jd_embeddings = model.encode(jd, convert_to_tensor=True)
    semantic_score = util.pytorch_cos_sim(res_embeddings, jd_embeddings).item()
    return round(semantic_score * 100, 2)

def extract_experience(text):
    exp_match = re.search(exp_pattern, text, re.IGNORECASE)
    if exp_match:
        years = int(exp_match.group(1)) if exp_match.group(1) else 0
        months = int(exp_match.group(2)) if exp_match.group(2) else 0
        if years >= 2000:
            years -= 2025
        exp = years + (months / 12)
    else:
        exp = 0
    if exp>20:
        return 0
    return exp

def compute_exp_score(text, jd):
    jd_exp = extract_experience(jd)
    res_exp = extract_experience(text)

    if jd_exp == 0:
        return 100
    exp_diff = abs(jd_exp - res_exp)
    exp_score = max(100 - (exp_diff / jd_exp) * 100, 0)

    return round(exp_score, 2)

# def extract_skills(text):
#     doc = nlp(text)
#     extracted_skills = set()
#     for ent in doc.ents:
#         if ent.label_ in ["ORG", "PRODUCT", "TECHNOLOGY"]:
#             extracted_skills.add(ent.text.lower())
#     for skill in predefined_skills:
#         if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
#             extracted_skills.add(skill.lower())
#     return extracted_skills

def compute_skill_score(jd, text):
    jd_skill = extract_skill_jd(jd)
    res_skill = extract_skill_res(text,jd_skill)

    similar_skills = jd_skill.intersection(res_skill)
    if len(jd_skill) == 0:
        return 0
    skill_score = (len(similar_skills) / len(jd_skill)) * 100
    print(skill_score)
    return round(skill_score, 2)

def extract_education(text):
    doc = nlp(text)
    extracted_degree = set()
    regex_match = edu_pattern.findall(text)
    extracted_degree.update(regex_match)

    # for ent in doc.ents:
    #     if ent.label_ == "ORG":
    #         extracted_degree.add(ent.text)
    return extracted_degree

def compute_edu_score(jd, text):
    jd_edu = extract_education(jd)
    res_edu = extract_education(text)

    if not jd_edu:
        return 100
    best_match = 0
    for jd_degree in jd_edu:
        for res_degree in res_edu:
            similarity = fuzz.partial_ratio(jd_degree.lower(), res_degree.lower())
            best_match = max(best_match, similarity)
    if best_match >= 90:
        education_score = 100  # Exact match
    elif best_match >= 75:
        education_score = 75  # Closely related field
    elif best_match >= 50:
        education_score = 50  # Somewhat relevant field
    else:
        education_score = 0  # No match

    return education_score

def compute_score(text, jd):
    semantic_score = semantic_scoring(text, jd)
    skill_score = compute_skill_score(jd, text)
    edu_score = compute_edu_score(jd, text)
    exp_score = compute_exp_score(text, jd)

    final_score = (
        weights["semantic"] * semantic_score +
        weights["skills"] * skill_score +
        weights["education"] * edu_score +
        weights["experience"] * exp_score
    ) / 100
    return {
        "Final Score": round(final_score, 2),
        "Semantic Score": semantic_score,
        "Skills Score": skill_score,
        "Experience Score": exp_score,
        "Education Score": edu_score,
    }

if __name__ == "__main__":
    data_folder = r"C:\Projects\Resume_checker\data\data"
    final_scores = {}
    for label_folder in os.listdir(data_folder):
        label_path = os.path.join(data_folder, label_folder)
        if not os.path.isdir(label_path):
            continue
        for file in os.listdir(label_path):
            if file.endswith(".pdf"):
                file_path = os.path.join(label_path, file)
                text = extract_text_pdf(file_path)
                jd = """We are looking for a talented Machine Learning Engineer to join our dynamic team at [Company Name]. As a Machine Learning Engineer, you will be responsible for developing, implementing, and maintaining machine learning models that drive our products and services forward. You will work closely with cross-functional teams to understand their needs, translate them into technical requirements, and deliver scalable solutions.
                      Key Responsibilities:
                    Design, build, and maintain machine learning models for various applications.
                    Perform data analysis and feature extraction to improve model performance.
                    Collaborate with data engineers to ensure data quality and availability.
                    Research and implement new machine learning algorithms and techniques.
                    Optimize models for performance and scalability.
                    Document models and collaborate with other team members.
                    Stay up-to-date with the latest research and trends in machine learning.
                    Qualifications:
                    Bachelor's degree in Computer Science, Mathematics, Statistics, or a related field.
                    3-5 years of experience in machine learning and data analysis.
                    Proficiency in Python or another programming language.  
                    Experience with machine learning libraries (e.g., TensorFlow, PyTorch, scikit-learn).
                    Knowledge of SQL and NoSQL databases.
                    Familiarity with cloud platforms (e.g., AWS, Google Cloud).
                    Strong problem-solving and analytical skills.
                    Ability to work independently and as part of a team.
                    Excellent communication skills.
                    Preferred Qualifications:
                    Master's degree in a related field.
                        Experience with big data technologies.
                    Publication in machine learning conferences or journals.
                        Proficiency in multiple programming languages.
                    Experience with deep learning frameworks.
                    We Offer:
                    Competitive salary and benefits package.
                    Opportunities for growth and advancement.
                    Collaborative and inclusive work environment.
                    Flexible work hours and remote work options.
                    Access to the latest tools and technologies.
                    How to Apply:
                    Please send your resume and cover letter to [email address] with "Machine Learning Engineer" in the subject line.
                    We look forward to reviewing your application and the opportunity to discuss how you can contribute to our team at [Company Name].
                    """
                scores = compute_score(text, jd)
                final_scores[file] = scores["Final Score"]

    ranked_score = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
    print(ranked_score)