# Amazon Sales Data Analysis Report
**Project ID:** 78G0OL  
**Dataset:** Amazon Sale Report.csv — 128,976 orders  
**Period Covered:** April 2022 – June 2022  
**Analyst:** Data Analytics Intern — InnoByte Services

---

## Executive Summary

This report presents a comprehensive analysis of Amazon India sales data covering ~3 months of transactions (April–June 2022). The dataset contains **128,976 orders** across 9 product categories, spanning 69 Indian states/territories. Total shipped revenue stands at **₹71.05 Million**, with an average order value of ₹649.

Key takeaways include strong dominance of T-shirts (~50% of revenue), Maharashtra as the top revenue state, a 14.2% cancellation rate that represents the single biggest operational challenge, nearly 70% Amazon-fulfilled orders, and a Premium customer segment (₹601–₹1,000) that generates the most revenue of any group.

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

Revenue shows a fluctuating trend across the three months with a peak mid-period followed by a slight decline. This is consistent with seasonal demand patterns in fashion e-commerce.

**Key Insight:** Month-on-month revenue changes should be tracked to anticipate inventory needs. If a declining trend persists beyond June 2022, promotional campaigns should be activated proactively.

### Order Amount Distribution (Figure 9)

The distribution of order amounts is right-skewed — the majority of orders fall between ₹300 and ₹1,000, with the mean (₹649) sitting above the median, indicating a small number of high-value orders pulling the average up.

**Key Insight:** Most customers are mid-to-premium spenders. Marketing efforts should target the ₹500–₹1,000 range where volume and value intersect optimally.

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

T-shirts alone account for nearly **50% of total revenue**, making them the single most critical category. Shirts come second at ~28%. Together these two categories drive ~78% of all revenue.

**Key Insight:** The business is heavily concentrated in basic apparel. Accessories (Wallet, Watch, Socks) are under-monetized relative to their unit volumes and represent strong upsell/cross-sell opportunities.

### Cancellation Rate by Category (Figure 10)

Some categories have significantly higher cancellation rates than others, pointing to category-specific issues such as sizing problems, quality complaints, or inaccurate listings.

**Key Insight:** Categories with above-average cancellation rates need immediate listing audits and stock accuracy checks. Reducing cancellations in high-volume categories like T-shirts has the highest revenue recovery potential.

### Size Distribution (Figure 6)

M and L are the most popular sizes, followed by XL. Sizes 5XL and 6XL see minimal demand.

**Key Insight:** Inventory should be stocked heavily in M, L, and XL. Overstocking 4XL–6XL leads to capital lock-up. Consider demand-based replenishment for extended sizes.

### Revenue Heatmap: Category × Month (Figure 8)

T-shirts and Shirts are consistently strong across all months. Blazzers show concentration in specific months, indicating seasonal demand.

**Key Insight:** Plan category-specific inventory 45 days ahead of demand peaks — Blazzers pre-winter, Perfumes pre-festival season.

---

## 3. Fulfillment Analysis

### Fulfillment Method (Figure 4)

| Method | Orders | Share |
|---|---|---|
| Amazon Fulfilled (FBA) | 89,713 | 69.6% |
| Merchant Fulfilled | 39,263 | 30.4% |

Amazon's FBA dominates, which is a positive indicator — FBA orders typically have higher delivery success rates and stronger customer trust.

### Order Status Breakdown (Figure 3)

- **Shipped – Delivered to Buyer:** the majority of shipped orders ✅
- **Cancelled:** 18,334 orders (14.2%) — the biggest concern area ⚠️
- **Returned / Rejected / Lost:** small but impactful on seller metrics and revenue recovery

**Key Insight:** The 14.2% cancellation rate is significantly above the ~5% industry benchmark. Each cancelled order at ₹649 average represents roughly **₹11.9M in lost revenue**. Investigating root causes (stock-outs, payment failures, delayed dispatch) is a critical priority.

---

## 4. Customer Segmentation

### B2B vs B2C (Figure 7)

| Segment | Orders | Share |
|---|---|---|
| B2C (Individual) | 1,28,104 | 99.3% |
| B2B (Business) | 872 | 0.7% |

The business is overwhelmingly B2C. However, B2B orders tend to be higher-value bulk purchases.

**Key Insight:** A dedicated B2B outreach program (corporate gifting, uniform supply) could unlock a high-margin revenue stream with minimal incremental effort.

### Customer Segmentation by Order Value (Figure 12)

| Segment | Orders | Revenue |
|---|---|---|
| Budget (₹0 – ₹300) | 1,631 (1.5%) | ₹0.47M |
| Mid-Range (₹301 – ₹600) | 50,661 (46.2%) | ₹23.09M |
| Premium (₹601 – ₹1,000) | 42,693 (38.9%) | ₹32.65M |
| High-Value (₹1,000+) | 12,174 (11.1%) | ₹14.84M |

**Key Insight:** The Premium segment generates the most revenue (₹32.65M) despite being second in order volume. Loyalty rewards and personalized recommendations targeting this segment will deliver the highest ROI.

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

Maharashtra and Karnataka (Mumbai + Bengaluru metros) together account for 30%+ of total revenue.

### Top 10 Cities by Revenue (Figure 11)

City-level analysis reveals that Mumbai, Bengaluru, Hyderabad, and Chennai are the top contributors. This adds depth to the state-level view and helps target hyperlocal marketing campaigns.

**Key Insight:** Tier-2 cities (Pune, Jaipur, Lucknow, Coimbatore) show organic demand. Improving delivery SLA in these cities can capture significant untapped revenue.

---

## 6. Business Insights & Recommendations

### 🔴 Critical Actions

1. **Reduce Cancellation Rate (14.2% → below 7%):** Audit cancellation reasons — incorrect stock listings, payment gateway failures, or delayed dispatch. Implement real-time inventory sync and pre-payment validation.

2. **Concentrate inventory in M, L, XL:** These sizes drive the majority of volume. Move 4XL+ to demand-based replenishment.

### 🟡 Growth Opportunities

3. **Upsell Accessories with Apparel:** Bundle Socks/Wallets/Watches as "Complete the Look" with T-shirt/Shirt purchases.

4. **Expand Amazon FBA coverage:** Migrating Merchant-fulfilled SKUs to FBA can improve delivery SLA and customer satisfaction scores.

5. **Launch B2B program:** Target corporate clients, schools, and event organizers. Even 5% B2B penetration could add ₹3.5M+ in high-margin revenue.

6. **Focus marketing on Premium segment:** The ₹601–₹1,000 segment generates ₹32.65M — the highest of any group. Retaining and growing this segment should be a top priority.

### 🟢 Regional Strategy

7. **Deepen in Top-5 States:** Maharashtra and Karnataka drive 30%+ of revenue. Invest in regional language creatives and same-day delivery in Mumbai and Bengaluru.

8. **Penetrate Tier-2 Cities:** Rajasthan, Madhya Pradesh, and Bihar show demand but are under-served. Partner with regional delivery networks to improve SLA.

### 📊 Operational Improvements

9. **Seasonal inventory planning:** Use the Category × Month heatmap (Figure 8) to plan SKU-level stock 45 days ahead of demand peaks.

10. **Return rate tracking:** Adding return analytics will help identify defective product batches or sizing issues early.

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
| `amazon_sales_analysis.py` | Full Python source code (run to regenerate all 12 charts) |
| `figures/fig1_monthly_revenue.png` | Monthly revenue trend |
| `figures/fig2_category_performance.png` | Category revenue + units sold |
| `figures/fig3_order_status.png` | Order status pie chart |
| `figures/fig4_fulfilment.png` | Amazon vs Merchant fulfillment |
| `figures/fig5_top_states.png` | Top 10 states by revenue |
| `figures/fig6_size_distribution.png` | Size-wise units sold |
| `figures/fig7_b2b_b2c.png` | B2B vs B2C split |
| `figures/fig8_heatmap.png` | Category × Month revenue heatmap |
| `figures/fig9_price_distribution.png` | Order amount distribution |
| `figures/fig10_cancellation_by_category.png` | Cancellation rate by category |
| `figures/fig11_top_cities.png` | Top 10 cities by revenue |
| `figures/fig12_customer_segmentation.png` | Customer segmentation by order value |
| `Amazon_Sales_Analysis_Report.md` | This report |
| `README.md` | Project overview and setup guide |

---

## Conclusion

The Amazon India sales data reveals a business with strong fundamentals — ₹71M in shipped revenue, healthy order volumes, and clear category leaders. The two highest-priority improvements are reducing the 14.2% cancellation rate (immediate revenue recovery of ~₹11.9M) and diversifying beyond T-shirts/Shirts to reduce single-category concentration risk.

The Premium customer segment (₹601–₹1,000) is the most valuable group and should anchor retention and marketing strategies. Geographic expansion to Tier-2 cities and a B2B program offer medium-term growth levers requiring minimal incremental investment.

---
