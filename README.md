# Amazon Sales Data Analysis
**Project ID:** 78G0OL | **Internship:** InnoByte Services

## Overview
A comprehensive analysis of Amazon India sales data covering 128,976 orders across April–June 2022. The project extracts actionable business insights on sales trends, product performance, customer behavior, and geographical distribution.

## Key Findings
- 📦 **128,976 total orders** | ₹71.05M in shipped revenue
- 🏆 **T-shirts** dominate with ~50% of total revenue (₹35.4M)
- ⚠️ **14.2% cancellation rate** — biggest area for improvement
- 📍 **Maharashtra** is the #1 state (₹12.13M revenue)
- 🚚 **69.6% orders** fulfilled by Amazon (FBA)
- 👥 **99.3% B2C** orders — B2B is an untapped opportunity
- 💰 **Premium segment (₹601–₹1,000)** generates the highest revenue at ₹32.65M

## Charts Generated (12 total)
| # | Chart | Objective Covered |
|---|---|---|
| 1 | Monthly Revenue Trend | Sales Overview |
| 2 | Category Revenue & Volume | Product Analysis |
| 3 | Order Status Distribution | Sales Overview |
| 4 | Fulfillment Method | Fulfillment Analysis |
| 5 | Top 10 States by Revenue | Geographical Analysis |
| 6 | Size Distribution | Product Analysis |
| 7 | B2B vs B2C Split | Customer Segmentation |
| 8 | Revenue Heatmap (Category × Month) | Product + Sales Overview |
| 9 | Order Amount Distribution | Customer Segmentation |
| 10 | Cancellation Rate by Category | Fulfillment + Product Analysis |
| 11 | Top 10 Cities by Revenue | Geographical Analysis |
| 12 | Customer Segmentation by Order Value | Customer Segmentation |

## Tech Stack
| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| Pandas | Data loading, cleaning, aggregation |
| Matplotlib | Chart rendering |
| Seaborn | Statistical visualizations & heatmaps |
| NumPy | Numerical operations |

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/rohannellary/amazon-sales-analysis.git
cd amazon-sales-analysis
```

**2. Install dependencies**
```bash
pip install pandas matplotlib seaborn numpy
```

**3. Add the dataset**
Place `Amazon Sale Report.csv` in the project root folder.

**4. Run the analysis**
```bash
python amazon_sales_analysis.py
```
All 12 charts will be saved inside the `figures/` folder automatically.

## Project Structure
```
amazon-sales-analysis/
│
├── amazon_sales_analysis.py          # Main analysis script
├── Amazon Sale Report.csv            # Dataset
├── Amazon_Sales_Analysis_Report.md   # Full written report
├── README.md                         # This file
├── .gitignore                        # Git ignore rules
│
└── figures/                          # All 12 generated charts
    ├── fig1_monthly_revenue.png
    ├── fig2_category_performance.png
    ├── fig3_order_status.png
    ├── fig4_fulfilment.png
    ├── fig5_top_states.png
    ├── fig6_size_distribution.png
    ├── fig7_b2b_b2c.png
    ├── fig8_heatmap.png
    ├── fig9_price_distribution.png
    ├── fig10_cancellation_by_category.png
    ├── fig11_top_cities.png
    └── fig12_customer_segmentation.png
```

## Top Recommendations
1. **Reduce cancellation rate** from 14.2% to under 7% — recover ~₹11.9M in lost revenue
2. **Stock M, L, XL heavily** — these sizes drive the majority of volume
3. **Launch B2B program** — currently only 0.7% of orders, huge untapped potential
4. **Target Tier-2 cities** — Mumbai & Bengaluru dominate; expand to Pune, Jaipur, Lucknow
5. **Cross-sell accessories** — Wallets, Watches, Socks are under-monetized
6. **Focus on Premium segment** — ₹601–₹1,000 orders generate the most revenue (₹32.65M)

---
*Submitted as part of InnoByte Services Data Analytics Internship — Project ID: 78G0OL*
