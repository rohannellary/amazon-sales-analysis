"""
Amazon Sales Data Analysis — Project ID: 78G0OL
================================================
Run:  python amazon_sales_analysis.py
Output: 12 PNG charts + printed summary in the terminal

Tech Stack:
    - Python 3.x
    - Pandas     — data loading, cleaning, aggregation
    - Matplotlib — chart rendering
    - Seaborn    — statistical visualizations & heatmaps
    - NumPy      — numerical operations
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. LOAD & CLEAN DATA
# ─────────────────────────────────────────────
CSV_PATH = "Amazon Sale Report.csv"

df = pd.read_csv(CSV_PATH, encoding='latin1')
df['Date']   = pd.to_datetime(df['Date'], format='%m-%d-%y', errors='coerce')
df['Month']  = df['Date'].dt.to_period('M')
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
df['Qty']    = pd.to_numeric(df['Qty'],    errors='coerce')

shipped = df[df['Status'].str.startswith('Shipped', na=False)].copy()

# ─────────────────────────────────────────────
# 2. KEY METRICS SUMMARY
# ─────────────────────────────────────────────
total_orders   = len(df)
shipped_orders = len(shipped)
cancelled      = (df['Status'] == 'Cancelled').sum()
total_revenue  = shipped['Amount'].sum()
avg_order_val  = shipped['Amount'].mean()
cancel_rate    = cancelled / total_orders * 100

print("=" * 50)
print("  AMAZON SALES ANALYSIS — KEY METRICS")
print("=" * 50)
print(f"  Total Orders      : {total_orders:,}")
print(f"  Shipped Orders    : {shipped_orders:,}")
print(f"  Cancelled Orders  : {cancelled:,}  ({cancel_rate:.1f}%)")
print(f"  Total Revenue     : ₹{total_revenue/1e6:.2f}M")
print(f"  Avg Order Value   : ₹{avg_order_val:.0f}")
print("=" * 50)

# ─────────────────────────────────────────────
# 3. SETUP
# ─────────────────────────────────────────────
PALETTE = ['#FF9900','#232F3E','#37475A','#FF6D00','#00A8E1',
           '#6DB33F','#E91E63','#9C27B0','#009688']
sns.set_theme(style='whitegrid', font_scale=1.05)

def save(name):
    plt.tight_layout()
    plt.savefig(f"{name}.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved → {name}.png")

# ─────────────────────────────────────────────
# FIG 1 — Monthly Revenue Trend
# ─────────────────────────────────────────────
monthly = shipped.groupby('Month')['Amount'].sum().reset_index()
monthly['Month_str'] = monthly['Month'].astype(str)

fig, ax = plt.subplots(figsize=(12, 5))
ax.fill_between(monthly['Month_str'], monthly['Amount'] / 1e6, alpha=0.18, color='#FF9900')
ax.plot(monthly['Month_str'], monthly['Amount'] / 1e6,
        marker='o', color='#FF9900', lw=2.5, ms=7)
for _, row in monthly.iterrows():
    ax.annotate(f"₹{row['Amount']/1e6:.1f}M",
                (row['Month_str'], row['Amount'] / 1e6),
                textcoords='offset points', xytext=(0, 10), ha='center', fontsize=9)
ax.set_title('Monthly Revenue Trend (Shipped Orders)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Month'); ax.set_ylabel('Revenue (₹ Millions)')
plt.xticks(rotation=30)
save("fig1_monthly_revenue")

# ─────────────────────────────────────────────
# FIG 2 — Category Revenue & Volume
# ─────────────────────────────────────────────
cat_rev = shipped.groupby('Category')['Amount'].sum().sort_values(ascending=False)
cat_qty = shipped.groupby('Category')['Qty'].sum().sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
bars = axes[0].bar(cat_rev.index, cat_rev.values / 1e6,
                   color=PALETTE[:len(cat_rev)], edgecolor='white')
axes[0].bar_label(bars, fmt='₹%.1fM', padding=3, fontsize=8.5)
axes[0].set_title('Revenue by Category', fontweight='bold')
axes[0].set_ylabel('Revenue (₹ Millions)')
axes[0].tick_params(axis='x', rotation=30)

bars2 = axes[1].bar(cat_qty.index, cat_qty.values,
                    color=PALETTE[:len(cat_qty)], edgecolor='white')
axes[1].bar_label(bars2, fmt='%d', padding=3, fontsize=8.5)
axes[1].set_title('Units Sold by Category', fontweight='bold')
axes[1].set_ylabel('Total Units')
axes[1].tick_params(axis='x', rotation=30)

plt.suptitle('Product Category Performance', fontsize=14, fontweight='bold', y=1.02)
save("fig2_category_performance")

# ─────────────────────────────────────────────
# FIG 3 — Order Status Distribution
# ─────────────────────────────────────────────
status_counts = df['Status'].value_counts()
colors_pie = ['#6DB33F','#FF9900','#E91E63','#9C27B0','#37475A',
              '#00A8E1','#FF6D00','#009688','#795548','#607D8B','#F44336','#FFC107','#03A9F4']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    status_counts.values, labels=None,
    autopct=lambda p: f'{p:.1f}%' if p > 2 else '',
    startangle=140, colors=colors_pie[:len(status_counts)],
    pctdistance=0.78, wedgeprops=dict(edgecolor='white', linewidth=1.2))
for at in autotexts:
    at.set_fontsize(8)
ax.legend(wedges,
          [f"{s} ({n:,})" for s, n in zip(status_counts.index, status_counts.values)],
          loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=9)
ax.set_title('Order Status Distribution', fontsize=14, fontweight='bold')
save("fig3_order_status")

# ─────────────────────────────────────────────
# FIG 4 — Fulfillment Method
# ─────────────────────────────────────────────
ful   = df['Fulfilment'].value_counts()
total = ful.sum()

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(ful.index, ful.values, color=['#FF9900', '#232F3E'], width=0.45, edgecolor='white')
ax.bar_label(bars, fmt='%d', padding=4, fontsize=11, fontweight='bold')
ax.set_title('Orders by Fulfilment Method', fontsize=13, fontweight='bold')
ax.set_ylabel('Number of Orders')
for bar, val in zip(bars, ful.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2,
            f'{val / total * 100:.1f}%', ha='center', va='center',
            color='white', fontsize=12, fontweight='bold')
save("fig4_fulfilment")

# ─────────────────────────────────────────────
# FIG 5 — Top 10 States by Revenue
# ─────────────────────────────────────────────
state_rev = shipped.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(11, 5))
colors_grad = sns.color_palette('YlOrRd', len(state_rev))[::-1]
bars = ax.barh(state_rev.index[::-1], state_rev.values[::-1] / 1e6,
               color=colors_grad, edgecolor='white')
ax.bar_label(bars, fmt='₹%.2fM', padding=4, fontsize=9)
ax.set_title('Top 10 States by Revenue (Shipped Orders)', fontsize=13, fontweight='bold')
ax.set_xlabel('Revenue (₹ Millions)')
save("fig5_top_states")

# ─────────────────────────────────────────────
# FIG 6 — Size Distribution
# ─────────────────────────────────────────────
size_order  = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL', '6XL', 'Free']
size_counts = shipped['Size'].value_counts()
size_counts = size_counts.reindex([s for s in size_order if s in size_counts.index]).dropna()

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(size_counts.index, size_counts.values,
              color=sns.color_palette('Blues_d', len(size_counts)), edgecolor='white')
ax.bar_label(bars, fmt='%d', padding=3, fontsize=9)
ax.set_title('Units Sold by Size', fontsize=13, fontweight='bold')
ax.set_ylabel('Units Sold')
save("fig6_size_distribution")

# ─────────────────────────────────────────────
# FIG 7 — B2B vs B2C
# ─────────────────────────────────────────────
b2b        = df['B2B'].value_counts()
labels_b2b = {True: 'B2B', False: 'B2C'}

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar([labels_b2b[k] for k in b2b.index], b2b.values,
              color=['#00A8E1', '#FF9900'], width=0.4, edgecolor='white')
ax.bar_label(bars, fmt='%d', padding=4, fontsize=11, fontweight='bold')
ax.set_title('B2B vs B2C Order Split', fontsize=13, fontweight='bold')
ax.set_ylabel('Number of Orders')
for bar, val in zip(bars, b2b.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2,
            f'{val / b2b.sum() * 100:.1f}%', ha='center', va='center',
            color='white', fontsize=12, fontweight='bold')
save("fig7_b2b_b2c")

# ─────────────────────────────────────────────
# FIG 8 — Revenue Heatmap: Category × Month
# ─────────────────────────────────────────────
pivot = shipped.groupby(['Category', 'Month'])['Amount'].sum().unstack(fill_value=0)
pivot.columns = [str(c) for c in pivot.columns]

fig, ax = plt.subplots(figsize=(14, 5))
sns.heatmap(pivot / 1e3, annot=True, fmt='.0f', cmap='YlOrRd',
            linewidths=0.4, linecolor='white', ax=ax,
            cbar_kws={'label': 'Revenue (₹ Thousands)'})
ax.set_title('Revenue Heatmap: Category × Month (₹ Thousands)', fontsize=13, fontweight='bold')
ax.set_xlabel('Month'); ax.set_ylabel('Category')
plt.xticks(rotation=30)
save("fig8_heatmap")

# ─────────────────────────────────────────────
# FIG 9 — Order Amount Distribution
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5))
ax.hist(shipped['Amount'].dropna(), bins=60, color='#FF9900', edgecolor='white', alpha=0.85)
ax.axvline(shipped['Amount'].mean(),   color='#232F3E', lw=2, linestyle='--',
           label=f"Mean ₹{shipped['Amount'].mean():.0f}")
ax.axvline(shipped['Amount'].median(), color='#E91E63', lw=2, linestyle='--',
           label=f"Median ₹{shipped['Amount'].median():.0f}")
ax.set_title('Order Amount Distribution', fontsize=14, fontweight='bold')
ax.set_xlabel('Order Amount (₹)')
ax.set_ylabel('Number of Orders')
ax.legend(fontsize=11)
save("fig9_price_distribution")

# ─────────────────────────────────────────────
# FIG 10 — Cancellation Rate by Category
# ─────────────────────────────────────────────
cat_total       = df.groupby('Category').size()
cat_cancelled   = df[df['Status'] == 'Cancelled'].groupby('Category').size()
cancel_rate_cat = (cat_cancelled / cat_total * 100).sort_values(ascending=False).dropna()

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(cancel_rate_cat.index, cancel_rate_cat.values,
              color=sns.color_palette('Reds_d', len(cancel_rate_cat)), edgecolor='white')
ax.bar_label(bars, fmt='%.1f%%', padding=3, fontsize=10)
ax.axhline(cancel_rate_cat.mean(), color='#232F3E', lw=1.8, linestyle='--',
           label=f'Avg {cancel_rate_cat.mean():.1f}%')
ax.set_title('Cancellation Rate by Category', fontsize=14, fontweight='bold')
ax.set_ylabel('Cancellation Rate (%)')
ax.tick_params(axis='x', rotation=20)
ax.legend()
save("fig10_cancellation_by_category")

# ─────────────────────────────────────────────
# FIG 11 — Top 10 Cities by Revenue
# ─────────────────────────────────────────────
city_rev = shipped.groupby('ship-city')['Amount'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(11, 5))
colors_grad = sns.color_palette('YlOrRd', len(city_rev))[::-1]
bars = ax.barh(city_rev.index[::-1], city_rev.values[::-1] / 1e6,
               color=colors_grad, edgecolor='white')
ax.bar_label(bars, fmt='₹%.2fM', padding=4, fontsize=9)
ax.set_title('Top 10 Cities by Revenue (Shipped Orders)', fontsize=13, fontweight='bold')
ax.set_xlabel('Revenue (₹ Millions)')
save("fig11_top_cities")

# ─────────────────────────────────────────────
# FIG 12 — Customer Segmentation by Order Value
# ─────────────────────────────────────────────
bins       = [0, 300, 600, 1000, 6000]
seg_labels = ['Budget\n(₹0–300)', 'Mid-Range\n(₹301–600)',
              'Premium\n(₹601–1000)', 'High-Value\n(₹1000+)']
shipped['Segment'] = pd.cut(shipped['Amount'], bins=bins, labels=seg_labels)

seg_counts = shipped['Segment'].value_counts().reindex(seg_labels)
seg_rev    = shipped.groupby('Segment', observed=True)['Amount'].sum().reindex(seg_labels)
seg_colors = ['#00A8E1','#FF9900','#6DB33F','#E91E63']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

bars = axes[0].bar(seg_labels, seg_counts.values, color=seg_colors, edgecolor='white')
axes[0].bar_label(bars, fmt='%d', padding=3, fontsize=9)
axes[0].set_title('Customer Segments — Order Count', fontweight='bold')
axes[0].set_ylabel('Number of Orders')

bars2 = axes[1].bar(seg_labels, seg_rev.values / 1e6, color=seg_colors, edgecolor='white')
axes[1].bar_label(bars2, fmt='₹%.1fM', padding=3, fontsize=9)
axes[1].set_title('Customer Segments — Revenue Contribution', fontweight='bold')
axes[1].set_ylabel('Revenue (₹ Millions)')

plt.suptitle('Customer Segmentation by Order Value', fontsize=14, fontweight='bold', y=1.02)
save("fig12_customer_segmentation")

print(f"\nAll 12 charts saved. Analysis complete!")
