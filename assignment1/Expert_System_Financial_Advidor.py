from experta import *


class FinancialStatus(Fact):
    """Fact to hold financial details."""
    pass


class InvestmentAdvisor(KnowledgeEngine):
    @Rule(FinancialStatus(SavingsAdequate=False))
    def recommend_savings(self):
        print("Recommendation: Focus on building your savings.")

    @Rule(FinancialStatus(SavingsAdequate=True, IncomeAdequate=True))
    def recommend_stocks(self):
        print("Recommendation: Invest in stocks for growth.")

    @Rule(FinancialStatus(SavingsAdequate=True, IncomeAdequate=False))
    def recommend_mixture(self):
        print("Recommendation: Consider a balanced investment strategy.")


# Input collection
no_of_dependents = int(input("Enter the number of dependents: "))
income_steady = input("Is your income steady? (yes/no): ").strip().lower() == "yes"
amount_saved = float(input("Enter the amount you have saved: "))
income = float(input("Enter your current income: "))

print("-" * 5)
print("Number of Dependents:", no_of_dependents)
print("Income Steady:", income_steady)
print("Amount Saved:", amount_saved)
print("Income:", income)

# Calculate thresholds
savings_threshold = no_of_dependents * 3000
income_threshold = 9000 + no_of_dependents * 2500

print("-" * 5)
print("Savings Threshold:", savings_threshold)
print("Income Threshold:", income_threshold)

# Determine adequacy
savings_adequate = amount_saved > savings_threshold
income_adequate = income_steady and income > income_threshold

print("-" * 5)
print("Savings Adequate:", savings_adequate)
print("Income Adequate:", income_adequate)

# Use the expert system
advisor = InvestmentAdvisor()
advisor.reset()  # Clear any previous knowledge
advisor.declare(
    FinancialStatus(SavingsAdequate=savings_adequate, IncomeAdequate=income_adequate)
)
advisor.run()
