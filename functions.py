import math

def calculate_cost_of_equity(risk_free_asset, beta, market_return):
    ke = (risk_free_asset + beta * (market_return - risk_free_asset)) * 100
    return ke

def get_most_recent_value(data, metric_name):
    if metric_name in data.index:
        return data.loc[metric_name].iloc[0]
    return None

def calculate_cost_of_debt(interest_expense, total_debt):
    kd = (interest_expense / total_debt) * 100
    return kd

def effective_tax_rate(income_tax_expense, income_before_tax):
    tax_rate = (income_tax_expense / income_before_tax) * 100
    return tax_rate


def cost_of_debt_after_tax (cost_of_debt, tax_rate):
    calculate_cost_of_debt_after_tax = cost_of_debt * (1 - tax_rate / 100)
    return calculate_cost_of_debt_after_tax

def check_and_display_variables(variables):
    for name, value in variables.items():
        if math.isnan(value)== False:
            return True
        else:
            print(f"{name} not found.\n")
            break