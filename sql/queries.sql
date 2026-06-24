-- Query 1: Top 5 Funds by AUM

SELECT *
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV

SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- Query 3: Transactions by State

SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 4: Funds with Expense Ratio < 1%

SELECT scheme_name,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Query 5: Average SIP Amount

SELECT AVG(amount_inr) AS avg_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- Query 6: Top 5 States by Investment Amount

SELECT state,
       SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;

-- Query 7: Fund Count by Fund House

SELECT fund_house,
       COUNT(*) AS fund_count
FROM dim_fund
GROUP BY fund_house;

-- Query 8: Top 5 Funds by 5-Year Return

SELECT scheme_name,
       return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Query 9: Risk Grade Distribution

SELECT risk_grade,
       COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;

-- Query 10: Daily Average NAV Trend

SELECT date,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY date
ORDER BY date;