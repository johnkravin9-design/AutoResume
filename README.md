# AutoResume

AutoResume is a free and lightweight resume generator.  
It converts your resume data (YAML format) into a styled PDF — no paid API keys required.

## ✨ Features
- Write your resume in simple YAML
- Generate a professional PDF instantly
- 100% offline, no API costs
- Runs on Linux, Termux, macOS, and Windows

## 🚀 Quick Start
```bash
# Clone repo
git clone https://github.com/YOUR-USERNAME/AutoResume.git
cd AutoResume

# Setup environment
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# Generate your resume
python main.py --data sample_resume.yaml --out resume.pdf
