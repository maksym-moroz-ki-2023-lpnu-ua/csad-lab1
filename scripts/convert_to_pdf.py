import os
import subprocess
import markdown

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, ".."))
md_path = os.path.join(root_dir, "DEFENSE_QA.md")
html_path = os.path.join(root_dir, "DEFENSE_QA.html")
pdf_path = os.path.join(root_dir, "DEFENSE_QA.pdf")

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert markdown to html with extensions
html_body = markdown.markdown(
    md_content,
    extensions=[
        "tables",
        "fenced_code",
        "codehilite",
        "toc",
        "attr_list"
    ]
)

# Custom CSS for gorgeous printing and PDF reading
css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

@page {
    size: A4;
    margin: 18mm 15mm 20mm 15mm;
    @bottom-right {
        content: counter(page);
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Inter', sans-serif;
    color: #0f172a;
    font-weight: 700;
    page-break-after: avoid;
    break-after: avoid;
}

h1 {
    font-size: 20pt;
    border-bottom: 3px solid #2563eb;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 12px;
    color: #1e3a8a;
}

h2 {
    font-size: 14pt;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 18pt;
    margin-bottom: 8pt;
    color: #1e40af;
}

h3 {
    font-size: 11.5pt;
    margin-top: 14pt;
    margin-bottom: 6pt;
    color: #0369a1;
}

h4 {
    font-size: 10.5pt;
    margin-top: 10pt;
    margin-bottom: 4pt;
    color: #334155;
}

p, ul, ol {
    margin-top: 0;
    margin-bottom: 8pt;
}

li {
    margin-bottom: 3pt;
}

code {
    font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
    font-size: 8.8pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1.5px 4.5px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
}

pre {
    font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
    font-size: 8.5pt;
    background-color: #0f172a;
    color: #f8fafc;
    padding: 10px 12px;
    border-radius: 6px;
    overflow-x: auto;
    page-break-inside: avoid;
    break-inside: avoid;
    margin-bottom: 10pt;
    line-height: 1.4;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 12pt;
    font-size: 9pt;
    page-break-inside: avoid;
    break-inside: avoid;
}

th, td {
    border: 1px solid #cbd5e1;
    padding: 6px 9px;
    text-align: left;
    vertical-align: top;
}

th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 600;
}

tr:nth-child(even) td {
    background-color: #f8fafc;
}

blockquote {
    margin: 8pt 0;
    padding: 6pt 12pt;
    border-left: 4px solid #3b82f6;
    background-color: #eff6ff;
    color: #1e3a8a;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
    break-inside: avoid;
}

blockquote p {
    margin: 0;
}

hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 16pt 0;
}

a {
    color: #2563eb;
    text-decoration: none;
}

.badge {
    display: inline-block;
    padding: 2px 6px;
    font-size: 8pt;
    font-weight: 600;
    border-radius: 4px;
    background-color: #e0f2fe;
    color: #0369a1;
}
"""

full_html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Підготовка до захисту лабораторної роботи №1 - Мороз М.Т.</title>
    <style>
    {css}
    </style>
</head>
<body>
    {html_body}
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("HTML generated at", html_path)

# Run Edge headless to print to PDF
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

print("Converting to PDF using:", edge_path)
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(pdf_path):
    print("SUCCESS: PDF created at", pdf_path, "size:", os.path.getsize(pdf_path), "bytes")
else:
    print("Edge returned:", res.returncode, res.stderr)
