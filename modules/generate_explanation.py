from modules.score import extract_experience,extract_education
from modules.skill_extract_res import extract_skill_res
from modules.skill_extract_jd import extract_skill_jd
from modules.resume_parser import extract_text_pdf
def generate_explanation(resume, jd):
    resume_text = extract_text_pdf(resume)
    jd_skill=extract_skill_jd(jd)
    res_skill=extract_skill_res(resume,jd_skill)
    matched_skills = jd_skill.intersection(res_skill)
    experience = extract_experience(resume_text)
    education = extract_education(resume_text)
    
    explanation = f"The resume '{resume}' was recommended because it best matches the job description based on the following criteria:\n\n"
    explanation += f"- High semantic similarity to the job description.\n"
    explanation += f"- Matched Skills: {', '.join(matched_skills) if matched_skills else 'None'}\n"
    explanation += f"- Experience: {experience} years\n"
    explanation += f"- Education: {', '.join(education) if education else 'Not specified'}\n"
    return explanation
