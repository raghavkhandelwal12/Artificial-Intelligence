import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.patheffects as path_effects

from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak,
    Image, Paragraph
)
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from textwrap import wrap

# ============================
# FILE PATHS
# ============================
OBS_CSV = r"C:\Users\pc\Downloads\Force Motors Observation List(Sheet) (1).csv"
USERS_CSV = r"C:\Users\pc\Downloads\Force Motors User List(employee (3)).csv"

OUT_PDF = r"C:\Users\pc\Downloads\Akurdi_Report_FINAL_ALLPAGES.pdf"
PAGE2A_IMG = r"C:\Users\pc\Downloads\Akurdi_Page2A_Bar.png"
PAGE2B_IMG = r"C:\Users\pc\Downloads\Akurdi_Page2B_Bar.png"
PAGE3_IMG = r"C:\Users\pc\Downloads\Akurdi_Page3.png"
LOGO_PATH = r"C:\download (1).png"
HEADER_HEX = "#307268"

# ============================
# LOAD DATA
# ============================
obs = pd.read_csv(OBS_CSV, encoding="latin1")
users = pd.read_csv(USERS_CSV, encoding="latin1")

obs["Site Name"] = obs["Site Name"].astype(str).str.strip()
site_df = obs[obs["Site Name"].str.lower() == "akurdi"].copy()

if site_df.empty:
    raise SystemExit("No Akurdi data found!")

# ============================
# CLEAN STATUS
# ============================
site_df["Status_clean"] = (
    site_df["Status"].astype(str)
    .str.lower()
    .str.replace("-", " ")
    .str.replace("_", " ")
    .str.strip()
)

site_df["Status_clean"] = site_df["Status_clean"].replace({
    "inprogress": "in progress",
    "in-progress": "in progress",
    "in progress ": "in progress",
    "close": "closed",
    "closed ": "closed"
})

# ============================
# CLEAN AREA NAME
# ============================
site_df["Area Clean"] = (
    site_df["Area Name"]
    .astype(str)
    .str.replace(r"[-\s]+$", "", regex=True)
    .str.strip()
)

# ============================
# CLEAN AGING
# ============================
site_df["Aging"] = (
    site_df["Aging"].astype(str)
    .str.extract(r"(\d+)")
    .fillna("0")
    .astype(int)
)

# ============================
# PAGE 1 — EMPLOYEE SUMMARY
# ============================
emp = (
    site_df.groupby("Logged by")
    .agg(
        Total_Observations=("Issue Id", "count"),
        Total_Open=("Status_clean", lambda x: (x == "open").sum()),
        Total_InProgress=("Status_clean", lambda x: (x == "in progress").sum()),
        Total_Review=("Status_clean", lambda x: (x == "review").sum()),
        Total_Closed=("Status_clean", lambda x: (x == "closed").sum())
    )
).reset_index()

emp = emp.sort_values("Total_Observations", ascending=False)

# Calculate totals
total_sum = {
    "Total_Observations": int(emp["Total_Observations"].sum()),
    "Total_Open": int(emp["Total_Open"].sum()),
    "Total_InProgress": int(emp["Total_InProgress"].sum()),
    "Total_Review": int(emp["Total_Review"].sum()),
    "Total_Closed": int(emp["Total_Closed"].sum())
}

# ============================
# PAGE 2 — DIVISION CHART
# ============================
division = site_df.groupby("Area Clean").agg(
    Close=("Status_clean", lambda x: (x == "closed").sum()),
    Open=("Status_clean", lambda x: (x == "open").sum()),
    InProgress=("Status_clean", lambda x: (x == "in progress").sum()),
    Review=("Status_clean", lambda x: (x == "review").sum())
)
division["Total"] = division.sum(axis=1)
division = division.sort_values("Total", ascending=False)

import math

def build_area_chart(df, output_path):
    areas = df.index.tolist()
    close_vals = df["Close"].values
    inp_vals = df["InProgress"].values
    open_vals = df["Open"].values
    rev_vals = df["Review"].values
    totals = df["Total"].values

    fig_h = max(6, len(areas) * 0.55)
    fig, ax = plt.subplots(figsize=(16, fig_h))

    y_pos = np.arange(len(areas))
    
    # Calculate max value early for use in label function
    max_val = max(totals) if len(totals) > 0 else 100

    bar1 = ax.barh(y_pos, close_vals, color="#2ECC71", label="Closed")
    bar2 = ax.barh(y_pos, inp_vals, left=close_vals, color="#F5B041", label="In Progress")
    bar3 = ax.barh(y_pos, open_vals, left=close_vals + inp_vals, color="#E74C3C", label="Open")
    bar4 = ax.barh(y_pos, rev_vals, left=close_vals + inp_vals + open_vals, color="#3498DB", label="Review")

    def add_labels(bars, values):
        for bar, val in zip(bars, values):
            if val > 0:
                bar_width = bar.get_width()
                # Only show label if bar is wide enough (increased threshold)
                threshold = max(5, max_val * 0.03)  # At least 5 or 3% of max value
                if bar_width > threshold:
                    x = bar.get_x() + bar_width / 2
                    y = bar.get_y() + bar.get_height() / 2
                    # Use white text for better contrast on colored bars
                    text_color = "white" if bar_width > 10 else "black"
                    ax.text(x, y, str(int(val)), ha='center', va='center', 
                           fontsize=8, color=text_color, fontweight="bold")

    # Add labels with proper positioning
    add_labels(bar1, close_vals)
    add_labels(bar2, inp_vals)
    add_labels(bar3, open_vals)
    add_labels(bar4, rev_vals)

    # Add total labels at the end
    for i, total in enumerate(totals):
        offset = max(max_val * 0.02, 5)  # Dynamic offset
        ax.text(totals[i] + offset, y_pos[i], str(int(total)), 
               va='center', fontsize=10, fontweight="bold", color="black")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(areas, fontsize=10)
    ax.invert_yaxis()
    
    # Set x-axis limit with some padding
    ax.set_xlim(0, max_val * 1.15)
    
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), borderaxespad=0, 
             fontsize=10, frameon=True, facecolor="white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()

# Split and build charts
mid = int(math.ceil(len(division) / 2.0))
division_part1 = division.iloc[:mid].copy().sort_values("Total", ascending=False)
division_part2 = division.iloc[mid:].copy().sort_values("Total", ascending=False)

build_area_chart(division_part1, PAGE2A_IMG)
build_area_chart(division_part2, PAGE2B_IMG)

# ============================
# PAGE 3 — DASHBOARD (Power BI Style)
# ============================
fig = plt.figure(figsize=(14, 8))

gs = gridspec.GridSpec(
    2, 2,
    width_ratios=[1, 1],
    height_ratios=[1, 1],
    hspace=0.35,
    wspace=0.30
)

# TOP LEFT - What Happened PIE
ax1 = fig.add_subplot(gs[0, 0])
w = site_df["What Happened"].value_counts()

if len(w):
    colors_what = ['#0078D4', '#002050']  # Blue shades
    wedges, texts, autotexts = ax1.pie(
        w.values,
        labels=None,
        autopct=lambda pct: f'{pct:.1f}%' if pct > 5 else '',
        startangle=90,
        colors=colors_what,
        textprops={'fontsize': 10, 'color': 'white', 'fontweight': 'bold'},
        pctdistance=0.75
    )
    
    # Add legend below pie
    legend_labels = [f'{label} ({val})' for label, val in zip(w.index, w.values)]
    ax1.legend(wedges, legend_labels, title="Unsafe Act & Condition",
              loc="center", bbox_to_anchor=(0.5, -0.15),
              fontsize=9, frameon=False, ncol=1)
    
    ax1.set_title("Unsafe Act & Condition", fontsize=13, fontweight="bold", pad=15)
else:
    ax1.text(0.5, 0.5, "No data", ha="center", va="center")
    ax1.set_title("Unsafe Act & Condition", fontsize=13, fontweight="bold")

# TOP RIGHT - Status Summary BAR (Horizontal)
ax2 = fig.add_subplot(gs[0, 1])
order = ["closed", "open", "in progress", "review"]
sc = site_df["Status_clean"].value_counts().reindex(order, fill_value=0)

bar_colors = ["#70AD47", "#C00000", "#FFC000", "#4472C4"]  # Power BI colors
bars = ax2.barh(sc.index, sc.values, color=bar_colors, height=0.6)

# Add value labels at the end of bars
for bar in bars:
    width = bar.get_width()
    ax2.text(
        width + max(sc.values) * 0.02,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va='center', ha='left', fontsize=10, fontweight='bold'
    )

ax2.set_xlim(0, max(sc.values) * 1.2)
ax2.set_xlabel('')
ax2.set_ylabel('')
ax2.set_title("Summarised", fontsize=13, fontweight="bold", pad=15)
ax2.invert_yaxis()
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.spines["left"].set_visible(False)
ax2.tick_params(left=False, bottom=False)
ax2.set_xticks([])

# BOTTOM - Severity DONUT (Spanning both columns)
ax3 = fig.add_subplot(gs[1, :])
sev = site_df["Severity"].value_counts()

if len(sev):
    # Power BI style colors
    severity_colors = {
        'Medium': '#0078D4',  # Blue
        'High': '#C00000',    # Red
        'Low': '#FFC000'      # Orange/Yellow
    }
    colors_list = [severity_colors.get(label, '#95A5A6') for label in sev.index]
    
    # Create donut
    wedges, texts, autotexts = ax3.pie(
        sev.values,
        labels=None,
        autopct='',
        startangle=90,
        colors=colors_list,
        wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2)
    )
    
    # Add labels with counts and percentages outside
    total_count = sum(sev.values)
    
    for i, (wedge, label, count) in enumerate(zip(wedges, sev.index, sev.values)):
        ang = (wedge.theta2 - wedge.theta1) / 2.0 + wedge.theta1
        
        x = 1.3 * np.cos(np.radians(ang))
        y = 1.3 * np.sin(np.radians(ang))
        
        ha = 'left' if x > 0 else 'right'
        pct = (count / total_count) * 100
        
        # Add text with count and percentage
        ax3.text(x, y, f'{int(count)} ({pct:.2f}%)',
                ha=ha, va='center',
                fontsize=10, fontweight='bold')
    
    # White center circle
    circle = plt.Circle((0, 0), 0.60, color="white")
    ax3.add_artist(circle)
    
    # Legend on the right
    legend = ax3.legend(
        wedges,
        [label for label in sev.index],
        title="Severity",
        title_fontsize=11,
        loc="center left",
        bbox_to_anchor=(1.05, 0.5),
        fontsize=10,
        frameon=False
    )
    legend.get_title().set_fontweight('bold')
    
    ax3.set_title("Severity", fontsize=13, fontweight="bold", pad=15)
else:
    ax3.text(0.5, 0.5, "No severity data", ha="center", va="center")
    ax3.set_title("Severity", fontsize=13, fontweight="bold")

plt.tight_layout()
plt.savefig(PAGE3_IMG, dpi=150, bbox_inches="tight")
plt.close()

# ==========================================================
# ADD BORDER + LOGO + FOOTER ON EVERY PAGE
# ==========================================================
def add_border_logo_footer(canvas, doc):
    canvas.saveState()
    
    border_color = colors.HexColor(HEADER_HEX)

    # Border (left and right only)
    canvas.setStrokeColor(border_color)
    canvas.setLineWidth(2)

    canvas.line(doc.leftMargin - 6, 
                doc.bottomMargin - 6,
                doc.leftMargin - 6,
                doc.height + doc.bottomMargin + 6)

    canvas.line(doc.leftMargin + doc.width + 6, 
                doc.bottomMargin - 6,
                doc.leftMargin + doc.width + 6,
                doc.height + doc.bottomMargin + 6)

    # Footer bar
    footer_h = 28
    canvas.setFillColor(border_color)
    canvas.rect(doc.leftMargin - 6,
                doc.bottomMargin - 6,
                doc.width + 12,
                footer_h,
                fill=1,
                stroke=0)

    # Footer text
    canvas.setFont("Helvetica-Bold", 12)
    canvas.setFillColor(colors.whitesmoke)
    canvas.drawCentredString(
        doc.leftMargin + doc.width / 2,
        doc.bottomMargin + 8,
        "Created by Momentum"
    )

    canvas.restoreState()

# ============================
# HEADER FUNCTION WITH LOGO (REDUCED SPACE)
# ============================
PAGE_SIZE = landscape(A4)
left_margin = right_margin = 0.5 * inch
top_margin = 0.30 * inch  # REDUCED from 0.40
bottom_margin = 0.60 * inch

usable_width = PAGE_SIZE[0] - left_margin - right_margin

def make_header_with_logo(title_text):
    """Create compact header with title and logo"""
    header = Table(
        [
            [
                Paragraph(
                    f"<b>{title_text}</b>",
                    ParagraphStyle(
                        name="header_title",
                        fontSize=13,  # Reduced from 14
                        textColor=colors.whitesmoke,
                        alignment=1,
                        fontName="Helvetica-Bold"
                    )
                ),
                Image(LOGO_PATH, width=60, height=22)  # Smaller logo
            ]
        ],
        colWidths=[usable_width - 70, 70]
    )

    header.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor(HEADER_HEX)),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (0,0), (0,0), "CENTER"),
        ("ALIGN", (1,0), (1,0), "RIGHT"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),  # REDUCED from 6
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),  # REDUCED from 6
    ]))

    return header

# ============================
# BUILD PDF
# ============================
doc = SimpleDocTemplate(
    OUT_PDF,
    pagesize=PAGE_SIZE,
    leftMargin=left_margin,
    rightMargin=right_margin,
    topMargin=top_margin,
    bottomMargin=bottom_margin
)

story = []

# ============================
# PAGE 1 - TWO COLUMNS (ALL EMPLOYEES ON ONE PAGE)
# ============================
header = make_header_with_logo("MiSafe Logged Details From 01st March to 23rd Nov 2025")
story.append(header)
story.append(Spacer(1, 0.04 * inch))  # REDUCED from 0.06

# KPI boxes - compact
kpi_vals = [
    total_sum["Total_Observations"],
    total_sum["Total_Open"],
    total_sum["Total_InProgress"],
    total_sum["Total_Review"],
    total_sum["Total_Closed"]
]

kpi_labels = ["Total Observations", "Open", "In Progress", "Review", "Closed"]
kpi_box_width = usable_width / 5.0

kpi_row = []
for val, label in zip(kpi_vals, kpi_labels):
    val_style = ParagraphStyle("kpi_val", fontSize=20, fontName="Helvetica-Bold", alignment=1)
    lbl_style = ParagraphStyle("kpi_lbl", fontSize=7.5, fontName="Helvetica", alignment=1)
    
    box = Table(
        [[Paragraph(f"<b>{val}</b>", val_style)],
         [Paragraph(label, lbl_style)]],
        colWidths=[kpi_box_width * 0.95],
        rowHeights=[30, 18]
    )
    box.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (0,0), "TOP"),
        ("VALIGN", (0,1), (0,1), "BOTTOM"),
        ("TOPPADDING", (0,0), (0,0), 6),
        ("BOTTOMPADDING", (0,0), (0,0), 0),
        ("TOPPADDING", (0,1), (0,1), 0),
        ("BOTTOMPADDING", (0,1), (0,1), 5),
        ("BOX", (0,0), (-1,-1), 1, colors.grey),
        ("BACKGROUND", (0,0), (-1,-1), colors.white)
    ]))
    kpi_row.append(box)

kpi_table = Table([kpi_row], colWidths=[kpi_box_width] * 5)
kpi_table.setStyle(TableStyle([
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE")
]))
story.append(kpi_table)
story.append(Spacer(1, 0.04*inch))  # REDUCED from 0.06

# TWO COLUMN LAYOUT
gutter = 0.25 * inch
col_width = (usable_width - gutter) / 2.0

col_widths_emp = [
    col_width * 0.30,
    col_width * 0.175,
    col_width * 0.115,
    col_width * 0.175,
    col_width * 0.115,
    col_width * 0.12
]

total_employees = len(emp)
mid_point = (total_employees + 1) // 2

left_employees = emp.iloc[:mid_point].copy()
right_employees = emp.iloc[mid_point:].copy()

# LEFT COLUMN DATA
left_data = [["Logged by", "Total\nObservations", "Total\nOpen", "Total In\nProgress", "Total\nReview", "Total\nClosed"]]
for _, row in left_employees.iterrows():
    left_data.append([
        row["Logged by"],
        int(row["Total_Observations"]),
        int(row["Total_Open"]),
        int(row["Total_InProgress"]),
        int(row["Total_Review"]),
        int(row["Total_Closed"])
    ])

left_subtotal = [
    "Total",
    int(left_employees["Total_Observations"].sum()),
    int(left_employees["Total_Open"].sum()),
    int(left_employees["Total_InProgress"].sum()),
    int(left_employees["Total_Review"].sum()),
    int(left_employees["Total_Closed"].sum())
]
left_data.append(left_subtotal)

# RIGHT COLUMN DATA
right_data = [["Logged by", "Total\nObservations", "Total\nOpen", "Total In\nProgress", "Total\nReview", "Total\nClosed"]]
for _, row in right_employees.iterrows():
    right_data.append([
        row["Logged by"],
        int(row["Total_Observations"]),
        int(row["Total_Open"]),
        int(row["Total_InProgress"]),
        int(row["Total_Review"]),
        int(row["Total_Closed"])
    ])

right_subtotal = [
    "Total",
    int(right_employees["Total_Observations"].sum()),
    int(right_employees["Total_Open"].sum()),
    int(right_employees["Total_InProgress"].sum()),
    int(right_employees["Total_Review"].sum()),
    int(right_employees["Total_Closed"].sum())
]
right_data.append(right_subtotal)

# Create LEFT table
left_table = Table(left_data, colWidths=col_widths_emp, repeatRows=1)
left_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor(HEADER_HEX)),
    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 7),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ALIGN", (0,0), (0,0), "LEFT"),
    ("ALIGN", (1,0), (-1,0), "CENTER"),
    ("ALIGN", (0,1), (0,-1), "LEFT"),
    ("ALIGN", (1,1), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("FONTSIZE", (0,1), (-1,-2), 6.5),
    ("FONTNAME", (0,1), (-1,-2), "Helvetica"),
    ("LEFTPADDING", (0,0), (-1,-1), 2),
    ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ("TOPPADDING", (0,0), (-1,0), 3),
    ("BOTTOMPADDING", (0,0), (-1,0), 3),
    ("TOPPADDING", (0,1), (-1,-2), 1.5),
    ("BOTTOMPADDING", (0,1), (-1,-2), 1.5),
    ("BACKGROUND", (0, len(left_data)-1), (-1, len(left_data)-1), colors.Color(1, 0.92, 0.5)),
    ("FONTNAME", (0, len(left_data)-1), (-1, len(left_data)-1), "Helvetica-Bold"),
    ("FONTSIZE", (0, len(left_data)-1), (-1, len(left_data)-1), 7),
    ("TOPPADDING", (0, len(left_data)-1), (-1, len(left_data)-1), 3),
    ("BOTTOMPADDING", (0, len(left_data)-1), (-1, len(left_data)-1), 3),
]))

# Create RIGHT table
right_table = Table(right_data, colWidths=col_widths_emp, repeatRows=1)
right_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor(HEADER_HEX)),
    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 7),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ALIGN", (0,0), (0,0), "LEFT"),
    ("ALIGN", (1,0), (-1,0), "CENTER"),
    ("ALIGN", (0,1), (0,-1), "LEFT"),
    ("ALIGN", (1,1), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("FONTSIZE", (0,1), (-1,-2), 6.5),
    ("FONTNAME", (0,1), (-1,-2), "Helvetica"),
    ("LEFTPADDING", (0,0), (-1,-1), 2),
    ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ("TOPPADDING", (0,0), (-1,0), 3),
    ("BOTTOMPADDING", (0,0), (-1,0), 3),
    ("TOPPADDING", (0,1), (-1,-2), 1.5),
    ("BOTTOMPADDING", (0,1), (-1,-2), 1.5),
    ("BACKGROUND", (0, len(right_data)-1), (-1, len(right_data)-1), colors.Color(1, 0.92, 0.5)),
    ("FONTNAME", (0, len(right_data)-1), (-1, len(right_data)-1), "Helvetica-Bold"),
    ("FONTSIZE", (0, len(right_data)-1), (-1, len(right_data)-1), 7),
    ("TOPPADDING", (0, len(right_data)-1), (-1, len(right_data)-1), 3),
    ("BOTTOMPADDING", (0, len(right_data)-1), (-1, len(right_data)-1), 3),
]))

combined_tables = Table(
    [[left_table, Spacer(gutter, 0), right_table]],
    colWidths=[col_width, gutter, col_width]
)
combined_tables.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP")
]))

story.append(combined_tables)

# ============================
# PAGE 2 CHARTS
# ============================
story.append(PageBreak())
chart_header_2a = make_header_with_logo("Dashboard")
story.append(chart_header_2a)
story.append(Spacer(1, 0.04 * inch))  # REDUCED
story.append(Image(PAGE2A_IMG, width=10.2*inch, height=5.8*inch))

story.append(PageBreak())
chart_header_2b = make_header_with_logo("Dashboard")
story.append(chart_header_2b)
story.append(Spacer(1, 0.04 * inch))  # REDUCED
story.append(Image(PAGE2B_IMG, width=10.2*inch, height=5.8*inch))

# ============================
# PAGE 3
# ============================
story.append(PageBreak())
chart_header_3 = make_header_with_logo("Dashboard")
story.append(chart_header_3)
story.append(Spacer(1, 0.04 * inch))  # REDUCED
story.append(Image(PAGE3_IMG, width=10*inch, height=5*inch))

# ============================
# AREA-WISE PAGES
# ============================
wrap_style = ParagraphStyle("wrap", fontSize=7, leading=8.5, fontName="Helvetica")
ALL_AREAS = sorted(site_df["Area Clean"].dropna().unique())

col_width_area = [2.6*inch, 1.1*inch, 0.75*inch, 0.95*inch, 1.5*inch, 1.4*inch, 0.65*inch, 0.6*inch]
ROWS_PER_AREA_PAGE = 22  # Increased from 20

for area in ALL_AREAS:
    area_df = site_df[
        (site_df["Area Clean"] == area) &
        (site_df["Status_clean"] == "open")
    ].copy()

    if area_df.empty:
        continue

    cols = ["Description", "What Happened", "Severity", "Logged by", "Area Name", "Location", "Status", "Aging"]
    cols = [c for c in cols if c in area_df.columns]
    
    col_width_area_adjusted = col_width_area[:len(cols)]
    
    all_rows = []
    for _, r in area_df.iterrows():
        row = [Paragraph(str(r[c]), wrap_style) for c in cols]
        all_rows.append(row)
    
    total_rows = len(all_rows)
    page_count = math.ceil(total_rows / ROWS_PER_AREA_PAGE) if total_rows > ROWS_PER_AREA_PAGE else 1
    
    for page_idx in range(page_count):
        story.append(PageBreak())
        
        area_title = f"{area}"
        
        area_header_style = ParagraphStyle(
            name="area_header",
            fontSize=12,  # Reduced from 13
            textColor=colors.whitesmoke,
            alignment=1,
            fontName="Helvetica-Bold"
        )
        
        area_header = Table(
            [[Paragraph(f"<b>{area_title}</b>", area_header_style), Image(LOGO_PATH, width=60, height=22)]],
            colWidths=[usable_width - 70, 70]
        )

        area_header.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), colors.HexColor(HEADER_HEX)),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("ALIGN", (0,0), (0,0), "CENTER"),
            ("ALIGN", (1,0), (1,0), "RIGHT"),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ]))

        story.append(area_header)
        story.append(Spacer(1, 0.04*inch))  # REDUCED
        
        start_idx = page_idx * ROWS_PER_AREA_PAGE
        end_idx = min(start_idx + ROWS_PER_AREA_PAGE, total_rows)
        page_rows = all_rows[start_idx:end_idx]
        
        data = [cols] + page_rows
        
        t = Table(data, colWidths=col_width_area_adjusted, repeatRows=1)
        
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor(HEADER_HEX)),
            ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,0), 7.5),
            ("GRID", (0,0), (-1,-1), 0.4, colors.grey),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING", (0,0), (-1,-1), 2.5),
            ("RIGHTPADDING", (0,0), (-1,-1), 2.5),
            ("TOPPADDING", (0,0), (-1,-1), 2.5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 2.5),
        ]))
        
        story.append(t)

# ============================
# FINAL PDF BUILD
# ============================
doc.build(
    story,
    onFirstPage=add_border_logo_footer,
    onLaterPages=add_border_logo_footer
)

print("✓ FINAL REPORT CREATED:", OUT_PDF)
print(f"✓ Total observations: {total_sum['Total_Observations']}")