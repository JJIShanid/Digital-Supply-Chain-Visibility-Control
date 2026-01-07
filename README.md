# Digital-Supply-Chain-Visibility-Control
This project delivers an end-to-end Supply Chain Visibility and Control (SCVC) solution designed to support inventory management, delivery performance tracking, and supply planning decision-making.
The dashboard enables executives, supply planners, and project managers to quickly identify risks, trends, and improvement opportunities across the supply chain.
<img width="1870" height="813" alt="Screenshot 2026-01-07 223419" src="https://github.com/user-attachments/assets/24d98fd6-6b2a-40a4-ba2b-1547b13d96e3" />
<img width="1827" height="904" alt="Screenshot 2026-01-07 223430" src="https://github.com/user-attachments/assets/0ef2f081-3e60-4710-875c-76cadf9916ef" />

2. Business Problem

Modern supply chains face challenges such as:

Limited visibility into inventory levels

Difficulty predicting stockouts and overstock situations

Poor transparency of delivery delays

Inaccurate demand forecasting

Fragmented KPI reporting for management

This project addresses these challenges by combining advanced analytics with simple, intuitive visual storytelling.

3. Solution Summary

The solution consists of:

Backend analytics (Jupyter Notebook)

Data cleaning and transformation

Inventory and delivery modeling

Machine learning–based demand forecasting

Frontend dashboard (Streamlit)

Clear executive KPIs

Interactive and understandable visualizations

Management-ready storytelling

4. Data & Assumptions

Since real enterprise data often lacks full transparency, the following realistic assumptions were applied:

Inventory levels were synthetically generated to simulate stock flow

Supplier IDs were created to evaluate supplier performance

Delivery lead times were simulated to assess on-time vs delayed deliveries

These assumptions reflect standard industry practices in analytics and consulting projects.

5. Executive KPI Overview
   KPI Cards Explained
   | KPI                   | What It Shows                                                 | Why It Matters                    |
| --------------------- | ------------------------------------------------------------- | --------------------------------- |
| Avg Delivery Time     | Average number of days taken to deliver orders                | Indicates supply chain efficiency |
| On-Time Delivery %    | Percentage of orders delivered on or before planned lead time | Core SCVC reliability metric      |
| Total Inventory Value | Monetary value of current inventory on hand                   | Capital tied up in stock          |
| Forecast Accuracy     | Accuracy of demand forecast vs actual sales                   | Planning and forecasting quality  |

6. Inventory Visibility Section
📊 Graph: Average Inventory Level Over Time

What it shows:
A time-series line chart showing how average inventory levels change over time.

Business insight:

Identifies inventory build-up or depletion trends

Helps planners anticipate overstock or stockout situations

Supports inventory optimization decisions

🟢🔴 Graph: Inventory Health Distribution (Pie Chart)

What it shows:
Breakdown of inventory into:

Healthy Stock

Reorder Required

Business insight:

Highlights products that need immediate attention

Enables proactive replenishment planning

Reduces stockout risk

7. Delivery & Order Performance
🚚 Graph: On-Time vs Delayed Deliveries

What it shows:
Bar chart comparing the number of on-time and delayed deliveries.

Business insight:

Measures delivery reliability

Helps identify execution issues in logistics

Supports performance reviews and corrective actions

8. Supply Planning & Demand Forecasting
📈 Graph: Actual vs Forecast Sales

What it shows:
Line chart comparing:

Actual historical sales

Machine learning–based forecasted sales

Business insight:

Evaluates forecast quality

Supports demand planning and capacity decisions

Helps reduce overproduction or missed sales

Model used:
Random Forest Regressor (chosen for robustness and non-linear pattern handling)

🎯 KPI: Forecast Accuracy

What it shows:
Forecast accuracy measured using Mean Absolute Percentage Error (MAPE).

Business insight:

Higher accuracy means better planning reliability

Directly impacts inventory and service levels

9. Supplier Performance Analysis
🏭 Graph: On-Time Delivery Performance by Supplier

What it shows:
Bar chart displaying on-time delivery percentage per supplier.

Business insight:

Identifies high- and low-performing suppliers

Supports supplier evaluation and negotiations

Enables targeted improvement initiatives

10. Seasonal Demand Analysis
📆 Graph: Monthly Sales Distribution

What it shows:
Bar chart showing total sales per month.

Business insight:

Identifies seasonality and demand patterns

Helps plan inventory and capacity ahead of peak periods

Supports long-term supply planning

11. Architecture & Tools Used

    | Layer           | Tools                        |
| --------------- | ---------------------------- |
| Data Processing | Python, Pandas, NumPy        |
| Forecasting     | Scikit-learn (Random Forest) |
| Analytics       | Jupyter Notebook             |
| Visualization   | Streamlit, Plotly            |
| Version Control | Git & GitHub                 |

12. How to Run the Project
pip install pandas numpy streamlit plotly scikit-learn
cd digital-scvc-dashboard
streamlit run app.py

15. Future Enhancements

Scenario planning (what-if demand changes)

ERP integration (SAP, Oracle)

Automated alerts for stockouts and delays

Risk heatmaps for supply disruptions

16. Final Note

This project is designed to mirror real enterprise supply chain analytics solutions, not academic exercises.
It demonstrates the ability to turn complex data into clear, actionable insights — a critical skill for supply chain, analytics, and project management roles.

📌 Author

Ishan
Master’s in Data Science – Business Analytics


    
