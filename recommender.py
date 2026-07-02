risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

if risk.lower() == "low":
    print("\nRecommended Funds:")
    print("1. SBI Bluechip Fund")
    print("2. HDFC Balanced Advantage Fund")
    print("3. ICICI Prudential Equity & Debt Fund")

elif risk.lower() == "moderate":
    print("\nRecommended Funds:")
    print("1. Parag Parikh Flexi Cap Fund")
    print("2. Mirae Asset Large Cap Fund")
    print("3. Axis Growth Opportunities Fund")

elif risk.lower() == "high":
    print("\nRecommended Funds:")
    print("1. Quant Small Cap Fund")
    print("2. Nippon India Small Cap Fund")
    print("3. SBI Small Cap Fund")

else:
    print("Invalid Risk Appetite")