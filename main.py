import streamlit as st
from modules.score import compute_score
from modules.resume_parser import extract_text_pdf
from modules.generate_explanation import generate_explanation
import os
jd="""We are looking for a talented Machine Learning Engineer to join our dynamic team at [Company Name]. As a Machine Learning Engineer, you will be responsible for developing, implementing, and maintaining machine learning models that drive our products and services forward. You will work closely with cross-functional teams to understand their needs, translate them into technical requirements, and deliver scalable solutions.
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
                    We look forward to reviewing your application and the opportunity to discuss how you can contribute to our team at [Company Name]."""
data_path=r"C:\Projects\Resume_checker\data\data\INFORMATION-TECHNOLOGY"
def main():
    # st.title("AI-Powered Resume Matching")
    
    # jd = st.text_area("Enter the Job Description:")
    
    # if st.button("Analyze Resumes"):
    #     if not jd:
    #         st.error("Please enter a job description.")
    #         return
        
        final_scores = {}
        
        for file in os.listdir(data_path):
            if file.endswith(".pdf"):
                file_path = os.path.join(data_path,file)
                text = extract_text_pdf(file_path)
                scores = compute_score(text, jd)
                final_scores[file] = scores["Final Score"]
                
        ranked_scores = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        
        # st.subheader("Ranked Resumes")
        for i, (file, score) in enumerate(ranked_scores, 1):
            print(f"{i}. {file} - Score: {score}")
        
        if ranked_scores:
            top_resume = ranked_scores[0][0]
            explanation = generate_explanation(os.path.join(data_path,top_resume), jd)
            # st.subheader("Why was this resume recommended?")
            print(explanation)

if __name__ == "__main__":
    main()