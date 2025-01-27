import re
from rapidfuzz import fuzz
def extract_skills_from_jd(jd):
    pre_defined_skills={
        # Technical and IT Roles
    "Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "SQL", "R",
    "React", "Angular", "Node.js", "Django", "Flask", "Spring",
    "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy", "Matplotlib",
    "AWS", "Azure", "Google Cloud Platform", "Kubernetes", "Docker",
    "Jenkins", "Terraform", "Ansible", "CI/CD", "Git", "Agile",
    "LAN/WAN management", "Cisco routers", "Firewalls", "VPN",
    "Penetration Testing", "Vulnerability Assessment", "SIEM tools", "SOC operations",
    
    # Finance and Accounting
    "Financial Analysis", "Budgeting", "Forecasting", "Taxation", "Auditing",
    "SAP", "QuickBooks", "Excel", "Tally", "Risk Management",
    "Accounts Payable", "Accounts Receivable", "Payroll Management", "Cost Accounting",

    # Marketing and Sales
    "SEO", "SEM", "Content Marketing", "Social Media Marketing",
    "Google Analytics", "CRM", "Email Marketing", "Market Research",
    "Sales Strategy", "Lead Generation", "Customer Relationship Management",
    "Negotiation", "Brand Management", "Event Planning",

    # Healthcare
    "Patient Care", "Medical Billing", "Electronic Health Records (EHR)",
    "ICD-10 Coding", "Phlebotomy", "Clinical Research",
    "HIPAA Compliance", "Diagnosis", "Prescription Writing",
    "Healthcare Analytics", "Telemedicine",

    # Human Resources
    "Recruitment", "Employee Engagement", "Performance Management",
    "Compensation and Benefits", "HR Policies", "Payroll Processing",
    "Conflict Resolution", "Training and Development",
    "HRIS (Human Resources Information System)",

    # Design and Creative
    "Graphic Design", "UI/UX Design", "Adobe Photoshop", "Illustrator",
    "Figma", "Sketch", "Video Editing", "Animation",
    "Typography", "Wireframing", "Prototyping",

    # Operations and Logistics
    "Supply Chain Management", "Inventory Management", "Logistics Planning",
    "Procurement", "Warehouse Management", "Lean Manufacturing",
    "Six Sigma", "Fleet Management", "Process Optimization",

    # Education and Training
    "Curriculum Design", "Teaching", "Public Speaking",
    "Classroom Management", "E-learning Platforms", "Assessment Tools",
    "Educational Technology", "Mentoring", "Instructional Design",

    # Customer Service
    "Customer Support", "Problem Resolution", "Call Center Operations",
    "Order Processing", "Customer Retention", "CRM Tools",
    "Upselling", "Multitasking", "Active Listening",
    }
    jd=jd.lower()
    skill_dellimeters=r"[,:;\.\-\n]"
    potential_skills=re.split(skill_dellimeters,jd)
    extracted_skills=set()

    for skill in potential_skills:
        skill=skill.strip()
        for known_skill in pre_defined_skills:
            if fuzz.partial_ratio(skill, known_skill) > 80: 
                extracted_skills.add(known_skill)
                break
    return extracted_skills

if __name__=="__main__":
    jd="""We are looking for a Python Developer to join our engineering team and help us develop and maintain various software products.

Python Developer responsibilities include writing and testing code, debugging programs and integrating applications with third-party web services. To be successful in this role, you should have experience using server-side logic and work well in a team.

Ultimately, you’ll build highly responsive web applications that align with our business needs.

Responsibilities
Write effective, scalable code
Develop back-end components to improve responsiveness and overall performance
Integrate user-facing elements into applications
Test and debug programs
Improve functionality of existing systems
Implement security and data protection solutions
Assess and prioritize feature requests
Coordinate with internal teams to understand user requirements and provide technical solutions
Requirements and skills
Work experience as a Python Developer
Expertise in at least one popular Python framework (like Django, Flask or Pyramid)
Knowledge of object-relational mapping (ORM)
Familiarity with front-end technologies (like JavaScript and HTML5)
Team spirit
Good problem-solving skills
BSc in Computer Science, Engineering or relevant field"""
    skills=extract_skills_from_jd(jd)
    print(skills)
    

 
