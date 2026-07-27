# 🛡️ CyberQuest CTF – Beginner Web Security Challenges

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![CTF](https://img.shields.io/badge/CTF-Beginner-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A beginner-friendly **Capture The Flag (CTF)** platform designed to introduce fundamental **Web Security** concepts through six hands-on challenges.

Built as an educational project to help students learn offensive security techniques in a safe environment while demonstrating modern development practices using **Git**, **GitHub**, **Docker**, and **GitHub Actions (CI/CD)**.

---

# 📖 Overview

CyberQuest CTF consists of **six progressive levels**, each focusing on a common web security concept encountered during penetration testing and bug bounty hunting.

Whether you're a cybersecurity student or someone taking your first steps into ethical hacking, these challenges provide practical experience with real-world techniques.

## 🎯 Learning Objectives

After completing this CTF, participants will understand:

- HTML Source Code Inspection
- Information Disclosure
- robots.txt Enumeration
- Cookie Analysis
- Browser Developer Tools
- Client-side Validation Bypass
- Base64 Encoding & Decoding
- Command Injection
- Basic Web Enumeration
- Ethical Hacking Methodology

---

# ✨ Features

- 🏴 Six beginner-friendly challenges
- 🌐 Realistic web security scenarios
- 🔍 Hands-on learning approach
- 🐳 Docker support
- ⚙ GitHub Actions CI/CD
- 📚 Beginner-friendly documentation
- 💡 Progressive difficulty
- 🚀 Easy local deployment

---

# 🛠 Tech Stack

- HTML
- CSS
- JavaScript
- Python (Flask)
- Docker
- Git
- GitHub
- GitHub Actions

---

# 📂 Project Structure

```text
6-level-beginner-CTF-with-CI-CD/
│
├── level-1/
├── level-2/
├── level-3/
├── level-4/
├── level-5/
├── level-6/
│
├── .github/
│   └── workflows/
│
├── README.md
└── LICENSE
```

---

# 🚀 Getting Started

## Prerequisites

Before running the project, make sure you have:

- Git
- Python 3.x
- Modern Web Browser
- Docker (Optional)

Clone the repository:

```bash
git clone https://github.com/SilentS13/6-level-beginner-CTF-with-CI-CD.git
```

Navigate into the project:

```bash
cd 6-level-beginner-CTF-with-CI-CD
```

Open Levels 1–5 directly in your browser.

For Level 6:

```bash
cd level-6
pip install -r requirements.txt
python app.py
```

Visit:

```
http://localhost:5000
```

---

# 🏴 Challenge Levels

| Level | Challenge | Topic | Difficulty |
|-------|-----------|--------|------------|
| 1 | The Hidden Path | HTML Comments & Source Code | ⭐ |
| 2 | The Secret List | robots.txt Enumeration | ⭐ |
| 3 | The Cookie Jar | Cookie Manipulation | ⭐⭐ |
| 4 | The Script Kiddie | Client-side Validation Bypass | ⭐⭐ |
| 5 | The Encoded Message | Base64 Encoding | ⭐⭐⭐ |
| 6 | The Command Room | Command Injection | ⭐⭐⭐⭐ |

---

# 🔍 Challenge Details

## Level 1 – The Hidden Path

**Topic**

HTML Comments & Source Code

**Objective**

Find the hidden flag inside the webpage source code.

**Hint**

Use:

- Right Click → View Page Source
- or press **Ctrl + U**

---

## Level 2 – The Secret List

**Topic**

Information Disclosure using `robots.txt`

**Objective**

Locate the hidden directory blocked from search engines.

**Hint**

Visit:

```
/robots.txt
```

---

## Level 3 – The Cookie Jar

**Topic**

Cookie Manipulation

**Objective**

Inspect browser cookies and recover the hidden flag.

**Hint**

Developer Tools → Application (Storage) → Cookies

---

## Level 4 – The Script Kiddie

**Topic**

Client-side Validation Bypass

**Objective**

Enable the disabled button to reveal the flag.

**Hint**

Inspect the HTML element and remove the `disabled` attribute.

---

## Level 5 – The Encoded Message

**Topic**

Base64 Encoding

**Objective**

Decode the provided Base64 string.

**Hint**

Look for strings ending with:

```
==
```

Use any Base64 decoder.

---

## Level 6 – The Command Room

**Topic**

Command Injection

**Objective**

Exploit the vulnerable application to read `flag.txt`.

### Setup

```bash
cd level-6
pip install -r requirements.txt
python app.py
```

Visit

```
http://localhost:5000
```

### Hint

Linux/macOS

```bash
127.0.0.1; cat flag.txt
```

Windows

```cmd
127.0.0.1 & type flag.txt
```

---

# 🏗 Project Workflow

```text
Developer
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
      ▼
Automated Build & Checks
      │
      ▼
Deploy / Run Challenges
      │
      ▼
Player Solves Challenges
```

---

# 📸 Screenshots

Add screenshots here after completing the project.

Example:

```
images/
├── home.png
├── level1.png
├── level6.png
└── github-actions.png
```

---

# 🎓 Skills You Will Learn

- Web Enumeration
- Source Code Analysis
- Browser DevTools
- Cookie Inspection
- Information Disclosure
- Base64 Decoding
- Command Injection
- Basic Web Exploitation
- Git & GitHub Workflow
- Docker Fundamentals
- CI/CD Basics

---

# 🤝 Team Members

| Name | Role |
|------|------|
| **Vinnet Shinde** | Team Lead |
| **Pratham Solanki** | Developer |
| **Manush Patel** | Developer |
| **Parth Patel** | Developer |
| **Mahi Shah** | Developer |

---

# 🔮 Future Improvements

- User Authentication
- Dynamic Flags
- Online Scoreboard
- Hint Unlock System
- Leaderboard
- Docker Compose Support
- More Web Security Challenges
- SQL Injection Level
- XSS Challenge
- File Upload Vulnerability
- Admin Dashboard

---

# 📄 License

This project is intended for **educational purposes only**.

Feel free to use, modify, and share it for learning and classroom activities.

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star this repository
- 🍴 Fork the project
- 📢 Share it with fellow cybersecurity learners

Happy Hacking! 🚩
