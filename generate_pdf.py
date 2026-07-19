import markdown
import subprocess
import sys
import os

md_path = "/workspace/vaadi-life-seo-geo-aeo-report.md"
html_path = "/workspace/vaadi-life-seo-geo-aeo-report.html"
pdf_path = "/workspace/vaadi-life-seo-geo-aeo-report.pdf"

with open(md_path, "r") as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code", "nl2br"])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Mono:wght@400;500&display=swap');

  :root {{
    --brand: #1a3c5e;
    --accent: #2e6da4;
    --green: #1a6e45;
    --red: #b91c1c;
    --amber: #92400e;
    --muted: #64748b;
    --border: #e2e8f0;
    --bg-light: #f8fafc;
    --bg-code: #1e293b;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 10.5pt;
    line-height: 1.65;
    color: #1e293b;
    background: #fff;
    padding: 0;
    margin: 0;
  }}

  /* Cover page */
  .cover {{
    background: linear-gradient(135deg, #0f2340 0%, #1a3c5e 50%, #0f4c75 100%);
    color: #fff;
    padding: 60px 50px 50px;
    min-height: 297mm;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}

  .cover .tag {{
    font-size: 8pt;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #93c5fd;
    margin-bottom: 28px;
  }}

  .cover h1 {{
    font-size: 32pt;
    font-weight: 700;
    line-height: 1.15;
    color: #fff;
    margin-bottom: 18px;
    border: none;
    padding: 0;
  }}

  .cover .subtitle {{
    font-size: 13pt;
    color: #bfdbfe;
    margin-bottom: 40px;
    line-height: 1.5;
  }}

  .cover .meta-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 40px;
  }}

  .cover .meta-item {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 10px;
    padding: 16px 18px;
  }}

  .cover .meta-label {{
    font-size: 7.5pt;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #93c5fd;
    margin-bottom: 4px;
  }}

  .cover .meta-value {{
    font-size: 10pt;
    color: #e0f2fe;
    font-weight: 500;
  }}

  .cover .score-box {{
    margin-top: 40px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 12px;
    padding: 24px 28px;
    display: flex;
    align-items: center;
    gap: 28px;
  }}

  .cover .big-score {{
    font-size: 52pt;
    font-weight: 700;
    color: #fbbf24;
    line-height: 1;
  }}

  .cover .score-label {{
    font-size: 10pt;
    color: #bfdbfe;
    line-height: 1.5;
  }}

  .cover .score-label strong {{
    display: block;
    font-size: 13pt;
    color: #fff;
    margin-bottom: 4px;
  }}

  /* Main content wrapper */
  .content {{
    padding: 40px 50px;
    max-width: 780px;
    margin: 0 auto;
  }}

  /* Typography */
  h1 {{
    font-size: 20pt;
    font-weight: 700;
    color: var(--brand);
    margin: 40px 0 16px;
    padding-bottom: 10px;
    border-bottom: 3px solid var(--brand);
    page-break-after: avoid;
  }}

  h2 {{
    font-size: 14pt;
    font-weight: 700;
    color: var(--brand);
    margin: 32px 0 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--border);
    page-break-after: avoid;
  }}

  h3 {{
    font-size: 11.5pt;
    font-weight: 600;
    color: #0f4c75;
    margin: 22px 0 8px;
    page-break-after: avoid;
  }}

  h4 {{
    font-size: 10.5pt;
    font-weight: 600;
    color: #334155;
    margin: 18px 0 6px;
  }}

  p {{ margin: 0 0 12px; }}

  a {{ color: var(--accent); text-decoration: none; }}

  strong {{ font-weight: 600; }}

  em {{ font-style: italic; color: #475569; }}

  hr {{
    border: none;
    border-top: 2px solid var(--border);
    margin: 36px 0;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0 24px;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }}

  thead tr {{
    background: var(--brand);
    color: #fff;
  }}

  thead th {{
    padding: 9px 12px;
    text-align: left;
    font-weight: 600;
    font-size: 8.5pt;
    letter-spacing: 0.05em;
  }}

  tbody tr:nth-child(even) {{ background: var(--bg-light); }}
  tbody tr:hover {{ background: #e0f2fe; }}

  td {{
    padding: 8px 12px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
  }}

  /* Code blocks */
  pre {{
    background: var(--bg-code);
    color: #e2e8f0;
    border-radius: 8px;
    padding: 16px 18px;
    font-family: 'Fira Mono', 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.6;
    overflow-x: auto;
    margin: 14px 0 20px;
    page-break-inside: avoid;
  }}

  code {{
    font-family: 'Fira Mono', 'Courier New', monospace;
    font-size: 8.5pt;
    background: #f1f5f9;
    color: #b91c1c;
    padding: 2px 5px;
    border-radius: 4px;
  }}

  pre code {{
    background: none;
    color: #e2e8f0;
    padding: 0;
  }}

  /* Lists */
  ul, ol {{
    margin: 8px 0 14px 22px;
    padding: 0;
  }}

  li {{ margin-bottom: 5px; }}

  /* Callout boxes */
  blockquote {{
    border-left: 4px solid var(--accent);
    background: #eff6ff;
    margin: 16px 0;
    padding: 14px 18px;
    border-radius: 0 8px 8px 0;
    font-size: 10pt;
    color: #1e3a5f;
  }}

  /* Status indicators in text */
  .status-good {{ color: var(--green); font-weight: 700; }}
  .status-warn {{ color: var(--amber); font-weight: 700; }}
  .status-bad  {{ color: var(--red);   font-weight: 700; }}

  /* Section number badge */
  .section-badge {{
    display: inline-block;
    background: var(--brand);
    color: #fff;
    font-size: 8pt;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 12px;
    margin-right: 8px;
    vertical-align: middle;
  }}

  /* Page breaks */
  .page-break {{ page-break-before: always; }}

  @page {{
    size: A4;
    margin: 18mm 18mm 20mm;
    @bottom-center {{
      content: "vaadi.life — SEO / GEO / AEO Audit · July 2026 · Page " counter(page);
      font-size: 8pt;
      color: #94a3b8;
      font-family: 'Inter', sans-serif;
    }}
  }}

  @media print {{
    .cover {{ min-height: 100vh; }}
  }}
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="tag">Confidential Audit Report · July 2026</div>
  <h1>vaadi.life<br>SEO · GEO · AEO<br>Full Audit Report</h1>
  <div class="subtitle">
    A comprehensive search visibility assessment covering<br>
    Search Engine Optimization, Generative Engine Optimization,<br>
    and Answer Engine Optimization.
  </div>

  <div class="meta-grid">
    <div class="meta-item">
      <div class="meta-label">Property</div>
      <div class="meta-value">Vaadi — Himalayan Homestay</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Location</div>
      <div class="meta-value">Near Auli, Uttarakhand, India</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Website</div>
      <div class="meta-value">https://vaadi.life</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Audit Date</div>
      <div class="meta-value">July 2026</div>
    </div>
  </div>

  <div class="score-box">
    <div class="big-score">4.4</div>
    <div class="score-label">
      <strong>Overall Score — Out of 10</strong>
      Strong product. Critically weak machine-readable signals.<br>
      Significant untapped visibility potential across SEO, GEO, and AEO.
    </div>
  </div>
</div>

<!-- MAIN CONTENT -->
<div class="content">
{html_body}
</div>

</body>
</html>
"""

with open(html_path, "w") as f:
    f.write(html)

print(f"HTML written to {html_path}")

# Generate PDF using weasyprint
sys.path.insert(0, '/home/ubuntu/.local/lib/python3.10/site-packages')
from weasyprint import HTML, CSS
HTML(filename=html_path).write_pdf(pdf_path)
print(f"PDF written to {pdf_path}")
print(f"File size: {os.path.getsize(pdf_path):,} bytes")
