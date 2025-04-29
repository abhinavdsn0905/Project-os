# Secure Authentication Module for Operating Systems

## 📋 Project Overview

In today's interconnected landscape, secure identity verification is critical to safeguard sensitive information and prevent unauthorized access.  
This project develops a **secure authentication module** integrating **multi-factor authentication (MFA)** using:

- Password-based login
- OTP (One-Time Password) verification via Telegram Bot

It strengthens operating systems against modern cyber threats like brute-force attacks, buffer overflow exploits, and credential leaks.

---

## 🎯 Key Objectives

- **Implement Multi-Factor Authentication (MFA)**:
  - Password + OTP-based verification
  - OTPs generated and delivered via Telegram Bot
- **Enhance Security**:
  - Secure password storage using PBKDF2-HMAC-SHA256
  - Protection against brute-force and replay attacks
- **Cross-Platform Compatibility**:
  - Designed for Linux, future scope for Windows/macOS
- **Future Enhancements**:
  - Biometric authentication (Fingerprint)
  - OTP via email or SMS

---

## 🛠️ Features

- ✅ Password authentication with strong hashing
- ✅ OTP-based second-factor authentication via Telegram
- ✅ Protection against buffer overflow and credential leaks
- ✅ SQLite database for secure credential storage
- ✅ Modular and extensible code structure

---

## 🧹 Technologies Used

- **Programming Language**: Python
- **Database**: SQLite
- **Cryptography**:
  - PBKDF2-HMAC-SHA256 for password hashing
  - HMAC for secure password verification
- **Networking**:
  - Telegram Bot API for OTP delivery
  - `requests` library for HTTP communication
- **Version Control**: Git and GitHub
- **Future Enhancements**:
  - Biometric Authentication (libfprint)
  - Email-based OTP (smtplib & ssl)

---

## 🔥 System Architecture

1. **User Registration**:
   - Username, password, and email are provided.
   - Passwords are hashed with a random salt.
   - Credentials are stored securely in the database.

2. **User Authentication**:
   - Verify username and password.
   - Generate and send OTP via Telegram.
   - Verify OTP for successful authentication.

---

## 📂 Project Structure

```plaintext
auth_db.sqlite        # SQLite Database file (created at runtime)
Project.py            # Main Python script (Authentication Module)
README.md             # Project documentation
```

---

## 🚀 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/abhinavdsn0905/Secure-Authentication-Module
   cd Secure-Authentication-Module
   ```

2. Install required libraries:
   ```bash
   pip install requests cryptography
   ```

3. Replace the placeholders in `Project.py` with your Telegram Bot credentials:
   ```python
   TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
   ```

4. Run the project:
   ```bash
   python Project.py
   ```

5. Choose from the menu:
   - Register a new user
   - Authenticate an existing user
   - Exit

---

## 🔐 Security Measures Implemented

- PBKDF2 password hashing with 100,000 iterations
- HMAC-based password verification
- Random 6-digit OTP generation
- OTP delivered securely via Telegram API
- Constant-time comparison to prevent timing attacks
- Secure SQLite storage with username and email fields

---

## 📈 Future Scope

- Biometric authentication (fingerprint scanning)
- OTP delivery via Email and SMS
- Windows and macOS OS integration
- Real-time security event monitoring
- OAuth and Single Sign-On (SSO) support

---

## 📜 References

- [ChatGPT](https://openai.com/)
- [Implementing Secure Authentication and Authorization in System Software - ResearchGate](https://www.researchgate.net/publication/389359231_Implementing_Secure_Authentication_and_Authorization_in_System_Software)
- [Highly Secure Password-Based Authentication Approach - ResearchGate](https://www.researchgate.net/publication/386071817_Highly_Secure_and_Easy_to_Remember_PasswordBased_Authentication_Approach)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  
Make sure to update tests as appropriate.

---

## 📄 License

This project is for academic and educational purposes.  
Commercial usage may require prior approval.
