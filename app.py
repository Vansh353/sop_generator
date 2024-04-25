import time
import streamlit as st
import openai
from openai import OpenAI




# Set your OpenAI API key
openai.api_key = "sk-proj-8RORbiF7yWVwoLopwBnwT3BlbkFJAsL7tb3ph1XRFn15ea9j"
client = OpenAI(api_key=openai.api_key)
def generate_sop(inputs):

    # Construct the messages for the Chat API
    messages = [
            {"role": "system", "content": "You are a helpful assistant tasked with creating a Statement of Purpose (SOP) for a graduate program application. The applicant has provided the following information:\n\n- Full Name: [Full Name]\n- Current University: [Current University]\n- University Applying To: [University Applying To]\n- Program: [Program]\n- Long-term Goal: [Long-term Goal]\n\n1. Begin by introducing the applicant, mentioning their name, current university, the university they are applying to, the program they are interested in, and their long-term goal.\n\n2. Ask the applicant why they chose the university they are applying to and incorporate their response into the SOP.\n\n3. Include details about the applicant's work experience, projects, extra-curricular activities, and academic achievements as provided.\n\n4. Ensure that the SOP maintains a professional tone and effectively conveys the applicant's qualifications, motivations, and aspirations.\n\n5. Conclude the SOP with a summary of the applicant's strengths and a statement expressing their readiness and enthusiasm for the program.\n\nBased on this prompt, craft a compelling and cohesive SOP that showcases the applicant's potential and suitability for the graduate program. The response should be in the first person."},
            {"role": "user", "content": f"My name is {inputs['full_name']}. I am currently studying at {inputs['current_uni']}. I am applying to {inputs['apply_uni']} for the {inputs['program']} program. My long-term goal is {inputs['long_term_goal']}."},
            {"role": "assistant", "content": f"Why did I choose {inputs['apply_uni']}? {inputs['apply_uni_reason']}"},
            {"role": "user", "content": f"Work Experience: {inputs['work_experience']}"},
            {"role": "user", "content": f"Projects: {inputs['projects']}"},
            {"role": "user", "content": f"Extra-curricular: {inputs['extra_curricular']}"},
            {"role": "user", "content": f"Academic Achievements: {inputs['academic_achievements']}"},
        ]

    # Use Chat API to generate the SoP
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=600
    )

    return response.choices[0].message.content.strip()

def main():
    st.title("Statement of Purpose Generator")
    st.image("maxresdefault.jpg")
    
    st.markdown("""
    Welcome to the SOP Generator! This application uses AI to generate a Statement of Purpose (SOP) based on your inputs.

    ---
    """)

    
    st.sidebar.info("""
    This tool generates a Statement of Purpose (SOP) for a graduate program application. 
    Fill in the required fields marked with * and click 'Generate SOP' to create your SOP. 
    The generated SOP will be displayed on the right.
    """)
    
    with st.sidebar.expander("Help"):
        st.write("""
        - Full Name*: Enter your full name as it appears on your official documents.
        - Current University*: Enter the name of the university you are currently attending.
        - University Applying To*: Enter the name of the university you are applying to.
        - Program*: Enter the name of the program you are applying for.
        - Long-term Goal*: Describe your long-term career or academic goal.
        - Why did you choose this university?: Explain why you chose this university for your graduate studies.
        - Work Experience: Describe your work experience relevant to the program you are applying for.
        - Projects: Describe any projects you have completed that are relevant to the program.
        - Extra-curricular Activities: Describe any extra-curricular activities you have participated in.
        - Academic Achievements: List any academic achievements or awards you have received.
        """)

    with st.sidebar:
        st.header("Input Information")
        full_name = st.text_input("Full Name*")
        current_uni = st.text_input("Current University*")
        apply_uni = st.text_input("University Applying To*")
        program = st.text_input("Program*")
        long_term_goal = st.text_input("Long-term Goal*")
        apply_uni_reason = st.text_input("Why did you choose this university?")
        work_experience = st.text_input("Work Experience")
        projects = st.text_input("Projects")
        extra_curricular = st.text_input("Extra-curricular Activities")
        academic_achievements = st.text_input("Academic Achievements")
        
        st.markdown("---")


    if st.sidebar.button("Generate SOP"):
        required_fields = [full_name, current_uni, apply_uni, program, long_term_goal]
        if any(not field for field in required_fields):
            st.error("Please fill in all required fields marked with *.")
        else:
            inputs = {
                "full_name": full_name,
                "current_uni": current_uni,
                "apply_uni": apply_uni,
                "program": program,
                "long_term_goal": long_term_goal,
                "apply_uni_reason": apply_uni_reason,
                "work_experience": work_experience,
                "projects": projects,
                "extra_curricular": extra_curricular,
                "academic_achievements": academic_achievements
            }
            progress = st.progress(0)
            for i in range(100):
                # Update the progress bar with each iteration.
                progress.progress(i + 1)
                time.sleep(0.01)
            sop = generate_sop(inputs)
            st.subheader("Generated Statement of Purpose")
            st.write(sop)
            st.download_button("Download SOP", data=sop, file_name='sop.txt', mime='text/plain')
    
    st.markdown("---")  # Add a horizontal line

    st.header("Instructions")
    st.write("""
    Fill out the input fields in the sidebar and then click the "Generate SOP" button. A preview of the SOP will be generated for you to review. If you're happy with the preview, you can generate the full SOP.
    """)

    st.markdown("---")  # Add a horizontal line

    st.header("About")
    st.write("""
    This application was developed by Zeel Thakkar. It uses the OpenAI API to generate the SOP.
    """)

    st.markdown("---")  # Add a horizontal line

    st.header("Contact")
    st.write("""
    If you have any questions or feedback, please contact me at Zeel123@gmail.com.
    """)

if __name__ == "__main__":
    main()  
