from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Flowable

from report_expansions import (
    expand_ch1, expand_ch2, expand_ch3, expand_ch4, expand_ch4b, expand_ch5,
    expand_ch6, expand_ch7, expand_ch7b, expand_ch8, expand_ch9, expand_ch10,
    expand_ch11, expand_ch11b, expand_ch11c, expand_ch12, expand_ch13, expand_ch14,
    expand_ch15, expand_ch16, expand_ch17, expand_ch18, expand_ch19,
    expand_appendices, expand_viva_extra,
)

# ─────────────────────── Color Palette ───────────────────────
GREEN_DARK   = colors.HexColor("#1a5c38")   # primary brand
GREEN_MED    = colors.HexColor("#2d7a50")
GREEN_LIGHT  = colors.HexColor("#e8f5ee")   # cell shading
ACCENT       = colors.HexColor("#f0a500")   # gold accent
GRAY_DARK    = colors.HexColor("#2c3e50")
GRAY_MID     = colors.HexColor("#7f8c8d")
GRAY_LIGHT   = colors.HexColor("#ecf0f1")
WHITE        = colors.white

PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm


# ─────────────────────── Custom Flowables ─────────────────────
class ColorBar(Flowable):
    """Horizontal colored bar used as a section separator."""
    def __init__(self, color=GREEN_DARK, height=4, width=None):
        super().__init__()
        self.bar_color = color
        self.bar_height = height
        self.bar_width = width or (PAGE_W - 2 * MARGIN)
    def draw(self):
        self.canv.setFillColor(self.bar_color)
        self.canv.rect(0, 0, self.bar_width, self.bar_height, fill=1, stroke=0)
    def wrap(self, *_):
        return self.bar_width, self.bar_height


# ─────────────────────── Styles ───────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    s = {}

    s["cover_title"] = ParagraphStyle(
        "cover_title", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=32,
        textColor=WHITE, alignment=TA_CENTER,
        spaceAfter=6, leading=40
    )
    s["cover_subtitle"] = ParagraphStyle(
        "cover_subtitle", parent=base["Normal"],
        fontName="Helvetica", fontSize=16,
        textColor=ACCENT, alignment=TA_CENTER,
        spaceAfter=4, leading=22
    )
    s["cover_minor"] = ParagraphStyle(
        "cover_minor", parent=base["Normal"],
        fontName="Helvetica", fontSize=11,
        textColor=WHITE, alignment=TA_CENTER,
        spaceAfter=3, leading=16
    )
    s["cover_label"] = ParagraphStyle(
        "cover_label", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=10,
        textColor=ACCENT, alignment=TA_CENTER,
        spaceAfter=2
    )
    s["cover_value"] = ParagraphStyle(
        "cover_value", parent=base["Normal"],
        fontName="Helvetica", fontSize=10,
        textColor=WHITE, alignment=TA_CENTER,
        spaceAfter=2
    )

    s["chapter_heading"] = ParagraphStyle(
        "chapter_heading", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=18,
        textColor=WHITE, alignment=TA_LEFT,
        spaceBefore=0, spaceAfter=0, leading=24
    )
    s["section_heading"] = ParagraphStyle(
        "section_heading", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=13,
        textColor=GREEN_DARK, alignment=TA_LEFT,
        spaceBefore=14, spaceAfter=5, leading=18
    )
    s["subsection_heading"] = ParagraphStyle(
        "subsection_heading", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=11,
        textColor=GREEN_MED, alignment=TA_LEFT,
        spaceBefore=10, spaceAfter=4, leading=16
    )
    s["body"] = ParagraphStyle(
        "body", parent=base["Normal"],
        fontName="Helvetica", fontSize=10,
        textColor=GRAY_DARK, alignment=TA_JUSTIFY,
        spaceAfter=6, leading=15
    )
    s["body_center"] = ParagraphStyle(
        "body_center", parent=base["Normal"],
        fontName="Helvetica", fontSize=10,
        textColor=GRAY_DARK, alignment=TA_CENTER,
        spaceAfter=6, leading=15
    )
    s["bullet"] = ParagraphStyle(
        "bullet", parent=base["Normal"],
        fontName="Helvetica", fontSize=10,
        textColor=GRAY_DARK, alignment=TA_LEFT,
        spaceAfter=4, leading=15,
        leftIndent=16, bulletIndent=0
    )
    s["code"] = ParagraphStyle(
        "code", parent=base["Normal"],
        fontName="Courier", fontSize=8,
        textColor=GRAY_DARK, alignment=TA_LEFT,
        spaceAfter=2, leading=12,
        leftIndent=8
    )
    s["caption"] = ParagraphStyle(
        "caption", parent=base["Normal"],
        fontName="Helvetica-Oblique", fontSize=9,
        textColor=GRAY_MID, alignment=TA_CENTER,
        spaceAfter=6
    )
    s["toc_chapter"] = ParagraphStyle(
        "toc_chapter", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=10,
        textColor=GREEN_DARK,
        spaceAfter=3, leading=15
    )
    s["toc_item"] = ParagraphStyle(
        "toc_item", parent=base["Normal"],
        fontName="Helvetica", fontSize=10,
        textColor=GRAY_DARK,
        spaceAfter=2, leading=14, leftIndent=12
    )
    s["abstract_text"] = ParagraphStyle(
        "abstract_text", parent=base["Normal"],
        fontName="Helvetica", fontSize=10.5,
        textColor=GRAY_DARK, alignment=TA_JUSTIFY,
        spaceAfter=8, leading=17
    )
    s["cert_text"] = ParagraphStyle(
        "cert_text", parent=base["Normal"],
        fontName="Helvetica", fontSize=11,
        textColor=GRAY_DARK, alignment=TA_JUSTIFY,
        spaceAfter=10, leading=18
    )
    s["sig_name"] = ParagraphStyle(
        "sig_name", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=11,
        textColor=GRAY_DARK,
        spaceAfter=2, leading=16
    )
    s["sig_detail"] = ParagraphStyle(
        "sig_detail", parent=base["Normal"],
        fontName="Helvetica", fontSize=10,
        textColor=GRAY_DARK,
        spaceAfter=2, leading=14
    )
    s["page_heading"] = ParagraphStyle(
        "page_heading", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=16,
        textColor=GREEN_DARK, alignment=TA_CENTER,
        spaceBefore=0, spaceAfter=16, leading=22
    )
    s["keyword"] = ParagraphStyle(
        "keyword", parent=base["Normal"],
        fontName="Helvetica-Oblique", fontSize=9.5,
        textColor=GREEN_MED, alignment=TA_LEFT,
        spaceAfter=4
    )
    return s


# ─────────────────────── Table Helpers ────────────────────────
def std_table(data, col_widths=None, header=True):
    """Build a styled table. First row is header if header=True."""
    avail = PAGE_W - 2 * MARGIN
    if col_widths is None:
        n = len(data[0])
        col_widths = [avail / n] * n

    style_cmds = [
        ("GRID",       (0,0), (-1,-1), 0.4, colors.HexColor("#bdc3c7")),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [WHITE, GRAY_LIGHT]),
        ("FONTNAME",   (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE",   (0,0), (-1,-1), 9),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 7),
        ("RIGHTPADDING",  (0,0), (-1,-1), 7),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ]
    if header:
        style_cmds += [
            ("BACKGROUND",  (0,0), (-1,0), GREEN_DARK),
            ("TEXTCOLOR",   (0,0), (-1,0), WHITE),
            ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",    (0,0), (-1,0), 9.5),
            ("ROWBACKGROUNDS", (1,0), (-1,-1), [WHITE, GREEN_LIGHT]),
        ]
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle(style_cmds))
    return t


def chapter_block(title, styles):
    """Return list of flowables for a chapter header bar."""
    bar_h = 36
    class ChapterBar(Flowable):
        def __init__(self):
            super().__init__()
        def draw(self):
            w = PAGE_W - 2 * MARGIN
            c = self.canv
            # dark green background
            c.setFillColor(GREEN_DARK)
            c.roundRect(0, 0, w, bar_h, 6, fill=1, stroke=0)
            # gold left accent
            c.setFillColor(ACCENT)
            c.rect(0, 0, 6, bar_h, fill=1, stroke=0)
            # title text
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 14)
            c.drawString(16, 11, title)
        def wrap(self, *_):
            return PAGE_W - 2 * MARGIN, bar_h

    return [Spacer(1, 14), ChapterBar(), Spacer(1, 12)]


# ─────────────────────── Cover Page ───────────────────────────
def cover_page(story, styles):
    class CoverBg(Flowable):
        def draw(self):
            c = self.canv
            w = PAGE_W - 2 * MARGIN
            h = PAGE_H - 2 * MARGIN
            # full-page dark gradient simulation via rects
            c.setFillColor(GREEN_DARK)
            c.rect(-MARGIN, -MARGIN, PAGE_W, PAGE_H, fill=1, stroke=0)
            # subtle lighter band
            c.setFillColor(GREEN_MED)
            c.rect(-MARGIN, PAGE_H * 0.55 - MARGIN, PAGE_W, PAGE_H * 0.15, fill=1, stroke=0)
            # decorative circles
            c.setFillColorRGB(1,1,1,0.04)
            c.circle(PAGE_W - MARGIN - 60, PAGE_H - MARGIN - 60, 120, fill=1, stroke=0)
            c.circle(-MARGIN + 40, -MARGIN + 40, 90, fill=1, stroke=0)
            # gold accent bar at bottom
            c.setFillColor(ACCENT)
            c.rect(-MARGIN, -MARGIN, PAGE_W, 8, fill=1, stroke=0)
        def wrap(self, *_):
            return 0, 0

    story.append(CoverBg())
    story.append(Spacer(1, 60))
    story.append(Paragraph("🐄", ParagraphStyle("emoji", fontName="Helvetica", fontSize=48,
                                                  alignment=TA_CENTER, textColor=ACCENT,
                                                  spaceAfter=4)))
    story.append(Paragraph("CATTLECLOUD", styles["cover_title"]))
    story.append(Paragraph("Smart Livestock Management System", styles["cover_subtitle"]))
    story.append(Spacer(1, 10))
    story.append(ColorBar(ACCENT, 2))
    story.append(Spacer(1, 20))
    story.append(Paragraph("A Minor Project Report", styles["cover_minor"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Submitted in partial fulfillment of the requirements for the award of",
        styles["cover_minor"]))
    story.append(Paragraph(
        "Bachelor of Technology / Bachelor of Computer Applications",
        styles["cover_minor"]))
    story.append(Spacer(1, 30))

    # meta table
    meta = [
        ["Project Title", "CattleCloud — Smart Livestock Management System"],
        ["Project Type",  "Full-Stack Web Application"],
        ["Session",       "2025–2026"],
        ["Report Date",   "May 2026"],
        ["Repository",    "minorproject (Monorepo)"],
    ]
    col_w = [(PAGE_W - 2*MARGIN) * 0.35, (PAGE_W - 2*MARGIN) * 0.65]
    cell_style = ParagraphStyle("cs", fontName="Helvetica", fontSize=10, textColor=GRAY_DARK, leading=14)
    cell_bold  = ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=10, textColor=GREEN_DARK, leading=14)
    table_data = [[Paragraph(r, cell_bold), Paragraph(v, cell_style)] for r, v in meta]
    t = Table(table_data, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), WHITE),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#bdc3c7")),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[WHITE, GREEN_LIGHT]),
    ]))
    story.append(t)
    story.append(Spacer(1, 34))

    story.append(Paragraph("Developed by the Project Team", styles["cover_label"]))
    story.append(Paragraph("Student Name 1 · Student Name 2 · (Add members)", styles["cover_minor"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Under the Guidance of", styles["cover_label"]))
    story.append(Paragraph("Guide Name, Designation", styles["cover_minor"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Department of Computer Science / Information Technology", styles["cover_minor"]))
    story.append(Paragraph("Institution Name, City", styles["cover_minor"]))

    story.append(PageBreak())


# ─────────────────────── Certificate ──────────────────────────
def certificate_page(story, styles):
    story.append(Paragraph("CERTIFICATE", styles["page_heading"]))
    story.append(ColorBar(GREEN_DARK, 3))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        'This is to certify that the project report entitled <b>"CattleCloud — Smart Livestock '
        'Management System"</b> submitted by <b>____________</b> to <b>____________ University/College</b> '
        'in partial fulfillment of the requirements for the award of <b>____________</b> is a record of '
        'bonafide work carried out under my supervision.',
        styles["cert_text"]))
    story.append(Paragraph(
        'The matter embodied in this report has not been submitted earlier for the award of any '
        'other degree/diploma to the best of my knowledge.',
        styles["cert_text"]))
    story.append(Spacer(1, 40))

    sig_data = [
        [Paragraph("<b>Guide Name</b>", styles["sig_name"]),
         Paragraph("<b>Head of Department</b>", styles["sig_name"])],
        [Paragraph("Designation", styles["sig_detail"]),
         Paragraph("Department", styles["sig_detail"])],
        [Paragraph("Signature: _______________", styles["sig_detail"]),
         Paragraph("Signature: _______________", styles["sig_detail"])],
        [Paragraph("Date: _______________", styles["sig_detail"]),
         Paragraph("Date: _______________", styles["sig_detail"])],
    ]
    half = (PAGE_W - 2*MARGIN) / 2
    t = Table(sig_data, colWidths=[half, half])
    t.setStyle(TableStyle([
        ("VALIGN",     (0,0),(-1,-1),"TOP"),
        ("TOPPADDING", (0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t)
    story.append(PageBreak())


# ─────────────────────── Declaration ──────────────────────────
def declaration_page(story, styles):
    story.append(Paragraph("DECLARATION", styles["page_heading"]))
    story.append(ColorBar(GREEN_DARK, 3))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        'We hereby declare that the project work entitled <b>"CattleCloud — Smart Livestock '
        'Management System"</b> submitted to <b>____________ Institution</b> is an authentic record of '
        'our own work carried out during the academic year <b>2025–2026</b> under the supervision of '
        '<b>____________</b>.',
        styles["cert_text"]))
    story.append(Paragraph(
        'This work has not been submitted elsewhere for a degree or diploma. We have given due '
        'acknowledgments wherever materials from other sources have been used.',
        styles["cert_text"]))
    story.append(Spacer(1, 40))

    headers = ["Student Name", "Roll No.", "Signature", "Date"]
    rows = [headers] + [["", "", "", ""], ["", "", "", ""]]
    col_w = [(PAGE_W-2*MARGIN)*x for x in [0.35, 0.15, 0.3, 0.2]]
    story.append(std_table(rows, col_widths=col_w))
    story.append(PageBreak())


# ─────────────────────── Acknowledgement ──────────────────────
def acknowledgement_page(story, styles):
    story.append(Paragraph("ACKNOWLEDGEMENT", styles["page_heading"]))
    story.append(ColorBar(GREEN_DARK, 3))
    story.append(Spacer(1, 20))
    paras = [
        'We express our sincere gratitude to our project guide <b>____________</b> for continuous '
        'support, valuable suggestions, and encouragement throughout the development of CattleCloud.',
        'We thank the <b>Head of the Department</b> and all faculty members for providing laboratory '
        'facilities and academic guidance.',
        'We are grateful to our families and peers for their motivation during the implementation '
        'and testing phases of this application.',
        'Finally, we acknowledge the open-source communities behind <b>React</b>, <b>Node.js</b>, '
        '<b>Express</b>, <b>MongoDB</b>, and <b>Vite</b>, whose tools made this project feasible '
        'within an academic timeline.',
    ]
    for p in paras:
        story.append(Paragraph(p, styles["cert_text"]))
    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>Team Members</b>", styles["sig_name"]))
    story.append(PageBreak())


# ─────────────────────── Abstract ─────────────────────────────
def abstract_page(story, styles):
    story.append(Paragraph("ABSTRACT", styles["page_heading"]))
    story.append(ColorBar(GREEN_DARK, 3))
    story.append(Spacer(1, 20))

    abstract_paras = [
        'Livestock farming remains a critical sector in rural economies, yet many small and medium '
        'farmers continue to rely on informal record-keeping. Missed vaccination schedules, '
        'inconsistent milk yield tracking, and poor visibility into farm expenses directly affect '
        'productivity and income. <b>CattleCloud</b> addresses these challenges through a '
        'browser-based <b>Smart Livestock Management System</b> that centralizes operational data '
        'in one secure dashboard.',

        'The system is implemented as a <b>three-tier web application</b>. The <b>presentation tier</b> '
        'is a React 19 single-page application built with Vite, offering bilingual support in '
        '<b>English and Hindi</b>. The <b>application tier</b> is a RESTful API developed with '
        'Express 5 and Node.js, using JSON Web Tokens (JWT) and bcrypt for authentication. The '
        '<b>data tier</b> is MongoDB, accessed through Mongoose schemas for users, animals, milk '
        'records, vaccinations, and financial transactions.',

        'Key capabilities include farmer registration and login, per-user data isolation, animal '
        'registry with Indian cattle and buffalo breeds, milk production logging with revenue '
        'estimation at Rs. 70 per litre, vaccination scheduling with automatic booster date '
        'calculation, and an expense/profit ledger with net farm profit/loss summary. A marketing '
        'landing page, Chart.js-based farmer dashboard, and Netlify deployment configuration '
        'complete the solution.',

        'The project demonstrates practical full-stack engineering suitable for academic evaluation. '
        'Certain features remain in prototype state — department-level analytics dashboard, '
        'server-integrated password recovery, and environment-based API configuration — which are '
        'documented as future enhancements.',

        'The repository is organized as a monorepo: backend/ hosts the Express API and Mongoose '
        'models; smart-livestock-dashboard/ contains the React client built with Vite; data/ holds '
        'legacy JSON samples from early prototyping. Farmers interact through standard HTML forms and '
        'tables; administrators (future scope) would use aggregated dashboards once backend analytics '
        'endpoints are implemented.',

        'From a software engineering perspective, the project applies separation of concerns, '
        'stateless authentication, and multi-tenant data isolation at the query level. These patterns '
        'mirror production systems while keeping the codebase small enough for code review during viva '
        'and minor project evaluation.',
    ]
    for p in abstract_paras:
        story.append(Paragraph(p, styles["abstract_text"]))

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        '<b>Keywords:</b> Livestock management, MERN-style stack, React, Express, MongoDB, JWT, '
        'dairy farming, vaccination tracking, bilingual web application.',
        styles["keyword"]))
    story.append(PageBreak())


# ─────────────────────── TOC ──────────────────────────────────
def toc_page(story, styles):
    story.append(Paragraph("TABLE OF CONTENTS", styles["page_heading"]))
    story.append(ColorBar(GREEN_DARK, 3))
    story.append(Spacer(1, 16))

    chapters = [
        ("1",  "Introduction"),
        ("2",  "Literature Survey & Existing Systems"),
        ("3",  "Problem Definition & Objectives"),
        ("4",  "System Analysis"),
        ("5",  "System Design"),
        ("6",  "Technology Stack"),
        ("7",  "Implementation — Backend"),
        ("8",  "Implementation — Frontend"),
        ("9",  "Database Design"),
        ("10", "Security & Authentication"),
        ("11", "User Interface & Screen Documentation"),
        ("12", "Algorithms & Business Logic"),
        ("13", "API Reference (Complete)"),
        ("14", "Testing & Validation"),
        ("15", "Deployment & DevOps"),
        ("16", "Results & Discussion"),
        ("17", "Limitations & Known Issues"),
        ("18", "Future Scope"),
        ("19", "Conclusion"),
        ("A",  "Appendix A — Project Directory Structure"),
        ("B",  "Appendix B — Glossary"),
        ("C",  "Appendix C — References"),
        ("D",  "Appendix D — Viva Preparation (Question Bank)"),
        ("E",  "Appendix E — Translation Module Overview"),
        ("F",  "Appendix F — Team Contribution Template"),
    ]

    avail = PAGE_W - 2 * MARGIN
    ch_w, title_w = avail * 0.10, avail * 0.90
    rows = []
    for num, title in chapters:
        bold = num.isdigit() and len(num) <= 2
        style = styles["toc_chapter"] if bold else styles["toc_item"]
        rows.append([
            Paragraph(f"<b>{num}</b>" if bold else num, style),
            Paragraph(f"<b>{title}</b>" if bold else title, style),
        ])

    t = Table(rows, colWidths=[ch_w, title_w])
    t.setStyle(TableStyle([
        ("VALIGN",       (0,0),(-1,-1),"TOP"),
        ("TOPPADDING",   (0,0),(-1,-1), 3),
        ("BOTTOMPADDING",(0,0),(-1,-1), 3),
        ("LEFTPADDING",  (0,0),(-1,-1), 0),
        ("LINEBELOW",    (0,0),(-1,-1), 0.3, GRAY_LIGHT),
    ]))
    story.append(t)
    story.append(PageBreak())


# ─────────────────────── Content Helpers ──────────────────────
def h2(text, styles): return Paragraph(text, styles["section_heading"])
def h3(text, styles): return Paragraph(text, styles["subsection_heading"])
def body(text, styles): return Paragraph(text, styles["body"])
def sp(n=8): return Spacer(1, n)
def bullet(text, styles): return Paragraph(f"• {text}", styles["bullet"])

def info_table(rows, styles, widths=None):
    """Two-column key-value table."""
    avail = PAGE_W - 2 * MARGIN
    w = widths or [avail*0.3, avail*0.7]
    cell = ParagraphStyle("it", fontName="Helvetica", fontSize=9.5, textColor=GRAY_DARK, leading=14)
    cell_b = ParagraphStyle("itb", fontName="Helvetica-Bold", fontSize=9.5, textColor=GREEN_DARK, leading=14)
    data = [[Paragraph(r, cell_b), Paragraph(v, cell)] for r, v in rows]
    t = Table(data, colWidths=w)
    t.setStyle(TableStyle([
        ("GRID",          (0,0),(-1,-1), 0.4, colors.HexColor("#bdc3c7")),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[WHITE, GREEN_LIGHT]),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 7),
        ("RIGHTPADDING",  (0,0),(-1,-1), 7),
    ]))
    return t


def code_block(lines, styles):
    """Render a code block with light background."""
    avail = PAGE_W - 2 * MARGIN
    cell_style = ParagraphStyle("cb2", fontName="Courier", fontSize=8,
                                 textColor=GRAY_DARK, leading=12)
    content = "<br/>".join(
        line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
        for line in lines
    )
    p = Paragraph(content, cell_style)
    t = Table([[p]], colWidths=[avail])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), colors.HexColor("#f4f6f8")),
        ("BOX",           (0,0),(-1,-1), 0.5, colors.HexColor("#bdc3c7")),
        ("LEFTPADDING",   (0,0),(-1,-1), 10),
        ("RIGHTPADDING",  (0,0),(-1,-1), 10),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
    ]))
    return t


# ─────────────────────── Chapters ─────────────────────────────

def ch1_intro(story, styles):
    story += chapter_block("Chapter 1 — Introduction", styles)
    story.append(h2("1.1 Background", styles))
    story.append(body(
        'India is among the largest milk-producing countries globally, with millions of households '
        'engaged in dairy and mixed livestock farming. Despite digital initiatives in agriculture, '
        'a significant portion of cattle owners still maintain records manually — notebooks, wall '
        'calendars, or verbal memory — for animal identity, milk quantities, veterinary visits, '
        'and cash flows.', styles))
    story.append(body('Manual systems introduce errors and delays:', styles))
    for b in [
        'A missed <b>Foot and Mouth Disease (FMD)</b> booster can affect herd health and marketability.',
        'Without daily milk logs, farmers cannot identify high-yield versus low-yield animals.',
        'Expenses scattered across feed, labor, and veterinary bills make <b>net profitability</b> unclear.',
    ]:
        story.append(bullet(b, styles))
    story.append(sp())
    story.append(body(
        '<b>CattleCloud</b> was conceived as an academic full-stack project to model a digital '
        'livestock management solution using modern, industry-relevant technologies.', styles))

    story.append(h2("1.2 About the Project", styles))
    story.append(body(
        '<b>CattleCloud</b> (repository folder: <i>smart-livestock-dashboard</i>) is a web-based '
        'livestock management platform targeting individual farmers. After authentication, a farmer can:', styles))
    for b in [
        'Register and maintain animals with breed, age, gender, purchase cost, and health status.',
        'Record milk production per animal per day.',
        'Maintain vaccination history with computed next-due dates.',
        'Track expenses and profits under categorized ledgers.',
        'View a dashboard with KPI cards and weekly milk production charts.',
        'Access a public marketing landing page with feature descriptions and FAQ.',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("1.3 Scope of the Project", styles))
    story.append(h3("In Scope", styles))
    for b in [
        'User registration and login against MongoDB.',
        'JWT-based session tokens for API authorization.',
        'CRUD operations for animals, milk, vaccinations, and expenses.',
        'User-scoped data access on the server.',
        'Bilingual UI strings (English / Hindi).',
        'Farmer dashboard with Chart.js visualization.',
        'Profile management with image upload (base64 stored in database).',
        'Frontend build and Netlify SPA configuration.',
    ]:
        story.append(bullet(b, styles))

    story.append(h3("Out of Scope (Current Version)", styles))
    for b in [
        'SMS/email notifications for vaccine reminders.',
        'Real-time IoT sensor integration (automated milk meters, RFID tags).',
        'Native Android/iOS applications.',
        'Multi-farm enterprise hierarchy.',
        'Fully functional government department dashboard (placeholder only).',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("1.5 Target Users", styles))
    headers = ["User Type", "Description", "System Support"]
    rows = [headers,
            ["Farmer", "Primary operator managing own herd", "Full module access after login"],
            ["Guest", "Visitor exploring product", "Landing page only"],
            ["Department Official", "Aggregated regional view", "Route exists; static placeholder"]]
    story.append(std_table(rows, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.2,0.45,0.35]]))
    expand_ch1(story, styles, body, h2, h3, bullet, sp, std_table, PAGE_W, MARGIN, PageBreak)
    story.append(PageBreak())


def ch2_literature(story, styles):
    story += chapter_block("Chapter 2 — Literature Survey & Existing Systems", styles)
    story.append(h2("2.1 Traditional Manual Systems", styles))
    story.append(body(
        'Traditional farm management relies on paper registers. Advantages include zero technology '
        'cost and no learning curve. Disadvantages include: no automatic search or filtering, no '
        'aggregation without manual calculation, high risk of data loss, and difficult backup and '
        'sharing with veterinarians or cooperatives.', styles))

    story.append(h2("2.2 Spreadsheet-Based Systems", styles))
    story.append(body(
        'Farmers and cooperatives often use Microsoft Excel or Google Sheets. These improve '
        'calculability but lack structured validation, role-based access control, mobile-optimized '
        'workflows, and integrated per-farmer authentication.', styles))

    story.append(h2("2.3 Commercial Livestock Software", styles))
    story.append(body(
        'Commercial solutions offer comprehensive modules but are expensive for smallholders, '
        'over-engineered for a minor project scope, and dependent on vendor lock-in and training. '
        '<b>CattleCloud</b> intentionally scopes down to core modules teachable within one '
        'academic semester while using the same architectural patterns.', styles))

    story.append(h2("2.4 Comparative Summary", styles))
    headers = ["Feature", "Paper", "Excel", "CattleCloud"]
    rows = [headers,
            ["Search/filter animals", "Poor", "Medium", "Yes"],
            ["Per-user cloud storage", "No", "Manual", "Yes (MongoDB)"],
            ["Vaccine reminder logic", "No", "Manual", "Partial (UI alerts)"],
            ["Mobile browser access", "N/A", "Medium", "Yes"],
            ["Auth & privacy", "N/A", "Weak", "JWT + user filter"],
            ["Cost", "Low", "Low/Medium", "Hosting dependent"]]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.35, 0.15, 0.15, 0.35]]
    story.append(std_table(rows, col_widths=w))
    expand_ch2(story, styles, body, h2, bullet, sp, std_table, PAGE_W, MARGIN)
    story.append(PageBreak())


def ch3_problem(story, styles):
    story += chapter_block("Chapter 3 — Problem Definition & Objectives", styles)
    story.append(h2("3.1 Problem Statement", styles))
    # highlight box
    avail = PAGE_W - 2 * MARGIN
    ps = ParagraphStyle("ps2", fontName="Helvetica-Oblique", fontSize=10.5,
                         textColor=GREEN_DARK, leading=17)
    p = Paragraph(
        'Small and medium livestock farmers lack an affordable, simple, and language-accessible '
        'digital system to record animals, milk yield, vaccinations, and expenses in one place, '
        'leading to operational inefficiency and financial opacity.', ps)
    t = Table([[p]], colWidths=[avail])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0),(-1,-1), GREEN_LIGHT),
        ("BOX",         (0,0),(-1,-1), 1, GREEN_DARK),
        ("LEFTPADDING", (0,0),(-1,-1), 14),
        ("RIGHTPADDING",(0,0),(-1,-1), 14),
        ("TOPPADDING",  (0,0),(-1,-1), 10),
        ("BOTTOMPADDING",(0,0),(-1,-1),10),
    ]))
    story.append(t)
    story.append(sp(12))

    story.append(h2("3.2 Need for the System", styles))
    for b in [
        '<b>Health compliance</b> — Timely vaccinations reduce disease outbreaks.',
        '<b>Productivity</b> — Milk logs help identify best-performing animals.',
        '<b>Financial clarity</b> — Combined expense and profit entries support net margin understanding.',
        '<b>Digital literacy</b> — Simple forms and Hindi language lower adoption barriers.',
        '<b>Academic learning</b> — Demonstrates end-to-end full-stack development.',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("3.3 Primary Objectives", styles))
    headers = ["ID", "Objective", "Success Criteria"]
    rows = [headers,
            ["O1", "Secure user accounts", "Register/login works; passwords hashed"],
            ["O2", "Animal registry", "Add/list/delete animals per user"],
            ["O3", "Milk tracking", "Records stored and shown in table + dashboard"],
            ["O4", "Vaccination records", "Schedule stored with next due date"],
            ["O5", "Financial ledger", "Expense/profit entries with net summary"],
            ["O6", "Dashboard analytics", "KPI cards + weekly bar chart"],
            ["O7", "Bilingual UI", "Toggle EN/HI on key screens"]]
    story.append(std_table(rows, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.08, 0.35, 0.57]]))

    story.append(h2("3.4 Constraints", styles))
    for b in [
        'Development time bounded by academic calendar.',
        'Single MongoDB instance (no sharding).',
        'Hardcoded milk price (Rs. 70/L) for revenue estimation.',
        'API base URL fixed to localhost:5000 in development.',
    ]:
        story.append(bullet(b, styles))
    expand_ch3(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN)
    story.append(PageBreak())


def ch4_analysis(story, styles):
    story += chapter_block("Chapter 4 — System Analysis", styles)
    story.append(h2("4.1 Functional Requirements", styles))

    fr = [
        ("FR-1.1", "User shall register with name, email, password."),
        ("FR-1.2", "User shall login and receive JWT."),
        ("FR-1.3", "Protected pages shall require authentication flag."),
        ("FR-2.1", "User shall add animal with ID, breed, age, gender, cost, health."),
        ("FR-2.2", "User shall view list of own animals only."),
        ("FR-2.3", "User shall delete own animals."),
        ("FR-2.4", "User shall search animals by ID substring."),
        ("FR-3.1", "User shall log milk quantity per animal per date."),
        ("FR-3.2", "System shall display per-record income at configured rate."),
        ("FR-4.1", "User shall select vaccine from predefined list."),
        ("FR-4.2", "System shall compute upcoming booster date from rules."),
        ("FR-4.3", "UI shall warn if booster due within 3 days."),
        ("FR-5.1", "User shall record type Expense or Profit."),
        ("FR-5.2", "Categories shall depend on type selected."),
        ("FR-5.3", "System shall compute totals and net profit/loss."),
        ("FR-6.1", "Display animal count, milk metrics, farm score."),
        ("FR-6.2", "Display weekly milk bar chart."),
    ]
    rows = [["ID", "Requirement"]] + [[k, v] for k, v in fr]
    story.append(std_table(rows, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.12, 0.88]]))

    story.append(h2("4.2 Non-Functional Requirements", styles))
    nfr = [
        ["NFR-1", "Performance", "API response < 2s on LAN for typical datasets"],
        ["NFR-2", "Usability", "Forms with labels; bilingual labels"],
        ["NFR-3", "Security", "Passwords hashed; JWT on protected routes"],
        ["NFR-4", "Scalability", "User-scoped queries (horizontal scaling possible later)"],
        ["NFR-5", "Maintainability", "Modular route files per domain"],
        ["NFR-6", "Portability", "Browser-based; OS independent"],
    ]
    rows = [["ID", "Category", "Requirement"]] + nfr
    w = [(PAGE_W-2*MARGIN)*x for x in [0.1, 0.2, 0.7]]
    story.append(std_table(rows, col_widths=w))

    story.append(h2("4.3 Feasibility Study", styles))
    feas = [
        ["Technical",   "High — React and Node ecosystems are mature; MongoDB free tier available."],
        ["Economic",    "High for demo — Open-source stack; Netlify/MongoDB Atlas free tiers."],
        ["Operational", "Medium — Requires farmer internet access; minimal training needed."],
    ]
    story.append(std_table([["Area", "Assessment"]] + feas,
                            col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.2, 0.8]]))
    expand_ch4(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN)
    expand_ch4b(story, styles, body, h2, bullet, std_table, PAGE_W, MARGIN, PageBreak)


def ch5_design(story, styles):
    story += chapter_block("Chapter 5 — System Design", styles)
    story.append(h2("5.1 Architectural Pattern", styles))
    story.append(body(
        'The project uses <b>Client-Server architecture</b> with <b>REST API</b> communication. '
        'It aligns with a simplified <b>MERN</b> stack (MongoDB, Express, React, Node) with the '
        'frontend powered by Vite rather than Create React App.', styles))
    story.append(sp(6))

    # Architecture diagram as a styled table
    avail = PAGE_W - 2 * MARGIN
    arch_style = ParagraphStyle("arch", fontName="Helvetica-Bold", fontSize=10,
                                  textColor=WHITE, alignment=TA_CENTER, leading=16)
    arch_sub   = ParagraphStyle("archs", fontName="Helvetica", fontSize=9,
                                  textColor=colors.HexColor("#d0e8da"), alignment=TA_CENTER, leading=14)
    layers = [
        (GREEN_DARK, "PRESENTATION LAYER", "React Components (Pages, Layout, Charts, Forms)"),
        (GREEN_MED,  "APPLICATION LAYER",  "Express Routers + authMiddleware (JWT)"),
        (colors.HexColor("#1a4a2e"),  "DATA LAYER", "MongoDB Collections via Mongoose"),
    ]
    def arch_row(color, title, sub):
        content = Paragraph(f'<b>{title}</b><br/><font size="9">{sub}</font>', arch_style)
        t = Table([[content]], colWidths=[avail*0.7])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0,0),(-1,-1), color),
            ("BOX",           (0,0),(-1,-1), 1, WHITE),
            ("TOPPADDING",    (0,0),(-1,-1), 10),
            ("BOTTOMPADDING", (0,0),(-1,-1), 10),
        ]))
        return t

    outer_rows = []
    for c, ti, su in layers:
        outer_rows.append([arch_row(c, ti, su)])
        if (c, ti, su) != layers[-1]:
            arrow = Paragraph("▼ HTTP/JSON / Mongoose", ParagraphStyle(
                "arr", fontName="Helvetica", fontSize=9, textColor=GREEN_MED, alignment=TA_CENTER))
            outer_rows.append([arrow])
    arch_outer = Table(outer_rows, colWidths=[avail*0.7])
    arch_outer.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),("TOPPADDING",(0,0),(-1,-1),2)]))

    # center it
    centered = Table([[arch_outer]], colWidths=[avail])
    centered.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER")]))
    story.append(centered)
    story.append(sp(14))

    story.append(h2("5.2 Module Decomposition", styles))
    modules = [
        ["Module", "Responsibility"],
        ["Auth",         "Identity lifecycle"],
        ["Users",        "Profile read/update image"],
        ["Animals",      "Herd registry"],
        ["Milk",         "Production diary"],
        ["Vaccinations", "Preventive health schedule"],
        ["Expenses",     "Farm accounting"],
        ["i18n",         "Translation dictionary"],
        ["Layout",       "Shell navigation"],
    ]
    story.append(std_table(modules, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.25, 0.75]]))

    story.append(h2("5.3 Design Decisions", styles))
    decisions = [
        ["Decision", "Rationale", "Trade-off"],
        ["MongoDB documents", "Flexible fields per record type", "No strict SQL joins"],
        ["JWT vs sessions", "Stateless API, SPA-friendly", "Token storage security"],
        ["fetch vs axios", "Simplicity in pages", "Duplicated base URL"],
        ["Delete-only (no PUT)", "Reduced scope", "Cannot edit records in-place"],
        ["Base64 profile images", "No separate file server", "Large documents in DB"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.28, 0.38, 0.34]]
    story.append(std_table(decisions, col_widths=w))
    expand_ch5(story, styles, body, h2, h3, bullet, code_block)
    story.append(PageBreak())


def ch6_tech(story, styles):
    story += chapter_block("Chapter 6 — Technology Stack", styles)

    story.append(h2("6.1 Frontend Technologies", styles))
    fe = [
        ["Technology", "Version", "Role"],
        ["React",            "19.2",  "Component-based UI"],
        ["Vite",             "7.3",   "Dev server, HMR, production bundling"],
        ["React Router",     "7.13",  "Client-side routing"],
        ["Chart.js",         "4.5",   "Chart rendering engine"],
        ["react-chartjs-2",  "5.3",   "React wrapper for Chart.js"],
        ["Recharts",         "3.7",   "Optional/alternate charts"],
        ["Lucide React",     "0.575", "Icons"],
        ["ESLint",           "9.x",   "Static analysis"],
    ]
    story.append(std_table(fe, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.3, 0.15, 0.55]]))

    story.append(h2("6.2 Backend Technologies", styles))
    be = [
        ["Technology", "Version", "Role"],
        ["Node.js",     "LTS",   "JavaScript runtime"],
        ["Express",     "5.2",   "HTTP routing, middleware"],
        ["Mongoose",    "9.2",   "ODM for MongoDB"],
        ["jsonwebtoken","9.0",   "Token issue/verify"],
        ["bcryptjs",    "3.0",   "Password hashing"],
        ["cors",        "2.8",   "Cross-origin headers"],
        ["dotenv",      "17.3",  "Environment configuration"],
    ]
    story.append(std_table(be, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.3, 0.15, 0.55]]))

    story.append(h2("6.3 Deployment Stack", styles))
    dep = [
        ["Component", "Platform", "Configuration"],
        ["Frontend static hosting", "Netlify", "netlify.toml, public/_redirects"],
        ["Backend",                 "Not configured (manual/cloud VM)", "Manual setup"],
        ["Database",                "Local or MongoDB Atlas", "MONGO_URI in .env"],
    ]
    story.append(std_table(dep, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.28, 0.38, 0.34]]))
    expand_ch6(story, styles, body, h2, h3, bullet)
    story.append(PageBreak())


def ch7_backend(story, styles):
    story += chapter_block("Chapter 7 — Implementation: Backend", styles)

    story.append(h2("7.1 Server Bootstrap (server.js)", styles))
    story.append(body('The entry file performs the following steps in sequence:', styles))
    for b in [
        'dotenv.config() — loads environment variables.',
        'Creates Express app instance.',
        'Applies cors() globally.',
        'Parses JSON bodies up to 10 MB (supports base64 profile images).',
        'Connects MongoDB via mongoose.connect(process.env.MONGO_URI).',
        'Mounts six route prefixes.',
        'Defines health route GET /.',
        'Listens on process.env.PORT.',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("7.2 Authentication Routes", styles))
    story.append(h3("POST /api/auth/register", styles))
    story.append(body('Accepts name, email, and password. Password is bcrypt-hashed (cost factor 10) '
                      'before persisting. Returns { message: "User registered" }.', styles))
    story.append(h3("POST /api/auth/login", styles))
    story.append(body('Verifies credentials; issues JWT signed with JWT_SECRET, expiring in 1 day. '
                      'Returns { token, name }.', styles))

    story.append(h2("7.3 Route Summary", styles))
    routes = [
        ["Route", "Method", "Auth", "Description"],
        ["/api/users/profile",     "GET",    "Yes", "Returns name, email, image"],
        ["/api/users/upload",      "PUT",    "Yes", "Updates image field (base64)"],
        ["/api/animals",           "POST",   "Yes", "Create animal"],
        ["/api/animals",           "GET",    "Yes", "List user animals"],
        ["/api/animals/:id",       "DELETE", "Yes", "Remove animal"],
        ["/api/milk",              "POST",   "Yes", "Log milk record"],
        ["/api/milk",              "GET",    "Yes", "List milk records"],
        ["/api/milk/:id",          "DELETE", "Yes", "Remove milk record"],
        ["/api/vaccinations",      "POST",   "Yes", "Record vaccination"],
        ["/api/vaccinations",      "GET",    "Yes", "List vaccinations"],
        ["/api/vaccinations/:id",  "DELETE", "Yes", "Remove vaccination"],
        ["/api/expenses",          "POST",   "Yes", "Record expense/profit"],
        ["/api/expenses",          "GET",    "Yes", "List expenses"],
        ["/api/expenses/:id",      "DELETE", "Yes", "Remove expense"],
        ["/",                      "GET",    "No",  "Health check — plain text"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.33, 0.12, 0.1, 0.45]]
    story.append(std_table(routes, col_widths=w))

    story.append(h2("7.4 Authentication Middleware", styles))
    story.append(body('The protect middleware extracts the Bearer token from the Authorization header, '
                      'verifies it with jwt.verify, sets req.user = decoded payload, and returns 401 '
                      'for missing or invalid tokens. All non-auth routes pass through this middleware.', styles))
    expand_ch7(story, styles, body, h2, h3, bullet, code_block, std_table, PAGE_W, MARGIN)
    expand_ch7b(story, styles, body, h2, h3, bullet, code_block, chapter_block, PageBreak)


def ch8_frontend(story, styles):
    story += chapter_block("Chapter 8 — Implementation: Frontend", styles)

    story.append(h2("8.1 Application Routing (App.jsx)", styles))
    routes = [
        ["Path", "Component", "Auth Required"],
        ["/",                    "Landing",             "No"],
        ["/login",               "Login",               "No"],
        ["/register",            "Register",            "No"],
        ["/forgot-password",     "ForgotPassword",      "No"],
        ["/farmer-dashboard",    "FarmerDashboard",     "Yes"],
        ["/department-dashboard","DepartmentDashboard", "Yes"],
        ["/animals",             "Animal",              "Yes"],
        ["/milk",                "Milk",                "Yes"],
        ["/vaccination",         "Vaccination",         "Yes"],
        ["/expenses",            "Expenses",            "Yes"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.35, 0.35, 0.3]]
    story.append(std_table(routes, col_widths=w))

    story.append(h2("8.2 Layout Shell", styles))
    for b in [
        '<b>Topbar</b> — menu hover, language toggle, dark mode toggle, profile dropdown.',
        '<b>Sidebar</b> — NavLinks; hidden until hover (open state).',
        '<b>Footer</b> — rendered on authenticated pages.',
        '<b>Outlet</b> — child route content.',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("8.3 API Integration Pattern", styles))
    story.append(body('Every protected page constructs requests using the farmer\'s JWT token from '
                      'localStorage. A recommended improvement is a centralized apiClient.js using '
                      'VITE_API_URL for the base path to avoid hardcoded localhost:5000 across all pages.', styles))

    story.append(h2("8.4 Unused / Partial Modules", styles))
    unused = [
        ["File", "Status"],
        ["services/api.js",          "Axios stub pointing to api.example.com — not used"],
        ["services/storage.js",      "localStorage CRUD — superseded by API"],
        ["context/LanguageContext",  "Partially redundant with App-level state management"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.35, 0.65]]
    story.append(std_table(unused, col_widths=w))
    expand_ch8(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN)
    story.append(PageBreak())


def ch9_database(story, styles):
    story += chapter_block("Chapter 9 — Database Design", styles)

    story.append(h2("9.1 Entity Relationships", styles))
    story.append(body('A User document has a one-to-many relationship with Animals, Milk records, '
                      'Vaccinations, and Expenses. Each child document stores a user field '
                      '(MongoDB ObjectId) referencing User._id to enforce per-user data isolation.', styles))

    story.append(h2("9.2 Collections Overview", styles))

    # user
    story.append(h3("User Collection", styles))
    rows = [["Field","Type","Description"],
            ["_id",      "ObjectId", "Primary key"],
            ["name",     "String",   "Display name"],
            ["email",    "String",   "Login identifier"],
            ["password", "String",   "bcrypt hash"],
            ["image",    "String",   "Optional base64/data URL"]]
    story.append(std_table(rows, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.2,0.2,0.6]]))

    # animal
    story.append(h3("Animal Collection", styles))
    rows = [["Field","Type","Required","Notes"],
            ["user",      "ObjectId","Yes","Owner reference"],
            ["animalId",  "String",  "Yes","Farmer-defined tag e.g. A1"],
            ["breed",     "String",  "Yes","Dropdown values"],
            ["age",       "String",  "No", "Stored as string from form"],
            ["gender",    "String",  "No", "Male/Female/Other"],
            ["cost",      "String",  "No", "Purchase cost"],
            ["health",    "String",  "No", "e.g. Healthy, Sick"],
            ["createdAt", "Date",    "Auto","Timestamps"]]
    story.append(std_table(rows, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.2,0.15,0.15,0.5]]))

    # vaccination
    story.append(h3("Vaccination Collection", styles))
    rows = [["Field","Type","Description"],
            ["user",         "ObjectId","Owner"],
            ["animalId",     "String",  "Target animal"],
            ["breed",        "String",  "Breed at time of vaccination"],
            ["vaccineName",  "String",  "FMD, HS, BQ, etc."],
            ["date",         "String",  "Administration date"],
            ["upcomingDate", "String",  "Next due or 'No Booster' text"]]
    story.append(std_table(rows, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.22,0.2,0.58]]))

    story.append(h2("9.3 Indexing Recommendations (Future)", styles))
    for b in [
        'Unique compound index on (user, animalId) to prevent duplicate animal IDs per farmer.',
        'Descending index on (user, date) for milk records to speed date-range queries.',
    ]:
        story.append(bullet(b, styles))
    expand_ch9(story, styles, body, h2, h3, std_table, PAGE_W, MARGIN)
    story.append(PageBreak())


def ch10_security(story, styles):
    story += chapter_block("Chapter 10 — Security & Authentication", styles)

    story.append(h2("10.1 Threat Model", styles))
    threats = [
        ["Threat", "Mitigation (Current)", "Gap"],
        ["Password theft from DB", "bcrypt hashing", "Weak user passwords still possible"],
        ["XSS stealing JWT",       "None specific",  "localStorage vulnerable"],
        ["IDOR (cross-user data)", "user filter on queries", "Good mitigation"],
        ["Brute force login",      "None",           "Add rate limiting"],
        ["Secret leakage",         ".env for JWT",   "Must not commit secrets"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.3, 0.35, 0.35]]
    story.append(std_table(threats, col_widths=w))

    story.append(h2("10.2 Password Hashing", styles))
    story.append(body('Algorithm: <b>bcrypt</b> with cost factor <b>10</b>. '
                      'The hash is stored in the User document; compare is done on login via '
                      'bcrypt.compare(password, user.password).', styles))

    story.append(h2("10.3 JWT Lifecycle", styles))
    for n, b in enumerate([
        'Issued at login with payload { id: user._id }.',
        'Client stores in localStorage key "token".',
        'Sent as Authorization: Bearer <token> on protected routes.',
        'Server verifies with process.env.JWT_SECRET.',
        'Expires after 1 day — client does not auto-refresh.',
    ], 1):
        story.append(bullet(f"<b>{n}.</b> {b}", styles))

    story.append(h2("10.4 Security Checklist for Production", styles))
    checks = [
        "HTTPS everywhere",
        "Restrict CORS to frontend origin",
        "HttpOnly cookie option instead of localStorage",
        "Input validation (Joi/Zod)",
        "Rate limit /api/auth/login",
        "Rotate JWT secrets",
        "Add .env to .gitignore on backend",
        "Helmet.js for HTTP headers",
    ]
    for c in checks:
        story.append(bullet(f"[ ] {c}", styles))
    expand_ch10(story, styles, body, h2, bullet)
    story.append(PageBreak())


def ch11_ui(story, styles):
    story += chapter_block("Chapter 11 — User Interface & Screen Documentation", styles)

    story.append(h2("11.1 Landing Page (/)", styles))
    sections = ["Hero — Title, tagline, Get Started, Watch Demo",
                "Stats — Marketing numbers (farms, milk tracked, farmers)",
                "Features Grid — 6 cards: Animal Registration, Vaccine Tracking, Milk Production, etc.",
                "Benefits — Save time, increase milk, control expenses, mobile access",
                "How It Works — 3 steps",
                "Testimonial — Star rating and quote",
                "FAQ — Two question/answer pairs",
                "Footer — Links and copyright text"]
    for s in sections:
        story.append(bullet(s, styles))

    story.append(h2("11.2 Farmer Dashboard (/farmer-dashboard)", styles))
    story.append(h3("KPI Cards", styles))
    kpis = [
        ["Card", "Computation"],
        ["Total Animals",    "animals.length"],
        ["Today Milk",       "Sum quantities where date === today"],
        ["Revenue Today",    "todayMilk * 70"],
        ["Total Milk",       "Sum all quantities"],
        ["Top Animal",       "Max milk by animalId"],
        ["Farm Score",       "(totalMilk * 0.5) + (totalAnimals * 2) + (revenueToday * 0.1)"],
    ]
    story.append(std_table(kpis, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.35, 0.65]]))

    story.append(h2("11.3 Animal Management (/animals)", styles))
    fields = [
        ["Field", "Control"],
        ["Animal ID", "Text input"],
        ["Breed",     "Select: Gir, Sahiwal, Red Sindhi, Tharparkar, HF Cross, Jersey, Murrah Buffalo, etc."],
        ["Age",       "Number input"],
        ["Gender",    "Select: Male, Female, Other"],
        ["Cost",      "Number input (displayed with Rs. symbol)"],
        ["Health",    "Text input"],
    ]
    story.append(std_table(fields, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.2, 0.8]]))

    story.append(h2("11.4 Vaccination Schedule (/vaccination)", styles))
    vacc = [
        ["Vaccine", "Booster Interval"],
        ["FMD",         "6 months"],
        ["HS",          "12 months"],
        ["BQ",          "12 months"],
        ["Brucellosis", "No booster"],
        ["Theileriosis","No booster"],
        ["Anthrax",     "12 months"],
    ]
    story.append(std_table(vacc, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.4, 0.6]]))

    story.append(h2("11.5 Expenses & Profit (/expenses)", styles))
    story.append(body('Expense categories: Feed, Veterinary, Labor, Equipment, Maintenance, '
                      'Breeding, Animal Purchase. Profit categories: Milk Sale, Dairy Products, '
                      'Animal Sale, Manure Sale, Government Subsidy. Summary row shows totals '
                      'and net profit/loss in green or red.', styles))
    expand_ch11(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN, PageBreak)
    expand_ch11b(story, styles, body, h2, h3, bullet, PageBreak)
    expand_ch11c(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN)
    story.append(PageBreak())


def ch12_algorithms(story, styles):
    story += chapter_block("Chapter 12 — Algorithms & Business Logic", styles)

    story.append(h2("12.1 Today's Milk Calculation", styles))
    story.append(code_block([
        "const today = new Date().toISOString().split('T')[0];",
        "const todayMilk = milkRecords",
        "  .filter(m => m.date === today)",
        "  .reduce((sum, m) => sum + Number(m.quantity), 0);",
    ], styles))
    story.append(sp(8))

    story.append(h2("12.2 Revenue Estimation", styles))
    story.append(code_block([
        "const milkPrice = 70; // INR per litre (hardcoded)",
        "const revenueToday = todayMilk * milkPrice;",
    ], styles))
    story.append(sp(8))

    story.append(h2("12.3 Farm Performance Score", styles))
    story.append(code_block([
        "const performanceScore =",
        "  (totalMilk    * 0.5) +",
        "  (totalAnimals * 2)   +",
        "  (revenueToday * 0.1);",
    ], styles))
    story.append(body('Heuristic scoring for gamification-style display — not an industry standard metric.', styles))

    story.append(h2("12.4 Weekly Milk Aggregation for Chart", styles))
    story.append(code_block([
        'const days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];',
        "const weeklyData = new Array(7).fill(0);",
        "milkRecords.forEach(r => {",
        "  const d = new Date(r.date).getDay(); // 0=Sun",
        "  const index = d === 0 ? 6 : d - 1;  // Mon=0",
        "  weeklyData[index] += Number(r.quantity);",
        "});",
    ], styles))

    story.append(h2("12.5 Vaccination Booster Date", styles))
    story.append(code_block([
        "if (months > 0) {",
        "  const nextDate = new Date(selectedDate);",
        "  nextDate.setMonth(nextDate.getMonth() + months);",
        '  upcomingDate = nextDate.toISOString().split("T")[0];',
        "} else {",
        '  upcomingDate = "No Booster";',
        "}",
    ], styles))

    story.append(h2("12.6 Vaccine Due Reminder", styles))
    story.append(code_block([
        "const diff = (new Date(v.upcomingDate) - new Date())",
        "             / (1000 * 60 * 60 * 24);",
        "return diff <= 3; // flag if due within 3 days",
    ], styles))

    story.append(h2("12.7 Net Farm Profit/Loss", styles))
    story.append(code_block([
        'const totalExpenses = records.filter(r => r.type === "Expense")',
        '  .reduce((sum, r) => sum + Number(r.amount), 0);',
        'const totalProfit = records.filter(r => r.type === "Profit")',
        '  .reduce((sum, r) => sum + Number(r.amount), 0);',
        'const netProfitLoss = totalProfit - totalExpenses;',
    ], styles))
    expand_ch12(story, styles, body, h2, bullet)
    story.append(PageBreak())


def ch13_api(story, styles):
    story += chapter_block("Chapter 13 — API Reference", styles)
    story.append(body('Base URL (development): http://localhost:5000', styles))
    story.append(body('Auth header (protected routes): Authorization: Bearer &lt;token&gt;', styles))

    api_rows = [
        ["Method", "Endpoint", "Auth", "Description"],
        ["POST",   "/api/auth/register",    "No",  "Register user; body: { name, email, password }"],
        ["POST",   "/api/auth/login",       "No",  "Login; returns { token, name }"],
        ["GET",    "/api/users/profile",    "Yes", "Returns { name, email, image }"],
        ["PUT",    "/api/users/upload",     "Yes", "Update profile image (base64)"],
        ["POST",   "/api/animals",          "Yes", "Create animal"],
        ["GET",    "/api/animals",          "Yes", "List user's animals"],
        ["GET",    "/api/animals/:id",      "Yes", "Single animal"],
        ["DELETE", "/api/animals/:id",      "Yes", "Delete animal"],
        ["POST",   "/api/milk",             "Yes", "Log milk record"],
        ["GET",    "/api/milk",             "Yes", "List milk records"],
        ["DELETE", "/api/milk/:id",         "Yes", "Delete milk record"],
        ["POST",   "/api/vaccinations",     "Yes", "Record vaccination"],
        ["GET",    "/api/vaccinations",     "Yes", "List vaccinations"],
        ["DELETE", "/api/vaccinations/:id", "Yes", "Delete vaccination"],
        ["POST",   "/api/expenses",         "Yes", "Record expense/profit"],
        ["GET",    "/api/expenses",         "Yes", "List expenses"],
        ["DELETE", "/api/expenses/:id",     "Yes", "Delete expense"],
        ["GET",    "/",                     "No",  "Health check — 'Backend running'"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.1, 0.3, 0.08, 0.52]]
    story.append(std_table(api_rows, col_widths=w))

    story.append(h2("HTTP Status Codes Used", styles))
    status = [
        ["Code","Usage"],
        ["200","Success"],
        ["201","Animal created"],
        ["400","Login credential errors"],
        ["401","Missing/invalid JWT"],
        ["500","Server/database errors"],
    ]
    story.append(std_table(status, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.15, 0.85]]))
    expand_ch13(story, styles, body, h2, code_block)
    story.append(PageBreak())


def ch14_testing(story, styles):
    story += chapter_block("Chapter 14 — Testing & Validation", styles)

    story.append(h2("14.1 Testing Strategy", styles))
    story.append(body(
        'Formal automated tests are not implemented (npm test exits with error on backend). '
        'Validation was performed through manual test cases during development.', styles))

    story.append(h2("14.2 Test Cases", styles))
    test_cases = [
        ["TC", "Description", "Steps", "Expected Result"],
        ["TC-01", "User Registration",
         "Open /register; enter valid Gmail + password; submit",
         "New document in users collection with hashed password"],
        ["TC-02", "Login",
         "POST correct credentials / wrong password",
         "JWT returned / Error message shown"],
        ["TC-03", "Animal CRUD",
         "Add, refresh, delete, switch user",
         "Persists; other user cannot see data"],
        ["TC-04", "Milk Records",
         "Add 10L for today; check dashboard",
         "Income = Rs.700; dashboard KPI updates"],
        ["TC-05", "Vaccination Booster",
         "Add FMD; check next due date",
         "Date ~6 months after administration"],
        ["TC-06", "Expenses",
         "Add expense Rs.1000; add profit Rs.5000",
         "Net = Rs.4000 displayed"],
        ["TC-07", "Profile Image",
         "Upload image <2MB; reload",
         "Preview and API return same image"],
        ["TC-08", "Language Toggle",
         "Switch EN to HI; reload",
         "Sidebar in Hindi; preference persisted"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.1, 0.2, 0.35, 0.35]]
    story.append(std_table(test_cases, col_widths=w))

    story.append(h2("14.3 Negative Testing", styles))
    neg = [
        ["Case", "Expected"],
        ["API call without token",     "401 Unauthorized"],
        ["Malformed JSON body",        "500 or parser error"],
        ["Duplicate registration email","500 / error message"],
    ]
    story.append(std_table(neg, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.45, 0.55]]))
    expand_ch14(story, styles, body, h2, bullet, std_table, PAGE_W, MARGIN)
    story.append(PageBreak())


def ch15_deployment(story, styles):
    story += chapter_block("Chapter 15 — Deployment & DevOps", styles)

    story.append(h2("15.1 Backend Deployment Steps", styles))
    for n, b in enumerate([
        'Provision VM or PaaS (Railway, Render, AWS EC2).',
        'Set environment variables: MONGO_URI, JWT_SECRET, PORT.',
        'Run npm install --production and npm start.',
        'Configure firewall to expose port.',
        'Optionally use PM2 for process management.',
    ], 1):
        story.append(bullet(f"<b>{n}.</b> {b}", styles))

    story.append(h2("15.2 Frontend Deployment (Netlify)", styles))
    story.append(code_block([
        "[build]",
        '  command = "npm run build"',
        '  publish = "dist"',
        "",
        "[[redirects]]",
        '  from = "/*"',
        '  to   = "/index.html"',
        "  status = 200",
    ], styles))

    story.append(h2("15.3 Environment Variables", styles))
    story.append(h3("Backend .env", styles))
    story.append(code_block([
        "MONGO_URI=mongodb+srv://<user>:<pass>@cluster.mongodb.net/cattlecloud",
        "JWT_SECRET=<long-random-string>",
        "PORT=5000",
    ], styles))
    story.append(h3("Frontend .env", styles))
    story.append(code_block(["VITE_API_URL=https://your-backend.example.com"], styles))
    expand_ch15(story, styles, body, h2, bullet)
    story.append(PageBreak())


def ch16_results(story, styles):
    story += chapter_block("Chapter 16 — Results & Discussion", styles)

    story.append(h2("16.1 Achieved Outcomes", styles))
    for b in [
        'Persistent cloud storage of farm records.',
        'Visual dashboard for milk analytics with Chart.js bar chart.',
        'Vaccination scheduling with due-soon warnings.',
        'Bilingual interface (English/Hindi) suitable for Indian farmers.',
        'Secure password storage and JWT-protected APIs with per-user data boundaries.',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("16.2 Demonstration Script (Viva)", styles))
    demo = [
        ["Step", "Action", "Duration"],
        ["1", "Show landing page and language toggle",               "1 min"],
        ["2", "Register new farmer account",                         "1 min"],
        ["3", "Login and show dashboard",                            "1 min"],
        ["4", "Add 2 animals with different breeds",                 "2 min"],
        ["5", "Add milk records; refresh dashboard — KPI change",    "2 min"],
        ["6", "Add vaccination; show next due date and alert banner","1 min"],
        ["7", "Add expense and profit; show net summary",            "1 min"],
        ["8", "Profile image upload",                                "1 min"],
        ["9", "Mention department dashboard as future work",         "30 sec"],
    ]
    w = [(PAGE_W-2*MARGIN)*x for x in [0.08, 0.72, 0.2]]
    story.append(std_table(demo, col_widths=w))

    story.append(h2("16.3 Learning Outcomes", styles))
    for b in [
        'REST API design and HTTP verbs.',
        'MongoDB schema design and references.',
        'React hooks and conditional rendering.',
        'Authentication flows in SPAs.',
        'CORS and environment configuration.',
        'Static site deployment.',
    ]:
        story.append(bullet(b, styles))
    expand_ch16(story, styles, body, h2, bullet)
    story.append(PageBreak())


def ch17_limitations(story, styles):
    story += chapter_block("Chapter 17 — Limitations & Known Issues", styles)

    story.append(h2("17.1 Functional Limitations", styles))
    lims = [
        ["#", "Limitation", "Severity"],
        ["L1", "Forgot password not connected to MongoDB", "High"],
        ["L2", "Dashboard ignores vaccination API",        "Medium"],
        ["L3", "No edit (update) endpoints",               "Medium"],
        ["L4", "Department dashboard is static",           "Medium"],
        ["L5", "Phone number collected but not stored",    "Low"],
        ["L6", "Gmail-only registration rule",             "Low"],
    ]
    story.append(std_table(lims, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.08, 0.72, 0.2]]))

    story.append(h2("17.2 Technical Bugs / Risks", styles))
    bugs = [
        ["#",  "Issue", "File"],
        ["B1", "Orphan LanguageProvider JSX",          "main.jsx"],
        ["B2", "Layout import wrong case",             "App.jsx"],
        ["B3", "Hardcoded API URL",                    "All pages"],
        ["B4", "token not cleared on logout",          "Topbar.jsx, Layout.jsx"],
        ["B5", "Unused authcontroller.js with weak secret", "backend/controllers/"],
        ["B6", "PrivateRoute ignores token validity",  "PrivateRoute.jsx"],
    ]
    story.append(std_table(bugs, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.08, 0.62, 0.3]]))
    expand_ch17(story, styles, body, h2, bullet)
    story.append(PageBreak())


def ch18_future(story, styles):
    story += chapter_block("Chapter 18 — Future Scope", styles)

    story.append(h2("18.1 Short-Term Enhancements (1–2 months)", styles))
    for b in [
        'Fix main.jsx and Layout import casing.',
        'Introduce VITE_API_URL across all fetch calls.',
        'Connect dashboard to /api/vaccinations.',
        'Implement server-side password reset (email OTP).',
        'Clear all auth keys on logout; redirect on 401 globally.',
        'Add unique compound index on (user, animalId).',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("18.2 Medium-Term Features (3–6 months)", styles))
    for b in [
        'Role-based access — farmer vs department with aggregated read APIs.',
        'Edit records — PUT/PATCH for animals, milk, etc.',
        'PDF/Excel export of milk and expense reports.',
        'SMS reminders for vaccines (Twilio / MSG91).',
        'PWA — service worker for limited offline entry.',
        'Mobile responsive audit — improve sidebar UX on phones.',
    ]:
        story.append(bullet(b, styles))

    story.append(h2("18.3 Long-Term Vision (6+ months)", styles))
    for b in [
        'IoT integration — automatic milk meter readings.',
        'GIS mapping — farm location and veterinary routing.',
        'Marketplace module — connect farmers to buyers.',
        'AI yield prediction from historical milk data.',
        'Integration with government livestock ID schemes.',
        'Microservices split if user base scales significantly.',
    ]:
        story.append(bullet(b, styles))
    expand_ch18(story, styles, body, h2, bullet)
    story.append(PageBreak())


def ch19_conclusion(story, styles):
    story += chapter_block("Chapter 19 — Conclusion", styles)
    story.append(sp(10))
    story.append(body(
        'CattleCloud demonstrates a complete <b>concept-to-implementation</b> pipeline for a '
        'livestock management web application. By combining a React frontend, Express backend, and '
        'MongoDB persistence, the project meets core academic objectives: requirements analysis, '
        'system design, modular implementation, and user-centered features for dairy farmers.',
        styles))
    story.append(body(
        "The system's strongest engineering aspects are <b>consistent user-scoped APIs</b>, a "
        "<b>coherent domain model</b> (animals &rarr; milk &rarr; health &rarr; finance), and "
        "<b>bilingual usability</b>. Areas requiring further work — production configuration, "
        "password recovery, department analytics, and automated testing — provide a clear roadmap "
        "beyond the minor project submission.",
        styles))
    story.append(body(
        'With the enhancements outlined in Chapter 18, CattleCloud could evolve from an academic '
        'MVP into a deployable rural SaaS product contributing to smarter, data-driven livestock '
        'farming.',
        styles))
    expand_ch19(story, styles, body, h2, bullet)
    story.append(PageBreak())


def appendices(story, styles):
    story += chapter_block("Appendix A — Project Directory Structure", styles)
    story.append(sp(8))
    story.append(code_block([
        "minorproject/",
        "├── PROJECT_REPORT.md",
        "├── backend/",
        "│   ├── server.js",
        "│   ├── package.json",
        "│   ├── .env                   (local secrets — do not publish)",
        "│   ├── controllers/",
        "│   │   └── authcontroller.js  (unused)",
        "│   ├── middleware/",
        "│   │   └── authMiddleware.js",
        "│   ├── models/",
        "│   │   ├── User.js",
        "│   │   ├── Animal.js",
        "│   │   ├── Milk.js",
        "│   │   ├── Vaccination.js",
        "│   │   └── Expense.js",
        "│   └── routes/",
        "│       ├── authRoutes.js",
        "│       ├── animalRoutes.js",
        "│       ├── milkRoutes.js",
        "│       ├── vaccinationRoutes.js",
        "│       └── expenseRoutes.js",
        "├── smart-livestock-dashboard/",
        "│   ├── index.html",
        "│   ├── vite.config.js",
        "│   ├── netlify.toml",
        "│   └── src/",
        "│       ├── main.jsx",
        "│       ├── App.jsx",
        "│       ├── components/",
        "│       ├── context/",
        "│       ├── pages/",
        "│       ├── services/",
        "│       └── utils/translations.js",
        "└── data/",
        "    ├── Animals.json",
        "    ├── Milk.json",
        "    ├── vaccination.json",
        "    └── expenses.json",
    ], styles))
    story.append(PageBreak())

    story += chapter_block("Appendix B — Glossary", styles)
    glossary = [
        ["Term", "Definition"],
        ["API",      "Application Programming Interface; HTTP endpoints for data exchange"],
        ["bcrypt",   "Password hashing function resistant to brute force"],
        ["CORS",     "Cross-Origin Resource Sharing; browser security for APIs"],
        ["CRUD",     "Create, Read, Update, Delete operations"],
        ["FMD",      "Foot and Mouth Disease — common cattle vaccination"],
        ["JWT",      "JSON Web Token — signed credential for stateless auth"],
        ["KPI",      "Key Performance Indicator — dashboard metric"],
        ["Mongoose", "MongoDB object modeling library for Node.js"],
        ["ODM",      "Object Document Mapper"],
        ["REST",     "Representational State Transfer — HTTP-based API style"],
        ["SPA",      "Single Page Application — client-side routed web app"],
        ["Vite",     "Frontend build tool and development server"],
    ]
    story.append(std_table(glossary, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.2, 0.8]]))
    story.append(PageBreak())

    story += chapter_block("Appendix C — References", styles)
    refs = [
        ("1",  "React Documentation",              "https://react.dev"),
        ("2",  "Express.js Guide",                 "https://expressjs.com"),
        ("3",  "Mongoose Documentation",           "https://mongoosejs.com"),
        ("4",  "MongoDB Manual",                   "https://www.mongodb.com/docs"),
        ("5",  "JSON Web Tokens Introduction",     "https://jwt.io/introduction"),
        ("6",  "Chart.js Documentation",           "https://www.chartjs.org/docs"),
        ("7",  "Vite Guide",                       "https://vite.dev"),
        ("8",  "Netlify SPA Redirects",            "https://docs.netlify.com/routing/redirects/"),
        ("9",  "OWASP Authentication Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"),
        ("10", "MDN Fetch API",                    "https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API"),
    ]
    for n, title, url in refs:
        story.append(body(f"<b>[{n}]</b> {title} — <i>{url}</i>", styles))
    story.append(PageBreak())

    story += chapter_block("Appendix D — Viva Preparation Question Bank", styles)
    story.append(h2("Basic", styles))
    qa = [
        ("Q1", "What is CattleCloud?",
         "A web-based livestock management system for recording animals, milk, vaccinations, and expenses."),
        ("Q2", "Which database did you use and why?",
         "MongoDB — flexible schema for varied farm records, easy integration with Node via Mongoose."),
        ("Q3", "How does login work?",
         "Server verifies bcrypt hash, returns JWT; client stores token and sends Bearer header on API calls."),
    ]
    for q, question, answer in qa:
        story.append(body(f"<b>{q}. {question}</b>", styles))
        story.append(body(f"A: {answer}", styles))
        story.append(sp(4))

    story.append(h2("Intermediate", styles))
    qa2 = [
        ("Q4", "How do you prevent Farmer A from seeing Farmer B's animals?",
         "Every query includes { user: req.user.id } from decoded JWT."),
        ("Q5", "Explain the vaccination booster logic.",
         "A rules map defines months per vaccine; frontend adds months to administration date for upcomingDate."),
        ("Q6", "What is the farm score formula?",
         "(totalMilk * 0.5) + (totalAnimals * 2) + (revenueToday * 0.1) — heuristic display metric."),
    ]
    for q, question, answer in qa2:
        story.append(body(f"<b>{q}. {question}</b>", styles))
        story.append(body(f"A: {answer}", styles))
        story.append(sp(4))

    story.append(h2("Advanced", styles))
    qa3 = [
        ("Q7", "What are JWT drawbacks in localStorage?",
         "Vulnerable to XSS; httpOnly cookies are a safer alternative."),
        ("Q8", "How would you deploy frontend and backend together?",
         "Host API on HTTPS subdomain; set VITE_API_URL; build React to static hosting; configure CORS."),
        ("Q9", "Why is forgot password not production-ready?",
         "It updates localStorage users, not MongoDB; no email verification."),
        ("Q10","How would you add an edit animal feature?",
         "Implement PUT /api/animals/:id with findOneAndUpdate filtered by user, add Edit button in UI."),
    ]
    for q, question, answer in qa3:
        story.append(body(f"<b>{q}. {question}</b>", styles))
        story.append(body(f"A: {answer}", styles))
        story.append(sp(4))

    story.append(PageBreak())

    story += chapter_block("Appendix F — Team Contribution Template", styles)
    contrib = [
        ["Member", "Roll No.", "Modules Contributed"],
        ["Student A", "", "Frontend: Landing, Login, Dashboard"],
        ["Student B", "", "Frontend: Animal, Milk pages"],
        ["Student C", "", "Backend: Auth, Animal APIs"],
        ["Student D", "", "Backend: Milk, Vaccination, Expenses APIs"],
        ["Student E", "", "Documentation, Testing, Deployment"],
    ]
    story.append(std_table(contrib, col_widths=[(PAGE_W-2*MARGIN)*x for x in [0.25, 0.2, 0.55]]))
    story.append(sp(14))
    story.append(body("<i>(Fill before submission)</i>", styles))
    expand_appendices(
        story, styles, body, h2, h3, bullet, std_table, code_block,
        PAGE_W, MARGIN, chapter_block, sp, PageBreak,
    )
    expand_viva_extra(story, styles, body, h2, bullet, chapter_block, PageBreak)


# ─────────────────────── Page Templates ───────────────────────
def on_page(canvas, doc):
    """Header/footer on every page except cover (page 1)."""
    if doc.page == 1:
        return
    canvas.saveState()
    w, h = A4

    # Header line
    canvas.setStrokeColor(GREEN_DARK)
    canvas.setLineWidth(1.5)
    canvas.line(MARGIN, h - MARGIN + 6, w - MARGIN, h - MARGIN + 6)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(GREEN_DARK)
    canvas.drawString(MARGIN, h - MARGIN + 9, "CattleCloud — Smart Livestock Management System")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY_MID)
    canvas.drawRightString(w - MARGIN, h - MARGIN + 9, "Minor Project Report  |  2025–2026")

    # Footer line
    canvas.setStrokeColor(GREEN_LIGHT)
    canvas.setLineWidth(0.8)
    canvas.line(MARGIN, MARGIN - 6, w - MARGIN, MARGIN - 6)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY_MID)
    canvas.drawCentredString(w / 2, MARGIN - 16, f"Page {doc.page}")

    canvas.restoreState()


# ─────────────────────── Main ─────────────────────────────────
def main():
    from pathlib import Path
    out = str(Path(__file__).resolve().parent / "CattleCloud_Project_Report.pdf")
    doc = SimpleDocTemplate(
        out, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN + 0.3*cm, bottomMargin=MARGIN + 0.3*cm,
        title="CattleCloud — Smart Livestock Management System",
        author="Project Team",
    )

    styles = build_styles()
    story = []

    cover_page(story, styles)
    certificate_page(story, styles)
    declaration_page(story, styles)
    acknowledgement_page(story, styles)
    abstract_page(story, styles)
    toc_page(story, styles)
    ch1_intro(story, styles)
    ch2_literature(story, styles)
    ch3_problem(story, styles)
    ch4_analysis(story, styles)
    ch5_design(story, styles)
    ch6_tech(story, styles)
    ch7_backend(story, styles)
    ch8_frontend(story, styles)
    ch9_database(story, styles)
    ch10_security(story, styles)
    ch11_ui(story, styles)
    ch12_algorithms(story, styles)
    ch13_api(story, styles)
    ch14_testing(story, styles)
    ch15_deployment(story, styles)
    ch16_results(story, styles)
    ch17_limitations(story, styles)
    ch18_future(story, styles)
    ch19_conclusion(story, styles)
    appendices(story, styles)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF written -> {out}")


if __name__ == "__main__":
    main()
