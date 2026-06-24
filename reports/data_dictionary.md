# Data Dictionary - Mutual Fund Analytics

## 01_fund_master.csv

| Column Name        | Data Type | Description                       |
| ------------------ | --------- | --------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme code           |
| fund_house         | Text      | Mutual fund company name          |
| scheme_name        | Text      | Name of mutual fund scheme        |
| category           | Text      | Fund category (Equity, Debt etc.) |
| sub_category       | Text      | Fund sub-category                 |
| plan               | Text      | Direct or Regular plan            |
| launch_date        | Date      | Scheme launch date                |
| benchmark          | Text      | Benchmark index                   |
| expense_ratio_pct  | Float     | Expense ratio percentage          |
| exit_load_pct      | Float     | Exit load percentage              |
| min_sip_amount     | Integer   | Minimum SIP amount                |
| min_lumpsum_amount | Integer   | Minimum lump sum investment       |
| fund_manager       | Text      | Fund manager name                 |
| risk_category      | Text      | Risk level                        |
| sebi_category_code | Text      | SEBI category code                |

---

## 02_nav_history.csv

| Column Name | Data Type | Description     |
| ----------- | --------- | --------------- |
| amfi_code   | Integer   | Scheme code     |
| date        | Date      | NAV date        |
| nav         | Float     | Net Asset Value |

---

## 03_aum_by_fund_house.csv

| Column Name    | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | Fund house name   |
| aum_lakh_crore | Float     | AUM in lakh crore |
| aum_crore      | Integer   | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |

---

## 04_monthly_sip_inflows.csv

| Column Name               | Data Type | Description           |
| ------------------------- | --------- | --------------------- |
| month                     | Text      | Reporting month       |
| sip_inflow_crore          | Integer   | SIP inflow amount     |
| active_sip_accounts_crore | Float     | Active SIP accounts   |
| new_sip_accounts_lakh     | Float     | New SIP accounts      |
| sip_aum_lakh_crore        | Float     | SIP AUM               |
| yoy_growth_pct            | Float     | Year-over-year growth |

---

## 05_category_inflows.csv

| Column Name      | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Text      | Reporting month   |
| category         | Text      | Fund category     |
| net_inflow_crore | Float     | Net inflow amount |

---

## 06_industry_folio_count.csv

| Column Name         | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Text      | Reporting month |
| total_folios_crore  | Float     | Total folios    |
| equity_folios_crore | Float     | Equity folios   |
| debt_folios_crore   | Float     | Debt folios     |
| hybrid_folios_crore | Float     | Hybrid folios   |
| others_folios_crore | Float     | Other folios    |

---

## 07_scheme_performance.csv

| Column Name       | Data Type | Description   |
| ----------------- | --------- | ------------- |
| amfi_code         | Integer   | Scheme code   |
| scheme_name       | Text      | Scheme name   |
| return_1yr_pct    | Float     | 1 year return |
| return_3yr_pct    | Float     | 3 year return |
| return_5yr_pct    | Float     | 5 year return |
| alpha             | Float     | Alpha value   |
| beta              | Float     | Beta value    |
| sharpe_ratio      | Float     | Sharpe ratio  |
| expense_ratio_pct | Float     | Expense ratio |
| risk_grade        | Text      | Risk grade    |

---

## 08_investor_transactions.csv

| Column Name        | Data Type | Description              |
| ------------------ | --------- | ------------------------ |
| investor_id        | Text      | Investor identifier      |
| transaction_date   | Date      | Transaction date         |
| amfi_code          | Integer   | Scheme code              |
| transaction_type   | Text      | SIP, Lumpsum, Redemption |
| amount_inr         | Integer   | Transaction amount       |
| state              | Text      | Investor state           |
| city               | Text      | Investor city            |
| gender             | Text      | Gender                   |
| annual_income_lakh | Float     | Annual income            |
| payment_mode       | Text      | Payment method           |
| kyc_status         | Text      | KYC verification status  |

---

## 09_portfolio_holdings.csv

| Column Name       | Data Type | Description         |
| ----------------- | --------- | ------------------- |
| amfi_code         | Integer   | Scheme code         |
| stock_symbol      | Text      | Stock symbol        |
| stock_name        | Text      | Company name        |
| sector            | Text      | Industry sector     |
| weight_pct        | Float     | Portfolio weight    |
| market_value_cr   | Float     | Market value        |
| current_price_inr | Float     | Current stock price |

---

## 10_benchmark_indices.csv

| Column Name | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Trading date         |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Closing index value  |
