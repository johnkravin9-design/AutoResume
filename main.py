import yaml
import argparse
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def render_resume(data_file, out_file):
    # Load YAML resume data
    with open(data_file, "r") as f:
        data = yaml.safe_load(f)

    doc = SimpleDocTemplate(out_file)
    styles = getSampleStyleSheet()
    story = []

    # === Header ===
    story.append(Paragraph(f"<b>{data['name']}</b>", styles["Title"]))
    if "title" in data:
        story.append(Paragraph(data["title"], styles["Heading2"]))
    story.append(Spacer(1, 12))

    # === Contact Info ===
    if "contact" in data:
        contact_parts = []
        for k, v in data["contact"].items():
            contact_parts.append(f"{k.capitalize()}: {v}")
        story.append(Paragraph(" | ".join(contact_parts), styles["Normal"]))
        story.append(Spacer(1, 12))

    # === Summary ===
    if "summary" in data:
        story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
        story.append(Paragraph(data["summary"], styles["Normal"]))
        story.append(Spacer(1, 12))

    # === Experience ===
    if "experience" in data:
        story.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
        for job in data["experience"]:
            story.append(Paragraph(f"<b>{job['role']}</b> — {job['company']} ({job['years']})", styles["Normal"]))
            if "details" in job:
                story.append(Paragraph(job["details"], styles["Normal"]))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 12))

    # === Education ===
    if "education" in data:
        story.append(Paragraph("<b>Education</b>", styles["Heading2"]))
        for edu in data["education"]:
            story.append(Paragraph(f"{edu['degree']} — {edu['school']} ({edu['years']})", styles["Normal"]))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 12))

    doc.build(story)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to YAML data file")
    parser.add_argument("--out", required=True, help="Output PDF file")
    args = parser.parse_args()

    if not os.path.exists(args.data):
        raise FileNotFoundError(f"YAML file not found: {args.data}")

    render_resume(args.data, args.out)
    print(f"✅ Resume generated: {args.out}")
