# Retail Sales Data Exploratory Data Analysis (EDA)

A comprehensive Exploratory Data Analysis (EDA) project on retail sales transaction data spanning 2023 to 2025. Built with Python, Pandas, Matplotlib, Seaborn, and Jupyter Notebook.

---

## 📁 Repository Structure

```
retail_sales_eda/
│
├── data/
│   └── retail_sales_data.csv        # Comprehensive retail sales dataset (2,000 rows x 17 columns)
├── eda_retail_sales.ipynb           # Fully executed Jupyter Notebook with charts, analysis & insights
├── generate_data.py                 # Script to generate synthetic retail sales dataset with realistic trends
├── generate_notebook.py             # Script to programmatically construct the Jupyter notebook
├── execute_notebook.py              # Script to execute all notebook cells and bake outputs inline
└── README.md                        # Documentation and project overview
```

---

## 📊 Checklist & Covered Requirements

- [x] **Initial Inspection:** Dataset shape, column dtypes, null value audit (`df.isnull().sum()`), `head()` inspection.
- [x] **Descriptive Statistics:** Detailed central tendencies (Mean, Median, Mode) and dispersion (Std Dev, Variance, IQR, Min, Max, Skewness) for all numerical features.
- [x] **Time Series Analysis:** Monthly revenue & profit trajectory line charts (annotated Q4 peaks) and quarterly revenue comparison bar chart across fiscal years (2023–2025).
- [x] **Customer Demographics:** Customer age distribution (Histogram + KDE), Gender breakdown (Pie chart), and Customer Segment revenue split (Consumer, Corporate, Home Office).
- [x] **Product Performance:** Top 10 best-selling products by revenue (Horizontal bar chart) and category-level revenue vs. profit breakdown.
- [x] **Correlation Heatmap:** Annotated Seaborn heatmap showing Pearson correlation matrix of numerical features.
- [x] **Non-Obvious Insight Visualisation:** Heatmap analyzing the impact of Discount Tiers on Net Profit Margin % across Product Categories, revealing margin erosion in low-margin categories.
- [x] **Written Observations:** Descriptive Markdown observation cells immediately following every chart and table.
- [x] **Strategic Conclusion:** 3 actionable, data-backed business recommendations for dynamic discounting, Q4 campaign optimization, and corporate B2B bundling.

---

## 🚀 Quickstart & How to Run

1. **Activate Virtual Environment / Install Dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn scipy nbformat nbconvert jupyter
   ```

2. **Generate / Refresh Dataset (Optional):**
   ```bash
   python generate_data.py
   ```

3. **Re-build & Execute Notebook:**
   ```bash
   python generate_notebook.py
   python execute_notebook.py
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook eda_retail_sales.ipynb
   ```

---

## 💡 Key Business Insights & Actionable Recommendations

1. **Category-Specific Dynamic Discount Caps:**
   - *Finding:* Discount rates >20% in low-margin lines (Home Appliances, Electronics Accessories) reduce profit margins from 42% down to 18%, pushing orders into negative margin territory.
   - *Recommendation:* Cap promotional discounts at **15% for Electronics and Home Appliances**, while using aggressive clearance discounts (up to 30%) exclusively on high-margin Apparel and Stationery.

2. **Q4 Seasonality Optimization:**
   - *Finding:* Q4 accounts for nearly **40% of annual store revenue**, driven by Black Friday and holiday gift buying.
   - *Recommendation:* Launch targeted holiday marketing campaigns 3 weeks earlier (mid-October) focusing on high-ticket bundles for the core demographic aged 25–49.

3. **Corporate & Home Office B2B Bundling:**
   - *Finding:* Corporate transactions yield significantly higher average order values due to bulk hardware purchases.
   - *Recommendation:* Introduce structured corporate procurement bundles offering volume discount tiers for laptops, ergonomic chairs, and office accessories.
