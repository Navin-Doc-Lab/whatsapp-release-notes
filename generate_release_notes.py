import json
from jinja2 import Template
import pdfkit

# Load JSON data
with open("release_notes_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load HTML template
with open("release_notes_template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# Render HTML
template = Template(template_content)
rendered_html = template.render(**data)

# Save HTML
with open("release_notes_output.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("✅ HTML file generated: release_notes_output.html")

# Optional: Save as PDF
try:
    pdfkit.from_string(rendered_html, "release_notes_output.pdf")
    print("✅ PDF file generated: release_notes_output.pdf")
except Exception as e:
    print("⚠️ PDF generation failed. Make sure wkhtmltopdf is installed.")
    print(e)
