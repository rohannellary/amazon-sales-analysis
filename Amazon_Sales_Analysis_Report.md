# Amazon Sales Data Analysis Report
**Project ID:** 78G0OL  
**Dataset:** Amazon_Sale_Report_1_.csv — 128,976 orders  
**Period Covered:** April 2022 – June 2022  
**Analyst:** Data Analytics Intern Project

---

## Executive Summary

This report presents a comprehensive analysis of Amazon India sales data covering ~3 months of transactions. The dataset contains **128,976 orders** across 9 product categories, spanning 69 Indian states/territories. Total shipped revenue stands at **₹71.05 Million**, with an average order value of ₹649. Key takeaways include strong dominance of T-shirts, Maharashtra as the top revenue state, a 14.2% cancellation rate, and nearly 70% Amazon-fulfilled orders — all of which point to clear areas for optimization.

---

## 1. Sales Overview

| Metric | Value |
|---|---|
| Total Orders | 1,28,976 |
| Shipped Orders | 1,09,695 |
| Cancelled Orders | 18,334 (14.2%) |
| Total Shipped Revenue | ₹71.05 Million |
| Average Order Value | ₹649 |
| Period | Apr 2022 – Jun 2022 |

### Monthly Revenue Trend (Figure 1)

Revenue shows a fluctuating trend across the three months. The data captures what appears to be a peak mid-period followed by a slight decline. This is consistent with seasonal demand patterns in fashion e-commerce.

**Key Insight:** Month-on-month revenue changes should be tracked to anticipate inventory needs. If a declining trend persists beyond June 2022, promotional campaigns should be activated proactively.

---

## 2. Product Analysis

### Category Performance (Figure 2)

| Category | Revenue | Units Sold |
|---|---|---|
| T-shirt | ₹35.4M | ~55,000+ |
| Shirt | ₹20.1M | ~35,000+ |
| Blazzer | ₹5.5M | ~5,000+ |
| Trousers | ₹4.2M | ~4,500+ |
| Perfume | ₹2.1M | ~2,000+ |
| Socks | ₹1.3M | ~8,000+ |
| Shoes | ₹1.1M | ~1,200+ |
| Wallet | ₹0.9M | ~1,000+ |
| Watch | ₹0.5M | ~600+ |

T-shirts alone account for nearly **50% of total revenue**, making them the single most critical category. Shirts come second with ~28% share. Together, these two apparel categories drive ~78% of all revenue.

**Key Insight:** The business is heavily concentrated in basic apparel. Accessories (Wallet, Watch, Socks) are under-monetized relative to their unit volumes and represent upsell/cross-sell opportunities.

### Size Distribution (Figure 6)

M and L are the most popular sizes, followed by XL. Sizes like 5XL and 6XL see minimal demand.

**Key Insight:** Inventory should be stocked heavily in M, L, and XL. Overstocking 4XL–6XL leads to capital lock-up. Consider size-inclusive bundles for slower-moving large sizes.

---

## 3. Fulfillment Analysis

### Fulfillment Method (Figure 4)

| Method | Orders | Share |
|---|---|---|
| Amazon Fulfilled | 89,713 | 69.6% |
| Merchant Fulfilled | 39,263 | 30.4% |

Amazon's fulfillment (FBA) dominates, which is a positive indicator since FBA orders typically have higher delivery success rates and customer trust.

### Order Status Breakdown (Figure 3)

- **Shipped – Delivered to Buyer:** the majority of shipped orders ✅  
- **Cancelled:** 18,334 orders (14.2%) — the biggest concern area  
- **Returned / Rejected / Lost:** small but impactful on seller metrics and revenue recovery  

**Key Insight:** The 14.2% cancellation rate is significantly above the ~5% industry benchmark. Investigating the root cause (stock-outs, pricing issues, payment failures) is a high-priority action item. Each cancelled order at ₹649 average represents roughly **₹11.9M in lost revenue**.

---

## 4. Customer Segmentation

### B2B vs B2C (Figure 7)

| Segment | Orders | Share |
|---|---|---|
| B2C (Individual) | 1,28,104 | 99.3% |
| B2B (Business) | 872 | 0.7% |

The business is overwhelmingly B2C. However, B2B orders, while few, tend to be higher-value bulk purchases.

**Key Insight:** A dedicated B2B outreach program (corporate gifting, uniform supply) could unlock a high-margin, low-acquisition-cost revenue stream with very little incremental effort.

---

## 5. Geographical Analysis

### Top 10 States by Revenue (Figure 5)

| Rank | State | Revenue |
|---|---|---|
| 1 | Maharashtra | ₹12.13M |
| 2 | Karnataka | ₹10.2M+ |
| 3 | Telangana | ₹7.5M+ |
| 4 | Tamil Nadu | ₹6.8M+ |
| 5 | Uttar Pradesh | ₹5.5M+ |
| 6–10 | Delhi, Gujarat, Rajasthan, Andhra Pradesh, West Bengal | ₹2M–₹4M range |

Maharashtra and Karnataka (Mumbai + Bengaluru metros) together account for a disproportionate share of revenue, reflecting strong urban e-commerce adoption.

**Key Insight:** Tier-1 metros dominate. Tier-2 cities (Pune, Jaipur, Lucknow, Hyderabad) show organic demand and should be targeted with regional promotions and faster delivery promise to grow their share.

### Revenue Heatmap: Category × Month (Figure 8)

The heatmap reveals that T-shirts and Shirts are consistently strong across all months. Blazzers show a concentration in specific months, suggesting seasonal demand.

**Key Insight:** Plan category-specific promotions aligned with demand seasons (e.g., Blazzer push pre-winter months, Perfume push around festivals).

---

## 6. Business Insights & Recommendations

### 🔴 Critical Actions

1. **Reduce Cancellation Rate (14.2% → below 7%):** Audit cancellation reasons. Likely culprits: incorrect stock listings, payment gateway failures, or delayed dispatch. Implement real-time inventory sync and pre-payment validation.

2. **Concentrate inventory in M, L, XL:** These sizes drive the majority of volume. Slow-moving sizes (4XL+) should move to demand-based replenishment.

### 🟡 Growth Opportunities

3. **Upsell Accessories with Apparel:** Socks/Wallets/Watches have brand presence but low revenue. Bundle them as "Complete the Look" with T-shirt/Shirt purchases.

4. **Expand Amazon FBA coverage:** Merchant-fulfilled orders (30%) likely have higher cancellation and return rates. Migrating more SKUs to FBA can improve delivery SLA and customer satisfaction scores.

5. **Launch B2B program:** Target corporate clients, schools, and event organizers for bulk uniform/merchandise orders. Even 5% B2B penetration could add ₹3.5M+ in high-margin revenue.

### 🟢 Regional Strategy

6. **Deepen in Top-5 States:** Maharashtra and Karnataka collectively drive ~30%+ of revenue. Localized ad spend (regional language creatives) and fast delivery programs (same-day in Mumbai/Bengaluru) can increase wallet share.

7. **Penetrate Tier-2 Cities:** States like Rajasthan, Madhya Pradesh, and Bihar show demand but under-serve. Partner with regional delivery networks to improve delivery SLA and build brand presence.

### 📊 Operational Improvements

8. **Seasonal inventory planning:** Use the Category × Month heatmap to plan SKU-level stock 45 days ahead of demand peaks (e.g., winter blazzers in September, festival perfumes in October).

9. **Return rate tracking:** While not fully captured in this dataset, adding return analytics will help identify defective product batches or sizing issues early.

---

## 7. Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| Pandas | Data loading, cleaning, aggregation |
| Matplotlib | Chart rendering |
| Seaborn | Statistical visualizations & heatmaps |
| NumPy | Numerical operations |

---

## 8. Files Delivered

| File | Description |
|---|---|
| `amazon_sales_analysis.py` | Full Python source code (run to regenerate all charts) |
| `fig1_monthly_revenue.png` | Monthly revenue trend |
| `fig2_category_performance.png` | Category revenue + units |
| `fig3_order_status.png` | Order status pie chart |
| `fig4_fulfilment.png` | Amazon vs Merchant fulfillment |
| `fig5_top_states.png` | Top 10 states by revenue |
| `fig6_size_distribution.png` | Size-wise units sold |
| `fig7_b2b_b2c.png` | B2B vs B2C split |
| `fig8_heatmap.png` | Category × Month revenue heatmap |
| `Amazon_Sales_Analysis_Report.md` | This report |

---

## Conclusion

The Amazon India sales data reveals a business with strong fundamentals — ₹71M in shipped revenue, healthy order volumes, and clear category leaders. The two highest-priority improvements are reducing the 14.2% cancellation rate (immediate revenue recovery) and diversifying beyond T-shirts/Shirts to reduce single-category concentration risk. Geographic and B2B expansion offer medium-term growth levers that require minimal incremental investment given the existing logistics infrastructure.

---
*Report generated as part of Data Analytics Internship — Project ID: 78G0OL*
