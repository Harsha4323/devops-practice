import re
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MicroDegree | Registration",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Demo app: registration data is kept only in Streamlit session state.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: linear-gradient(135deg, #f7f7ff 0%, #f4f8ff 55%, #f9f7ff 100%); }
.block-container { max-width: 1180px; padding-top: 1.5rem; padding-bottom: 3rem; }
.brandbar {
  background: linear-gradient(100deg,#5d43d6,#24166b);
  color: white; padding: 1rem 1.25rem; border-radius: 16px;
  display:flex; justify-content:space-between; align-items:center; gap:1rem;
  box-shadow: 0 12px 30px rgba(37,22,107,.16); margin-bottom: 1.4rem;
}
.brand { font-weight:800; font-size:1.15rem; letter-spacing:.2px; }
.nav { opacity:.9; font-size:.86rem; }
.hero {
  background: white; border: 1px solid #ebe8ff; border-radius: 22px;
  padding: 1.7rem; box-shadow: 0 14px 35px rgba(31,25,84,.07);
}
.eyebrow { display:inline-block; padding:.35rem .7rem; border-radius:999px;
  background:#f0edff; color:#5b43d5; font-size:.8rem; font-weight:700; }
h1 { color:#17172c; letter-spacing:-1.1px; }
.sub { color:#62657a; line-height:1.65; }
.feature { background:#f8f7ff; border:1px solid #eeebff; padding:1rem;
  border-radius:14px; margin-bottom:.75rem; }
.feature strong { color:#28205f; }
.small { color:#72748a; font-size:.86rem; line-height:1.5; }
div.stButton > button, div[data-testid="stFormSubmitButton"] button {
  background:linear-gradient(100deg,#7052ef,#5940d4); color:white;
  border:0; border-radius:10px; min-height:2.8rem; font-weight:700;
}
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover {
  color:white; border:0; filter:brightness(1.05);
}
.video-card { background:white; border:1px solid #e9e7f5; padding:1rem;
  border-radius:14px; margin:.55rem 0; box-shadow:0 4px 14px rgba(30,25,70,.04); }
.success-box { text-align:center; background:white; border:1px solid #e7f5eb;
  border-radius:22px; padding:2.2rem 1.4rem; box-shadow:0 14px 35px rgba(31,25,84,.07); }
.success-icon { margin:auto; width:82px; height:82px; display:grid; place-items:center;
  border-radius:50%; background:#dff8e9; color:#18a957; font-size:3rem; }
a { color:#6547e8 !important; }
footer { visibility:hidden; }
@media (max-width: 700px) {
  .brandbar { flex-direction:column; align-items:flex-start; }
  .hero { padding:1.15rem; }
}
</style>
""", unsafe_allow_html=True)

VIDEOS = [
    ("Getting Started with Python – Full Course for Beginners", "https://youtu.be/epRCCsUvJN8"),
    ("Python Full Course for free 🐍", "https://youtu.be/m3YFGPoefeM"),
    ("MicroDegree – Official Channel", "https://www.youtube.com/@MicroDegree/videos"),
]

if "registered" not in st.session_state:
    st.session_state.registered = False
if "registration" not in st.session_state:
    st.session_state.registration = {}

st.markdown("""
<div class="brandbar">
  <div class="brand">🎓 MicroDegree</div>
  <div class="nav">Home&nbsp;&nbsp;&nbsp; Courses&nbsp;&nbsp;&nbsp; Projects&nbsp;&nbsp;&nbsp; Login</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.registered:
    left, right = st.columns([1.15, .85], gap="large")
    with left:
        st.markdown("""
        <div class="hero">
          <span class="eyebrow">Join the MicroDegree Community 💜</span>
          <h1 style="margin-bottom:.35rem;">Create Your Account</h1>
          <p class="sub">Register now and unlock exclusive projects, learning resources, and a world of learning.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("registration_form", clear_on_submit=False):
            full_name = st.text_input("Full Name", placeholder="Enter your full name")
            email = st.text_input("Email Address", placeholder="you@example.com")
            phone = st.text_input("Phone Number", placeholder="Enter your phone number")
            program = st.selectbox(
                "Choose Program",
                ["Select a program", "Python Development", "Web Development",
                 "Data Science", "Full Stack Development", "Digital Marketing"],
            )
            password = st.text_input("Password", type="password", placeholder="At least 8 characters")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")
            agreed = st.checkbox("I agree to the Terms of Service and Privacy Policy")
            submitted = st.form_submit_button("🎓  Register Now", use_container_width=True)

        if submitted:
            errors = []
            if len(full_name.strip()) < 2:
                errors.append("Please enter your full name.")
            if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
                errors.append("Enter a valid email address.")
            if not re.fullmatch(r"[0-9+\-\s()]{7,20}", phone.strip()):
                errors.append("Enter a valid phone number.")
            if program == "Select a program":
                errors.append("Please choose a program.")
            if len(password) < 8:
                errors.append("Password must contain at least 8 characters.")
            if password != confirm_password:
                errors.append("Passwords do not match.")
            if not agreed:
                errors.append("Please accept the Terms of Service and Privacy Policy.")
            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Intentionally do not store the password.
                st.session_state.registration = {
                    "name": full_name.strip(),
                    "email": email.strip(),
                    "phone": phone.strip(),
                    "program": program,
                }
                st.session_state.registered = True
                st.rerun()

        st.markdown('<p class="small">Already have an account? <a href="#registration_form">Login</a></p>', unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="hero">
          <div style="font-size:4rem;text-align:center;">🚀</div>
          <h2 style="color:#21185c;text-align:center;">Learn. Build. Launch.</h2>
          <p class="sub" style="text-align:center;">Build real skills with practical, industry-relevant learning.</p>
          <div class="feature">🧭 <strong>Industry Relevant Curriculum</strong><br><span class="small">Learn skills that are in demand and build your future.</span></div>
          <div class="feature">🛠️ <strong>Hands-on Projects</strong><br><span class="small">Work on real-world projects and build your portfolio.</span></div>
          <div class="feature">🏆 <strong>Certificate of Completion</strong><br><span class="small">Showcase your learning achievements.</span></div>
          <div style="padding:.8rem;color:#5c5875;font-style:italic;">“Small steps today. Big projects tomorrow.”</div>
        </div>
        """, unsafe_allow_html=True)
else:
    data = st.session_state.registration
    st.markdown("""
    <div class="success-box">
      <div class="success-icon">✓</div>
      <h1 style="color:#176b39;margin-top:1rem;">You've unlocked exclusive projects!</h1>
      <p class="sub">Thanks for registering with MicroDegree. Get started by exploring these recommended resources.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    a, b = st.columns([1, 1])
    with a:
        st.markdown("### Welcome, " + data.get("name", "Learner") + " 👋")
        st.markdown(f"**Selected program:** {data.get('program', '')}")
        st.caption("Demo registration complete. Your details are held only in this session.")
        if st.button("← Back to registration", use_container_width=True):
            st.session_state.registered = False
            st.session_state.registration = {}
            st.rerun()
    with b:
        st.markdown("### Recommended Videos for You")
        for title, url in VIDEOS:
            st.markdown(
                f'<div class="video-card"><strong>▶ {title}</strong><br><a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a></div>',
                unsafe_allow_html=True,
            )
    st.info("This is a demo front end, not a production account system. For real users, connect a database and implement secure password hashing, email verification, and privacy/terms pages.")
