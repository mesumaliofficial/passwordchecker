import streamlit as st
import re
import string
import random

def check_password_strength(password):
    strength = 0
    feedback = []
    common_passwords = {"password123", "12345678", "qwerty", "abc123", "admin"}
    
    if password in common_passwords:
        return 0, ["This is a commonly used password. Choose a more unique one."], {}
    
    criteria = {
        "✅ Length (8+)": len(password) >= 8,
        "🔠 Uppercase Letter": any(char.isupper() for char in password),
        "🔡 Lowercase Letter": any(char.islower() for char in password),
        "🔢 Number": any(char.isdigit() for char in password),
        "🔣 Special Character": bool(re.search(r"[!@#$%^&*]", password))
    }

    strength = sum(criteria.values())

    if not criteria["✅ Length (8+)"]:
        feedback.append("- Password should be at least **8 characters** long.")
    if not criteria["🔠 Uppercase Letter"]:
        feedback.append("- Include at least **one uppercase letter**.")
    if not criteria["🔡 Lowercase Letter"]:
        feedback.append("- Include at least **one lowercase letter**.")
    if not criteria["🔢 Number"]:
        feedback.append("- Add at least **one number (0-9)**.")
    if not criteria["🔣 Special Character"]:
        feedback.append("- Include at least **one special character** (!@#$%^&*).")

    return strength, feedback, criteria

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    st.title("🔒 Password Strength Meter")
    password = st.text_input("Enter your password", type="password")

    if password:
        strength, feedback, criteria = check_password_strength(password)
        st.subheader("🔍 Password Strength Analysis")
        for criterion, met in criteria.items():
            st.markdown(f"✔️ **{criterion}**" if met else f"❌ **{criterion}**")

        strength_level = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
        st.progress(strength / 5)
        st.write(f"**🔹 Strength Level:** {strength_level[strength]}")

        if strength < 5:
            st.error("⚠️ Your password is not strong enough. Consider these improvements:")
            for tip in feedback:
                st.markdown(tip)
        else:
            st.success("🎉 Strong Password!")

    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.text(f"🔑 Suggested Strong Password: {strong_password}")

main()