from fpdf import FPDF, XPos, YPos
import os

OUTPUT = os.path.join(os.path.expanduser("~"), "Desktop", "MHCB_Site_Structure_2026.pdf")

# Colors
DARK   = (15, 23, 42)
BLUE   = (59, 130, 246)
TEAL   = (20, 184, 166)
PURPLE = (168, 85, 247)
AMBER  = (245, 158, 11)
GREEN  = (34, 197, 94)
SLATE  = (71, 85, 105)
LIGHT  = (248, 250, 252)
GRAY   = (30, 41, 59)

class PDF(FPDF):
    def header(self):
        self.set_fill_color(*DARK)
        self.rect(0, 0, 210, 22, 'F')
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*LIGHT)
        self.set_xy(10, 6)
        self.cell(0, 10, "MHCB - Site Architecture 2026", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(100, 120, 150)
        self.set_xy(10, 13)
        self.cell(0, 6, "myhealthcarebroker.com . Private Health Insurance Germany")
        self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*SLATE)
        self.cell(0, 10, f"Page {self.page_no()} | MHCB Site Structure | April 2026", align="C")
        self.set_text_color(0, 0, 0)

    def section_bar(self, text, color, icon=""):
        self.set_fill_color(*color)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*LIGHT)
        self.cell(0, 10, f"  {icon}  {text}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def sub_header(self, text, color):
        r, g, b = color
        self.set_fill_color(min(240,r//8+185), min(240,g//8+185), min(240,b//8+185))
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*SLATE)
        self.set_x(20)
        self.cell(170, 7, f"  {text}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(0.5)

    def page_row(self, url, vol="", tier=2, indent=20, accent=None):
        if accent:
            self.set_fill_color(*accent)
        else:
            self.set_fill_color(248, 250, 252)

        self.set_x(indent)
        w = 210 - indent - 10

        # URL
        self.set_font("Courier", "B", 8)
        self.set_text_color(30, 60, 120)
        url_w = w - 35
        self.cell(url_w, 7, url, fill=True)

        # Volume
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*SLATE)
        self.cell(35, 7, vol, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(0.5)

    def hub_row(self, url, vol, color):
        self.set_fill_color(*color)
        self.set_x(10)
        self.set_font("Courier", "B", 9)
        self.set_text_color(*LIGHT)
        self.cell(155, 9, f"  {url}", fill=True)
        self.set_font("Helvetica", "B", 8)
        self.cell(35, 9, vol, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def connector(self, text=""):
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*SLATE)
        self.set_x(10)
        self.cell(0, 5, f"    {text}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)

    def spacer(self, h=4):
        self.ln(h)

    def nav_preview(self):
        self.set_fill_color(*GRAY)
        self.rect(10, self.get_y(), 190, 12, 'F')
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*LIGHT)
        items = ["MHCB", "Insurance v", "Compare v", "Tools v", "Guides v", "Get Advice ->"]
        x_pos = [12, 45, 80, 115, 145, 175]
        y = self.get_y() + 3
        for item, x in zip(items, x_pos):
            self.set_xy(x, y)
            if item == "Get Advice ->":
                self.set_fill_color(*GREEN)
                self.cell(22, 6, item, fill=True, align="C")
            elif item == "MHCB":
                self.set_font("Helvetica", "B", 9)
                self.cell(20, 6, item)
                self.set_font("Helvetica", "B", 8)
            else:
                self.cell(30, 6, item)
        self.set_text_color(0, 0, 0)
        self.set_xy(10, y + 12)
        self.ln(2)


pdf = PDF()
pdf.set_margins(10, 28, 10)
pdf.set_auto_page_break(auto=True, margin=16)
pdf.add_page()

# ?? NAV PREVIEW
pdf.set_font("Helvetica", "B", 8)
pdf.set_text_color(*SLATE)
pdf.cell(0, 5, "NAVIGATION (was der Nutzer im Header sieht)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)
pdf.nav_preview()
pdf.ln(6)

# ?? HOMEPAGE
pdf.set_fill_color(*BLUE)
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(*LIGHT)
pdf.cell(0, 14, "   /   HOMEPAGE - myhealthcarebroker.com", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
pdf.set_font("Helvetica", "", 8)
pdf.set_fill_color(240, 245, 255)
pdf.set_text_color(*SLATE)
pdf.cell(0, 6, "   Hero + 3 Kategorien + Top Insurers + Reviews + CTA",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.ln(6)

# ?? FUNNEL
pdf.set_font("Helvetica", "B", 8)
pdf.set_text_color(*SLATE)
pdf.cell(0, 5, "USER FUNNEL:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)

steps = [
    ("Google Search", SLATE),
    ("Pillar Page", BLUE),
    ("Compare/Guide", GRAY),
    ("Insurer Review", GRAY),
    ("Get Advice", GREEN),
]
step_w = 36
x = 10
y = pdf.get_y()
for i, (label, color) in enumerate(steps):
    pdf.set_fill_color(*color)
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(*LIGHT)
    pdf.set_xy(x, y)
    pdf.cell(step_w, 8, label, align="C", fill=True)
    x += step_w
    if i < len(steps) - 1:
        pdf.set_xy(x, y)
        pdf.set_text_color(*SLATE)
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(4, 8, "->", align="C")
        x += 4

pdf.set_xy(10, y + 10)
pdf.set_text_color(0, 0, 0)
pdf.ln(6)

# ??????????????????????????????????????????????
# TIER 1
# ??????????????????????????????????????????????
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(*SLATE)
pdf.cell(0, 5, "?????????????????  TIER 1 . Haupt-Pillar-Pages (im Nav-Dropdown)  ?????????????????", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(3)

# Private
pdf.section_bar("PRIVATE INSURANCE", BLUE, "1.")
pdf.hub_row("/private-health-insurance-germany", "~2.500/mo", BLUE)

pdf.spacer(2)

# Public
pdf.section_bar("PUBLIC INSURANCE", TEAL, "2.")
pdf.hub_row("/public-health-insurance-germany", "~1.500/mo", TEAL)

pdf.spacer(2)

# Expat
pdf.section_bar("EXPAT INSURANCE  (GROESSTE LUECKE - Feather rankt #1)", PURPLE, "3.")
pdf.hub_row("/health-insurance-expats-germany", "~4.200/mo !!!!", PURPLE)

pdf.ln(6)

# ??????????????????????????????????????????????
# TIER 2 - PRIVATE
# ??????????????????????????????????????????????
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(*SLATE)
pdf.cell(0, 5, "?????????????????  TIER 2 . Sub-Pages Private Insurance  ?????????????????", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

pdf.sub_header("KOSTEN", BLUE)
pdf.page_row("/best-private-health-insurance-germany", "~2.100/mo")
pdf.page_row("/cheapest-private-health-insurance-germany", "~700/mo")
pdf.page_row("/private-health-insurance-cost-germany", "~1.800/mo")

pdf.sub_header("WECHSEL & ELIGIBILITY", BLUE)
pdf.page_row("/switch-public-to-private-health-insurance-germany", "~300/mo")
pdf.page_row("/private-health-insurance-salary-threshold-germany", "~200/mo")

pdf.sub_header("ZIELGRUPPEN", BLUE)
pdf.page_row("/private-health-insurance-freelancer-germany", "~130/mo")
pdf.page_row("/private-health-insurance-family-germany", "~80/mo")
pdf.page_row("/private-health-insurance-employees-germany", "~60/mo")
pdf.page_row("/private-health-insurance-students-germany", "~40/mo")

pdf.sub_header("INFORMATIONAL", BLUE)
pdf.page_row("/what-does-private-health-insurance-cover-germany", "~90/mo")
pdf.page_row("/public-vs-private-health-insurance-germany", "~300/mo")

pdf.ln(4)

# ??????????????????????????????????????????????
# TIER 2 - PUBLIC
# ??????????????????????????????????????????????
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(*SLATE)
pdf.cell(0, 5, "?????????????????  TIER 2 . Sub-Pages Public Insurance  ?????????????????", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

pdf.sub_header("VERGLEICH", TEAL)
pdf.page_row("/best-public-health-insurance-germany", "~400/mo")
pdf.page_row("/public-health-insurance-providers-germany", "~300/mo")

pdf.sub_header("TIER 3 . Einzelne GKV-Anbieter", TEAL)
pdf.page_row("/aok-health-insurance-germany", "~590/mo", indent=30)
pdf.page_row("/tk-health-insurance-germany", "~200/mo", indent=30)
pdf.page_row("/barmer-health-insurance-germany", "~150/mo", indent=30)
pdf.page_row("/dak-health-insurance-germany", "~80/mo", indent=30)

pdf.sub_header("TIER 3 . GKV-Vergleiche", TEAL)
pdf.page_row("/aok-vs-tk-germany", "~390/mo", indent=30)
pdf.page_row("/aok-vs-barmer-germany", "~100/mo", indent=30)

pdf.ln(4)

# ??????????????????????????????????????????????
# TIER 2 - EXPAT
# ??????????????????????????????????????????????
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(*SLATE)
pdf.cell(0, 5, "?????????????????  TIER 2 . Sub-Pages Expat Insurance  ?????????????????", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

pdf.sub_header("ZIELGRUPPEN", PURPLE)
pdf.page_row("/health-insurance-foreigners-germany", "~800/mo")
pdf.page_row("/health-insurance-freelancer-expats-germany", "~130/mo")

pdf.sub_header("SITUATIONEN", PURPLE)
pdf.page_row("/health-insurance-german-visa", "~50/mo")
pdf.page_row("/temporary-health-insurance-germany", "~30/mo")
pdf.page_row("/travel-insurance-germany", "~90/mo")

pdf.sub_header("STAEDTE (optional / Phase 2)", PURPLE)
pdf.page_row("/health-insurance-expats-berlin", "~60/mo", indent=30)
pdf.page_row("/health-insurance-expats-munich", "~40/mo", indent=30)
pdf.page_row("/health-insurance-expats-hamburg", "~20/mo", indent=30)

pdf.ln(4)

# ??????????????????????????????????????????????
# STANDALONE QUICK WINS
# ??????????????????????????????????????????????
pdf.section_bar("STANDALONE QUICK WINS - direkt von Homepage verlinkt", AMBER, "!")
pdf.page_row("/social-insurance-number-germany", "~2.500/mo  Feather #1 / MHCB #34")
pdf.page_row("/private-health-insurance-companies-germany", "~2.900/mo  Alle Anbieter Liste")

pdf.ln(4)

# ??????????????????????????????????????????????
# PAGE 2 - BOTTOM SECTIONS
# ??????????????????????????????????????????????
pdf.add_page()

# COMPARE
pdf.section_bar("COMPARE (Nav-Dropdown)", BLUE, "")
pdf.hub_row("/top-insurers/", "Hub", BLUE)
insurers = ["debeka", "allianz", "dkv", "axa", "barmenia", "hallesche", "hansemerkur", "signal-iduna", "continentale", "gothaer"]
for ins in insurers:
    pdf.page_row(f"/top-insurers/{ins}", "Review", indent=25)

pdf.ln(4)

# TOOLS
pdf.section_bar("TOOLS (Nav-Dropdown)", (234, 88, 12), "")
tools = [
    ("/calculator", "Beitragsrechner"),
    ("/quiz", "PKV-Eignungstest"),
    ("/compare", "Plan Vergleich"),
    ("/checklist", "Wechsel-Checkliste"),
]
for url, desc in tools:
    pdf.page_row(f"{url}  -  {desc}", "")

pdf.ln(4)

# GUIDES
pdf.section_bar("GUIDES (Nav-Dropdown)", SLATE, "")
guides = [
    ("/guide/who-qualifies", "Wer qualifiziert sich?"),
    ("/guide/how-to-switch", "Wie wechseln?"),
    ("/guide/for-freelancers", "Fuer Freelancer"),
    ("/guide/for-foreigners", "Fuer Austaender"),
    ("/guide/for-students", "Fuer Studenten"),
    ("/guide/costs-and-contributions", "Kosten & Beitraege"),
]
for url, desc in guides:
    pdf.page_row(f"{url}  -  {desc}", "")

pdf.ln(4)

# UTILITY
pdf.section_bar("UTILITY (Footer only)", GREEN, "")
util = ["/contact  - Get Advice CTA", "/about  - Team & Trust", "/privacy  - Legal", "/imprint  - Legal"]
for u in util:
    pdf.page_row(u, "")

pdf.ln(8)

# ??????????????????????????????????????????????
# SUMMARY TABLE
# ??????????????????????????????????????????????
pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(*DARK)
pdf.cell(0, 8, "ZUSAMMENFASSUNG - Wie viele Seiten?", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

rows = [
    ("Tier 1 - Haupt-Pillar-Pages", "3 Seiten", "Homepage + 3 Kategorien"),
    ("Tier 2 - Private Insurance Sub-Pages", "10 Seiten", "Kosten, Wechsel, Zielgruppen"),
    ("Tier 2 - Public Insurance Sub-Pages", "2 Seiten", "Best + Providers Liste"),
    ("Tier 3 - GKV Anbieter-Pages", "6 Seiten", "AOK, TK, Barmer, DAK + Vergleiche"),
    ("Tier 2 - Expat Insurance Sub-Pages", "5 Seiten", "Zielgruppen + Situationen"),
    ("Tier 3 - Expat Staedte (Phase 2)", "3 Seiten", "Berlin, Munich, Hamburg"),
    ("Standalone Quick Wins", "2 Seiten", "SVNR + Companies Liste"),
    ("Compare - Top Insurers", "11 Seiten", "Hub + 10 PKV-Anbieter"),
    ("Tools", "4 Seiten", "Calculator, Quiz, Compare, Checklist"),
    ("Guides", "6 Seiten", "Bestehende Guide-Pages"),
    ("Utility", "4 Seiten", "Contact, About, Privacy, Imprint"),
]

header_cols = ["Kategorie", "Anzahl", "Beschreibung"]
col_w = [80, 25, 80]

pdf.set_fill_color(*DARK)
pdf.set_font("Helvetica", "B", 8)
pdf.set_text_color(*LIGHT)
for h, w in zip(header_cols, col_w):
    pdf.cell(w, 8, f"  {h}", fill=True)
pdf.ln()

total = 0
for i, (cat, count, desc) in enumerate(rows):
    n = int(count.split()[0])
    total += n
    bg = (248, 250, 252) if i % 2 == 0 else (255, 255, 255)
    pdf.set_fill_color(*bg)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*DARK)
    pdf.cell(col_w[0], 7, f"  {cat}", fill=True)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*BLUE)
    pdf.cell(col_w[1], 7, f"  {count}", fill=True)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*SLATE)
    pdf.cell(col_w[2], 7, f"  {desc}", fill=True)
    pdf.ln()

pdf.set_fill_color(*GREEN)
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(*LIGHT)
pdf.cell(col_w[0], 9, "  GESAMT", fill=True)
pdf.cell(col_w[1], 9, f"  {total} Seiten", fill=True)
pdf.cell(col_w[2], 9, "  Vollstaendige Site-Abdeckung", fill=True)
pdf.ln()

pdf.set_text_color(0, 0, 0)
pdf.ln(8)

# BUILD ORDER
pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(*DARK)
pdf.cell(0, 8, "BUILD-REIHENFOLGE (nach Prioritaet)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

phases = [
    ("Phase 1 - SOFORT", GREEN, [
        "3x Tier 1 Hubs bauen (Private, Public, Expat)",
        "/social-insurance-number-germany  (2.500/mo Quick Win)",
        "/health-insurance-expats-germany  (4.200/mo groesste Luecke)",
    ]),
    ("Phase 2 - KURZFRISTIG", BLUE, [
        "10x Tier 2 Sub-Pages Private Insurance",
        "/best-private-health-insurance-germany  (2.100/mo)",
        "/private-health-insurance-cost-germany  (1.800/mo)",
    ]),
    ("Phase 3 - MITTELFRISTIG", TEAL, [
        "GKV Anbieter-Pages: AOK, TK, Barmer, DAK",
        "Expat Sub-Pages: Visa, Temporary, Travel",
        "/private-health-insurance-companies-germany",
    ]),
    ("Phase 4 - LANGFRISTIG", SLATE, [
        "Stadt-Pages: Berlin, Munich, Hamburg",
        "Weitere Zielgruppen-Pages",
        "Blog/Support-Content",
    ]),
]

for phase, color, items in phases:
    pdf.set_fill_color(*color)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*LIGHT)
    pdf.cell(0, 8, f"  {phase}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
    pdf.set_text_color(0, 0, 0)
    for item in items:
        pdf.set_fill_color(245, 248, 252)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*DARK)
        pdf.cell(0, 6, f"      ->  {item}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
    pdf.ln(2)

pdf.output(OUTPUT)
print(f"PDF gespeichert: {OUTPUT}")
