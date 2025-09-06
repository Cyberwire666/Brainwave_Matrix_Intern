

# 🛡️ Phishing Link Scanner

A simple Python tool to detect and analyze suspicious URLs for phishing indicators.
The scanner uses both **manual checks** (like detecting URL shorteners or suspicious keywords) and **Google Safe Browsing API** for verification.

---

## 🚀 Features

* Detects **shortened URLs** (e.g., `bit.ly`, `tinyurl`, etc.)
* Identifies **suspicious keywords** in URLs (e.g., `login`, `secure`, `bank`, `verify`)
* Integrates with **Google Safe Browsing API** for real-time threat detection
* Provides a **final safety verdict**

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Cyberwire666/Brainwave_Matrix_Intern.git
   
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

---

## 🔑 Setup Google Safe Browsing API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable **Google Safe Browsing API**
4. Create an **API key**
5. Add your key in the script:

   ```python
   GOOGLE_API_KEY = "your_api_key_here"
   ```

---

## ▶️ Usage

Run the script:

```bash
python simple_phishing_scanner.py
```

Enter a URL when prompted:

```
🔗 Enter the URL to check: https://bit.ly/3abcXYZ

🔍 Scanning URL: bit.ly

--- Manual Check Results ---
⚠️ Suspicious indicators found:
   - Shortened URL (URL shortener detected)

--- Google Safe Browsing Check ---
✅ This URL is safe (Google Safe Browsing).

--- Final Report ---
❌ This URL is NOT safe! Avoid opening it.
```

---

## 🧪 Example Test URLs

You can try scanning these sample URLs:

* Safe:

  * `https://www.google.com`
  * `https://www.wikipedia.org`

* Suspicious:

  * `https://bit.ly/3abcXYZ` (shortened)
  * `http://secure-login-verification.com` (fake login)

---

## ⚠️ Disclaimer

This tool is for **educational and security awareness purposes only**.
It should not be considered a fully comprehensive phishing detection system.
Always use caution before clicking unknown links.

---

# 🔐 Password Strength Checker  

A **Great, Impressive, and User-Friendly** tool built in Python to assess the strength of passwords entered by users.  
It analyzes length, complexity, and uniqueness to provide **clear feedback** on password strength.  

---

## ✨ Features  

- ✅ Checks **password length**  
- ✅ Analyzes **character variety** (uppercase, lowercase, digits, symbols)  
- ✅ Detects **common/weak passwords**  
- ✅ Provides **step-by-step feedback** with emojis for friendliness  
- ✅ Interactive **CLI tool** (keeps running until user exits)  

---

## 🚀 Demo  

```bash
$ python password_checker.py
🔐 Welcome to the Password Strength Checker 🔐

Enter a password (or type 'exit' to quit): hello123
Password Strength: 🟠 Medium
✅ Good length.
❌ Add uppercase letters.
❌ Add special characters (e.g. @, #, $).


## YEHIA TAREK
