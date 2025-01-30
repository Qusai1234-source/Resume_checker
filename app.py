import streamlit as st
from modules.score import compute_score
from modules.resume_parser import extract_text_pdf
from modules.generate_explanation import generate_explanation
import os

data_path=r"C:\Projects\Resume_checker\data\data\INFORMATION-TECHNOLOGY"
def main():
    st.title("AI-Powered Resume Matching")
    
    jd = st.text_area("Enter the Job Description:")
    
    if st.button("Analyze Resumes"):
        if not jd:
            st.error("Please enter a job description.")
            return
        
        final_scores = {}
        
        for file in os.listdir(data_path):
            if file.endswith(".pdf"):
                file_path = os.path.join(data_path, file)
                text = extract_text_pdf(file_path)
                scores = compute_score(text, jd)
                final_scores[file] = scores["Final Score"]
                
        ranked_scores = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        
        st.subheader("Ranked Resumes")
        for i, (file, score) in enumerate(ranked_scores, 1):
            st.write(f"{i}. {file} - Score: {score}")
        
        if ranked_scores:
            top_resume = ranked_scores[0][0]
            explanation = generate_explanation(os.path.join(data_path,top_resume), jd)
            st.subheader("Why was this resume recommended?")
            st.write(explanation)

if __name__ == "__main__":
    main()