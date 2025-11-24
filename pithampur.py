import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from textwrap import wrap
from PIL import Image as PILImage  

from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak,
    Image, Paragraph, KeepTogether
)
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas

# -----------------------------
# CONFIG - update file paths here
# -----------------------------
OBS_CSV = r"C:\Users\pc\Downloads\Force Motors Observation List(Sheet) (1).csv"
USERS_CSV = r"C:\Users\pc\Downloads\Force Motors User List(employee (3)).csv"
OUT_PDF = r"C:\Users\pc\Downloads\Pithampur_Report_FINAL_TwoColumn_fixed.pdf"
OUT_PITHAMPUR_CSV = r"C:\Users\pc\Downloads\Pithampur_Observations_Filtered.csv"

# Convert WEBP to PNG if needed
WEBP_LOGO = r"C:\Users\pc\Downloads\OIP.webp"
PNG_LOGO = r"C:\Users\pc\Downloads\OIP.png"

# Try to convert WEBP to PNG
try:
    from PIL import Image as PILImage
    if not os.path.exists(PNG_LOGO):
        img = PILImage.open(WEBP_LOGO)
        img.save(PNG_LOGO, 'PNG')
        print(f"✓ Converted logo to PNG: {PNG_LOGO}")
    LOGO_PATH = PNG_LOGO
except Exception as e:
    print(f"Warning: Could not convert logo: {e}")
    LOGO_PATH = WEBP_LOGO  # Try using WEBP directly

PAGE2_IMG = r"C:\Users\pc\Downloads\Pithampur_Page2_Bar.png"
PAGE3_IMG = r"C:\Users\pc\Downloads\Pithampur_Page3.png"
HEADER_HEX = "#307268"
# -----------------------------

def load_csv_try(path):
    """Try reading CSV with several common encodings."""
    for enc in ("utf-8", "latin1", "cp1252", "iso-8859-1"):
        try:
            return pd.read_csv(path, encoding=enc)
        except Exception:
            pass
    return pd.read_csv(path, encoding="utf-8", engine="python", errors="replace")

# Load CSVs
obs = load_csv_try(OBS_CSV)
users = load_csv_try(USERS_CSV)

# Normalize column names
obs.columns = [c.strip() for c in obs.columns]
users.columns = [c.strip() for c in users.columns]

# --- Detect columns ---
obs_expected = {
    "issue": ["Issue Id", "IssueId", "Observation ID", "Observation Id", "ID", "Id"],
    "site": ["Site Name", "SiteName", "Plant Name", "PlantName"],
    "area": ["Area Name", "AreaName", "Area"],
    "logged_by": ["Logged by", "Logged By", "Logged_by", "LoggedBy", "User", "Assigned To"],
    "status": ["Status", "status"]
}

def find_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    lowcols = {col.lower(): col for col in df.columns}
    for c in candidates:
        if c.lower() in lowcols:
            return lowcols[c.lower()]
    return None

issue_col = find_column(obs, obs_expected["issue"])
site_col = find_column(obs, obs_expected["site"])
area_col = find_column(obs, obs_expected["area"])
logged_col = find_column(obs, obs_expected["logged_by"])
status_col = find_column(obs, obs_expected["status"])

if site_col is None:
    raise SystemExit("No Site/Plant column found in observations CSV.")
if logged_col is None:
    logged_col = obs.columns[0]
if issue_col is None:
    issue_col = obs.columns[0]

# Ensure string types
obs[site_col] = obs[site_col].astype(str).str.strip()
obs[logged_col] = obs[logged_col].astype(str).str.strip()
if area_col:
    obs[area_col] = obs[area_col].astype(str).str.strip()
if status_col:
    obs[status_col] = obs[status_col].astype(str).str.strip().str.lower()

# Filter to Pithampur site
site_mask = obs[site_col].str.lower().str.contains("pithampur", na=False)
site_df = obs[site_mask].copy()
if site_df.empty:
    raise SystemExit("No rows with 'Pithampur' found.")

site_df.to_csv(OUT_PITHAMPUR_CSV, index=False)
print("Saved filtered CSV to:", OUT_PITHAMPUR_CSV)

# --- Find employee columns ---
user_expected = {
    "empname": ["Employee Name", "EmployeeName", "Employee"],
    "plant": ["Plant Name", "PlantName", "Plant"]
}
emp_name_col = find_column(users, user_expected["empname"])
emp_plant_col = find_column(users, user_expected["plant"])

if emp_name_col is None:
    raise SystemExit("Cannot find Employee Name column.")
if emp_plant_col is None:
    raise SystemExit("Cannot find Plant Name column.")

users[emp_name_col] = users[emp_name_col].astype(str).str.strip()
users[emp_plant_col] = users[emp_plant_col].astype(str).str.strip()

# Filter users to Pithampur
users_pith = users[users[emp_plant_col].str.lower().str.contains("pithampur", na=False)].copy()
if users_pith.empty:
    raise SystemExit("No employees with 'Pithampur' found.")

# Merge observations with employees
site_df["_logged_norm"] = site_df[logged_col].astype(str).str.lower().str.strip()
users_pith["_emp_norm"] = users_pith[emp_name_col].astype(str).str.lower().str.strip()
merged = site_df.merge(users_pith, left_on="_logged_norm", right_on="_emp_norm", how="inner", suffixes=("", "_user"))

if merged.empty:
    merged = site_df.copy()
    merged["_emp_norm"] = merged["_logged_norm"]
    print("Warning: Inner merge returned empty.")

# Normalize status
if status_col:
    merged["Status_clean"] = merged[status_col].astype(str).str.lower().str.replace("-", " ").str.replace("_", " ").str.strip()
    merged["Status_clean"] = merged["Status_clean"].replace({
        "inprogress": "in progress",
        "in progress ": "in progress",
        "in-progress": "in progress",
        "close": "closed",
        "closed ": "closed"
    })
else:
    merged["Status_clean"] = "unknown"

# Determine display column
if emp_name_col in merged.columns:
    display_logged_col = emp_name_col
else:
    display_logged_col = logged_col

# Aggregate per employee
agg = merged.groupby(display_logged_col).agg(
    Total_Observations=(issue_col, "count"),
    Total_Open=("Status_clean", lambda x: (x == "open").sum()),
    Total_InProgress=("Status_clean", lambda x: (x == "in progress").sum()),
    Total_Review=("Status_clean", lambda x: (x == "review").sum()),
    Total_Closed=("Status_clean", lambda x: (x == "closed").sum())
).reset_index()

agg = agg.sort_values("Total_Observations", ascending=False).reset_index(drop=True)

# Calculate totals
total_sum = {
    "Total_Observations": int(agg["Total_Observations"].sum()),
    "Total_Open": int(agg["Total_Open"].sum()),
    "Total_InProgress": int(agg["Total_InProgress"].sum()),
    "Total_Review": int(agg["Total_Review"].sum()),
    "Total_Closed": int(agg["Total_Closed"].sum())
}

# Convert to int
for col in ["Total_Observations", "Total_Open", "Total_InProgress", "Total_Review", "Total_Closed"]:
    agg[col] = agg[col].fillna(0).astype(int)

# Prepare rows
rows = []
for _, r in agg.iterrows():
    rows.append([
        str(r[display_logged_col]), 
        int(r["Total_Observations"]), 
        int(r["Total_Open"]),
        int(r["Total_InProgress"]), 
        int(r["Total_Review"]), 
        int(r["Total_Closed"])
    ])

# --- Build charts ---
if area_col and area_col in merged.columns:
    merged_area_col = area_col
elif "Area Name" in merged.columns:
    merged_area_col = "Area Name"
else:
    merged_area_col = None

if merged_area_col:
    division = merged.groupby(merged[merged_area_col].astype(str).str.strip()).agg(
        Close=("Status_clean", lambda x: (x == "closed").sum()),
        Open=("Status_clean", lambda x: (x == "open").sum()),
        InProgress=("Status_clean", lambda x: (x == "in progress").sum()),
        Review=("Status_clean", lambda x: (x == "review").sum())
    )
    division["Total"] = division.sum(axis=1)
    division = division.sort_values("Total", ascending=False)
else:
    division = pd.DataFrame({})

# -------------------------------------------
# PAGE 2: POWER BI STYLE AREA CHART (2 PAGES)
# -------------------------------------------

def build_area_chart(df, output_path):
    areas = df.index.tolist()

    close_vals = df["Close"].values
    inp_vals = df["InProgress"].values
    open_vals = df["Open"].values
    rev_vals = df["Review"].values
    totals = df["Total"].values

    fig_h = max(6, len(areas) * 0.55)
    fig, ax = plt.subplots(figsize=(16, fig_h))

    # Title
    ax.set_title(
        "Dashboard – Division Specific",
        fontsize=18,
        fontweight="bold",
        color="#307268",
        pad=25
    )

    # positions
    y_pos = np.arange(len(areas))

    # stacked bars
    bar1 = ax.barh(y_pos, close_vals, color="#2ECC71", label="Closed")
    bar2 = ax.barh(y_pos, inp_vals, left=close_vals, color="#F5B041", label="In Progress")
    bar3 = ax.barh(y_pos, open_vals, left=close_vals + inp_vals, color="#E74C3C", label="Open")
    bar4 = ax.barh(y_pos, rev_vals, left=close_vals + inp_vals + open_vals, color="#3498DB", label="Review")

    # add labels inside each segment
    def add_labels(bars, values):
        for bar, val in zip(bars, values):
            if val > 0:
                x = bar.get_x() + bar.get_width() / 2
                y = bar.get_y() + bar.get_height() / 2
                ax.text(x, y, str(int(val)), ha='center', va='center', fontsize=8, color="black", fontweight="bold")

    add_labels(bar1, close_vals)
    add_labels(bar2, inp_vals)
    add_labels(bar3, open_vals)
    add_labels(bar4, rev_vals)

    # total at end
    for i, total in enumerate(totals):
        ax.text(totals[i] + 8, y_pos[i], str(int(total)), va='center', fontsize=10, fontweight="bold", color="black")

    # y labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(areas, fontsize=10)

    # invert so first (largest) is at top
    ax.invert_yaxis()

    # legend and style
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), borderaxespad=0, fontsize=10, frameon=True, facecolor="white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


# Sort full list (largest first), then split
division = division.sort_values("Total", ascending=False)
mid = int(math.ceil(len(division) / 2.0))

division_part1 = division.iloc[:mid].copy().sort_values("Total", ascending=False)
division_part2 = division.iloc[mid:].copy().sort_values("Total", ascending=False)

# output paths
PAGE2A_IMG = r"C:\Users\pc\Downloads\Pithampur_Page2A.png"
PAGE2B_IMG = r"C:\Users\pc\Downloads\Pithampur_Page2B.png"

# build images
build_area_chart(division_part1, PAGE2A_IMG)
build_area_chart(division_part2, PAGE2B_IMG)
# ---------------------------------------
# PAGE 3 DASHBOARD - CLEAN POWER BI STYLE
# ---------------------------------------

# Create modern figure
fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor('#F8F8F8')

# Modern grid layout
gs = gridspec.GridSpec(
    3, 2,
    figure=fig,
    height_ratios=[0.35, 1.85, 2.0],
    width_ratios=[1, 1.05],
    hspace=0.4,
    wspace=0.3,
    left=0.06,
    right=0.94,
    top=0.93,
    bottom=0.05
)

# ===================================
# TITLE
# ===================================
ax_title = fig.add_subplot(gs[0, :])
ax_title.axis('off')
ax_title.text(
    0.5, 0.5, 'Summary Dashboard',
    fontsize=30, fontweight='700',
    color='#252423',
    ha='center', va='center'
)

# ===================================
# PIE CHART - What Happened (CLEAN)
# ===================================
ax_pie = fig.add_subplot(gs[1, 0])
ax_pie.set_facecolor('white')

# Card styling
for spine in ax_pie.spines.values():
    spine.set_edgecolor('#E1E1E1')
    spine.set_linewidth(1.2)

w = merged.get("What Happened", pd.Series()).value_counts()

if len(w) > 0:
    # Power BI color palette
    pie_colors = ['#00B7C3', '#5C2E91', '#E81123', '#FFB900', '#00CC6A', '#8764B8']
    
    # Clean pie chart
    wedges, texts, autotexts = ax_pie.pie(
        w.values,
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        colors=pie_colors[:len(w)],
        textprops={'fontsize': 13, 'weight': 'bold', 'color': 'white'},
        pctdistance=0.78,
        wedgeprops={'edgecolor': 'white', 'linewidth': 3}
    )
    
    # Clean title
    ax_pie.text(
        0.02, 1.12, 'What Happened',
        transform=ax_pie.transAxes,
        fontsize=18, fontweight='600',
        color='#252423'
    )
    
    # Minimal legend
    legend_labels = [f'{label}: {count:,}' for label, count in zip(w.index, w.values)]
    ax_pie.legend(
        wedges, legend_labels,
        loc='upper center',
        bbox_to_anchor=(0.5, -0.08),
        fontsize=10.5,
        frameon=False,
        ncol=min(len(w), 2)
    )

# ===================================
# BAR CHART - Status (CLEAN & WORKING)
# ===================================
ax_bar = fig.add_subplot(gs[1, 1])
ax_bar.set_facecolor('white')

# Card styling
for spine in ax_bar.spines.values():
    spine.set_edgecolor('#E1E1E1')
    spine.set_linewidth(1.2)

# Get status data
order = ["closed", "open", "in progress", "review"]
sc = merged["Status_clean"].value_counts().reindex(order, fill_value=0)

# Clean colors
status_colors = {
    'closed': '#107C10',
    'open': '#E81123', 
    'in progress': '#FFB900',
    'review': '#0078D4'
}
colors_list = [status_colors[s] for s in order]

# Create bars
y_pos = np.arange(len(sc))
bars = ax_bar.barh(
    y_pos, sc.values,
    height=0.55,
    color=colors_list,
    edgecolor='white',
    linewidth=1.5
)

# Smart labels (FIXED for small values)
max_value = max(sc.values) if max(sc.values) > 0 else 1

for i, (bar, val) in enumerate(zip(bars, sc.values)):
    if val > 0:
        bar_width = bar.get_width()
        y_center = bar.get_y() + bar.get_height() / 2
        
        # If bar is small (less than 10% of max), label goes outside
        if bar_width < (max_value * 0.1):
            ax_bar.text(
                bar_width + (max_value * 0.02),
                y_center,
                f'{int(val):,}',
                va='center', ha='left',
                fontsize=12, fontweight='700',
                color='#252423'
            )
        else:
            # Label inside
            ax_bar.text(
                bar_width * 0.5,
                y_center,
                f'{int(val):,}',
                va='center', ha='center',
                fontsize=12, fontweight='700',
                color='white'
            )

# Clean axis
ax_bar.set_yticks(y_pos)
ax_bar.set_yticklabels(
    ['Closed', 'Open', 'In Progress', 'Review'],
    fontsize=12, color='#252423', fontweight='500'
)
ax_bar.invert_yaxis()
ax_bar.set_xlim(0, max_value * 1.15)

# Title
ax_bar.text(
    0.02, 1.12, 'Status Summary',
    transform=ax_bar.transAxes,
    fontsize=18, fontweight='600',
    color='#252423'
)

# Clean up
for spine in ['top', 'right', 'bottom', 'left']:
    ax_bar.spines[spine].set_visible(False)
ax_bar.tick_params(left=False, bottom=False)
ax_bar.set_xticks([])

# ===================================
# DONUT CHART - Severity (CLEAN, NO CENTER TEXT)
# ===================================
ax_donut = fig.add_subplot(gs[2, :])
ax_donut.set_facecolor('white')

# Card styling
for spine in ax_donut.spines.values():
    spine.set_edgecolor('#E1E1E1')
    spine.set_linewidth(1.2)

sev = merged.get("Severity", pd.Series()).value_counts()

if len(sev) > 0:
    # Order
    severity_order = ['High', 'Medium', 'Low']
    sev_ordered = sev.reindex(severity_order, fill_value=0)
    sev_ordered = sev_ordered[sev_ordered > 0]
    
    # Clean severity colors
    sev_color_map = {
        'High': '#D13438',
        'Medium': '#FFB900',
        'Low': '#00B7C3'
    }
    donut_colors = [sev_color_map[label] for label in sev_ordered.index]
    
    # Clean donut - NO CENTER TEXT
    wedges, texts = ax_donut.pie(
        sev_ordered.values,
        labels=None,
        startangle=90,
        colors=donut_colors,
        wedgeprops={'width': 0.38, 'edgecolor': 'white', 'linewidth': 4}
    )
    
    total = sev_ordered.sum()
    
    # Percentage labels outside
    for i, (wedge, label, count) in enumerate(zip(wedges, sev_ordered.index, sev_ordered.values)):
        angle = (wedge.theta1 + wedge.theta2) / 2
        pct = (count / total) * 100
        
        x = 1.28 * np.cos(np.radians(angle))
        y = 1.28 * np.sin(np.radians(angle))
        
        # Clean percentage box
        ax_donut.text(
            x, y, f'{pct:.1f}%',
            ha='center', va='center',
            fontsize=15, fontweight='700',
            color='#252423',
            bbox=dict(
                boxstyle='round,pad=0.4',
                facecolor='white',
                edgecolor=donut_colors[i],
                linewidth=2.2
            )
        )
    
    # White center (NO TEXT)
    center_circle = plt.Circle((0, 0), 0.62, fc='white', linewidth=0)
    ax_donut.add_artist(center_circle)
    
    # Title
    ax_donut.text(
        0.5, 1.06, 'Severity',
        transform=ax_donut.transAxes,
        fontsize=18, fontweight='600',
        color='#252423',
        ha='center'
    )
    
    # Clean legend
    legend_labels = [f'{label}: {count:,}' for label, count in zip(sev_ordered.index, sev_ordered.values)]
    legend = ax_donut.legend(
        wedges, legend_labels,
        loc='center left',
        bbox_to_anchor=(1.02, 0.5),
        fontsize=11.5,
        frameon=True,
        facecolor='white',
        edgecolor='#E1E1E1',
        framealpha=1
    )

# Save
plt.savefig(PAGE3_IMG, dpi=200, bbox_inches='tight',
           facecolor='#F8F8F8', edgecolor='none')
plt.close()
print(f"✓ Clean Power BI Dashboard saved: {PAGE3_IMG}")
# -------------------------
# PDF GENERATION
# -------------------------
PAGE_SIZE = landscape(A4)
left_margin = right_margin = 0.35 * inch
top_margin = 0.28 * inch
bottom_margin = 0.60 * inch

doc = SimpleDocTemplate(
    OUT_PDF, 
    pagesize=PAGE_SIZE,
    leftMargin=left_margin, 
    rightMargin=right_margin,
    topMargin=top_margin, 
    bottomMargin=bottom_margin
)

story = []

def add_border_logo_footer(canvas, doc):
    canvas.saveState()  # Save state ONCE at the start
    
    border_color = colors.HexColor(HEADER_HEX)

    # Border (left and right only - NO BOTTOM)
    canvas.setStrokeColor(border_color)
    canvas.setLineWidth(2)

    # Left border
    canvas.line(doc.leftMargin - 6, 
                doc.bottomMargin - 6,
                doc.leftMargin - 6,
                doc.height + doc.bottomMargin + 6)

    # Right border
    canvas.line(doc.leftMargin + doc.width + 6, 
                doc.bottomMargin - 6,
                doc.leftMargin + doc.width + 6,
                doc.height + doc.bottomMargin + 6)

# Footer bar - increased height
    footer_h = 28  # Increased from 20 to 28
    canvas.setFillColor(border_color)
    canvas.rect(doc.leftMargin - 6,
                doc.bottomMargin - 6,
                doc.width + 12,
                footer_h,
                fill=1,
                stroke=0)

    # Footer text - better vertical centering
    canvas.setFont("Helvetica-Bold", 12)  # Increased from 11 to 12
    canvas.setFillColor(colors.whitesmoke)
    canvas.drawCentredString(
        doc.leftMargin + doc.width / 2,
        doc.bottomMargin + 8,  # Increased from 3 to 8 for better centering
        "Created by Momentum"
    )

    canvas.restoreState()  # Restore state ONCE at the end

# Calculate usable width
usable_width = PAGE_SIZE[0] - left_margin - right_margin
gutter = 0.25 * inch
table_width_each = (usable_width - gutter) / 2.0

# Column widths
col_widths = [
    1.65 * inch,  # Employee Name
    0.78 * inch,  # Total Observations
    0.58 * inch,  # Total Open
    0.68 * inch,  # Total In Progress  
    0.55 * inch,  # Total Review
    0.62 * inch   # Total Closed
]

total_col_width = sum(col_widths)
if total_col_width > table_width_each:
    scale_factor = (table_width_each / total_col_width) * 0.96
    col_widths = [w * scale_factor for w in col_widths]

# Rows per page
rows_per_column = 14
rows_per_page = rows_per_column * 2

# Wrap style
wrap_style = ParagraphStyle("wrap", fontSize=7.5, leading=9, fontName="Helvetica")

# -----------------------------------------------
# HEADER FUNCTION WITH LOGO
# -----------------------------------------------
def make_header_with_logo(title_text):
    """Create header with title and logo"""
    header = Table(
        [
            [
                Paragraph(
                    f"<b>{title_text}</b>",
                    ParagraphStyle(
                        name="header_title",
                        fontSize=16,
                        textColor=colors.white,
                        alignment=1,
                        fontName="Helvetica-Bold"
                    )
                ),
                Image(LOGO_PATH, width=75, height=28)
            ]
        ],
        colWidths=[usable_width - 85, 85]
    )

    header.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor(HEADER_HEX)),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (0,0), (0,0), "CENTER"),
        ("ALIGN", (1,0), (1,0), "RIGHT"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))

    return header

# -----------------------------------------------
# BUILD EMPLOYEE PAGES
# -----------------------------------------------
i = 0
page_no = 1
total_employees = len(rows)

while i < total_employees:
    if page_no > 1:
        story.append(PageBreak())

    # Add header with logo
    header = make_header_with_logo("MiSafe Logged Details From 01st March to 23rd Nov 2025")
    story.append(header)
    story.append(Spacer(1, 0.18 * inch))
    
    # KPI boxes on first page only
    if page_no == 1:
        kpi_vals = [
            total_sum["Total_Observations"],
            total_sum["Total_Open"],
            total_sum["Total_InProgress"],
            total_sum["Total_Review"],
            total_sum["Total_Closed"]
        ]
        
        kpi_labels = ["Total Observations", "Open", "In Progress", "Review", "Closed"]
        kpi_box_width = usable_width / 5.0
        
        kpi_data = []
        kpi_row = []
        for val, label in zip(kpi_vals, kpi_labels):
            val_style = ParagraphStyle("kpi_val", fontSize=20, fontName="Helvetica-Bold", alignment=1)
            lbl_style = ParagraphStyle("kpi_lbl", fontSize=8.5, fontName="Helvetica", alignment=1)
            
            box = Table(
                [[Paragraph(f"<b>{val}</b>", val_style)],
                 [Paragraph(label, lbl_style)]],
                colWidths=[kpi_box_width * 0.95],
                rowHeights=[35, 25]  # Fixed heights: 35 for number, 25 for label
            )
            box.setStyle(TableStyle([
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("VALIGN", (0,0), (0,0), "TOP"),      # Value aligned to TOP
                ("VALIGN", (0,1), (0,1), "BOTTOM"),   # Label aligned to BOTTOM
                ("TOPPADDING", (0,0), (0,0), 8),      # Less padding on top of number
                ("BOTTOMPADDING", (0,0), (0,0), 0),   # No padding below number
                ("TOPPADDING", (0,1), (0,1), 0),      # No padding above label
                ("BOTTOMPADDING", (0,1), (0,1), 8),   # More padding below label
                ("BOX", (0,0), (-1,-1), 1, colors.grey)
            ]))
            kpi_row.append(box)
        
        kpi_table = Table([kpi_row], colWidths=[kpi_box_width] * 5)
        kpi_table.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE")
        ]))
        story.append(kpi_table)
        story.append(Spacer(1, 0.18 * inch))
    
    # Get row chunks for this page
    chunk = rows[i:i+rows_per_page]
    left_chunk = chunk[:rows_per_column]
    right_chunk = chunk[rows_per_column:rows_per_column*2]
    
    # Table headers
    tbl_header = [
        "Employee Name", 
        "Total\nObservations", 
        "Total\nOpen", 
        "Total In\nProgress", 
        "Total\nReview", 
        "Total\nClosed"
    ]
    
    def prepare_table_data(chunk_rows):
        out = [tbl_header]
        for r in chunk_rows:
            name_wrapped = Paragraph(str(r[0]), wrap_style)
            out.append([name_wrapped, r[1], r[2], r[3], r[4], r[5]])
        
        if chunk_rows:
            tot_obs = sum([r[1] for r in chunk_rows])
            tot_open = sum([r[2] for r in chunk_rows])
            tot_inp = sum([r[3] for r in chunk_rows])
            tot_rev = sum([r[4] for r in chunk_rows])
            tot_closed = sum([r[5] for r in chunk_rows])
            total_para = Paragraph("<b>Total</b>", wrap_style)
            out.append([total_para, tot_obs, tot_open, tot_inp, tot_rev, tot_closed])
        return out
    
    left_data = prepare_table_data(left_chunk)
    right_data = prepare_table_data(right_chunk) if right_chunk else []
    
    # Create tables
    base_table_style = TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor(HEADER_HEX)),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 7.5),
        ("GRID", (0,0), (-1,-1), 0.4, colors.grey),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (1,0), (-1,-1), "CENTER"),
        ("ALIGN", (0,1), (0,-1), "LEFT"),
        ("FONTSIZE", (0,1), (-1,-1), 7.5),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("LEFTPADDING", (0,0), (-1,-1), 2.5),
        ("RIGHTPADDING", (0,0), (-1,-1), 2.5),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ])
    
    left_table = Table(left_data, colWidths=col_widths, repeatRows=1)
    left_table.setStyle(base_table_style)
    
    if len(left_data) > 1:
        total_row_idx = len(left_data) - 1
        left_table.setStyle(TableStyle([
            ("BACKGROUND", (0, total_row_idx), (-1, total_row_idx), colors.Color(1, 0.97, 0.7)),
            ("FONTNAME", (0, total_row_idx), (-1, total_row_idx), "Helvetica-Bold")
        ]))
    
    right_table = None
    if right_data:
        right_table = Table(right_data, colWidths=col_widths, repeatRows=1)
        right_table.setStyle(base_table_style)
        if len(right_data) > 1:
            total_row_idx = len(right_data) - 1
            right_table.setStyle(TableStyle([
                ("BACKGROUND", (0, total_row_idx), (-1, total_row_idx), colors.Color(1, 0.97, 0.7)),
                ("FONTNAME", (0, total_row_idx), (-1, total_row_idx), "Helvetica-Bold")
            ]))
    
    if right_table:
        combined = Table(
            [[left_table, Spacer(gutter, 0), right_table]], 
            colWidths=[table_width_each, gutter, table_width_each]
        )
        combined.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP")]))
        story.append(combined)
    else:
        story.append(left_table)
    
    story.append(Spacer(1, 0.15 * inch))
    
    i += rows_per_page
    page_no += 1

# Add chart pages with headers

story.append(PageBreak())
chart_header_2a = make_header_with_logo("Dashboard")
story.append(chart_header_2a)
story.append(Spacer(1, 0.15 * inch))
story.append(Image(PAGE2A_IMG, width=10.2*inch, height=5.5*inch))
story.append(Spacer(1, 0.25 * inch))  # Added spacer before footer

story.append(PageBreak())
chart_header_2b = make_header_with_logo("Dashboard")
story.append(chart_header_2b)
story.append(Spacer(1, 0.15 * inch))
story.append(Image(PAGE2B_IMG, width=10.2*inch, height=5.5*inch))
story.append(Spacer(1, 0.25 * inch))  # Added spacer before footer

story.append(PageBreak())
chart_header_3 = make_header_with_logo("Dashboard")
story.append(chart_header_3)
story.append(Spacer(1, 0.15 * inch))
story.append(Image(PAGE3_IMG, width=10*inch, height=4.8*inch))
story.append(Spacer(1, 0.3 * inch))

# -----------------------------------------------
# AREA-WISE PAGES WITH PROPER PAGINATION AND LOGO
# -----------------------------------------------
# -----------------------------------------------
# AREA-WISE PAGES WITH CONSISTENT ROW COUNT
# -----------------------------------------------
if merged_area_col:
    ALL_AREAS = sorted(merged[merged_area_col].dropna().unique())
else:
    ALL_AREAS = []

# Area detail column widths - ADJUSTED for better fit
col_width_area = [2.6*inch, 1.1*inch, 0.75*inch, 0.95*inch, 1.5*inch, 1.4*inch, 0.65*inch, 0.6*inch]

# CONSISTENT rows per page for all areas
ROWS_PER_AREA_PAGE = 16  # Same for all pages

for area in ALL_AREAS:
    area_df = merged[(merged.get(merged_area_col,"")==area) & (merged["Status_clean"]=="open")].copy()
    if area_df.empty:
        continue
    
    # Prepare columns and data
    cols = ["Description", "What Happened", "Severity", "Logged by", "Area Name", "Location", "Status", "Aging"]
    cols = [c for c in cols if c in area_df.columns]
    
    # Adjust column widths based on available columns
    col_width_area_adjusted = col_width_area[:len(cols)]
    
    # Prepare all rows
    all_rows = []
    for _, r in area_df.iterrows():
        row = [Paragraph(str(r[c]), ParagraphStyle("wrap", fontSize=7, leading=8.5)) for c in cols]
        all_rows.append(row)
    
    # Count total rows
    total_rows = len(all_rows)
    
    # Calculate number of pages needed
    if total_rows <= ROWS_PER_AREA_PAGE:
        # Small area: single page with actual row count
        page_count = 1
    else:
        # Large area: multiple pages with consistent 18 rows each
        page_count = math.ceil(total_rows / ROWS_PER_AREA_PAGE)
    
    # Generate pages
    for page_idx in range(page_count):
        story.append(PageBreak())
        
        
        area_title = f"{area}"
 
        
        # Create paragraph style for area header
        area_header_style = ParagraphStyle(
            name="area_header",
            fontSize=13,
            textColor=colors.white,
            alignment=1,
            fontName="Helvetica-Bold"
        )
        
        area_header = Table(
            [
                [
                    Paragraph(f"<b>{area_title}</b>", area_header_style),
                    Image(LOGO_PATH, width=70, height=25)
                ]
            ],
            colWidths=[usable_width - 80, 80]
        )

        area_header.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), colors.HexColor(HEADER_HEX)),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("ALIGN", (0,0), (0,0), "CENTER"),
            ("ALIGN", (1,0), (1,0), "RIGHT"),
            ("TOPPADDING", (0,0), (-1,-1), 8),
            ("BOTTOMPADDING", (0,0), (-1,-1), 8),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ]))

        story.append(area_header)
        story.append(Spacer(1, 0.15*inch))
        
        # Get rows for this page
        start_idx = page_idx * ROWS_PER_AREA_PAGE
        end_idx = min(start_idx + ROWS_PER_AREA_PAGE, total_rows)
        page_rows = all_rows[start_idx:end_idx]
        
        # Build table with header
        data = [cols] + page_rows
        
        t = Table(data, colWidths=col_width_area_adjusted, repeatRows=1)
        
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor(HEADER_HEX)),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
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
        
        # Add spacer before footer - IMPORTANT for preventing overlap
        if end_idx < total_rows:  # More pages coming
            story.append(Spacer(1, 0.2 * inch))
        else:  # Last page
            story.append(Spacer(1, 0.25 * inch))

# Build PDF
doc.build(story, onFirstPage=add_border_logo_footer, onLaterPages=add_border_logo_footer)
print("\n✓ PDF CREATED SUCCESSFULLY:", OUT_PDF)
print(f"✓ Total employees: {total_employees}")
print(f"✓ Total observations: {total_sum['Total_Observations']}")