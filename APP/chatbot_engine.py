from APP.analytics import (
    get_average_bill,
    get_average_energy_usage,
    get_automation_rate,
    get_total_customers,
    get_customer_usage,
    get_total_tickets
)

def chatbot_response(query: str):

    query = query.lower()

    if "average bill" in query:
        return f"The average customer bill is ${get_average_bill()}"

    elif "energy usage" in query:
        return f"The average energy usage is {get_average_energy_usage()} kWh"

    elif "automation rate" in query:
        return f"The chatbot automation rate is {get_automation_rate()}%"

    elif "customers" in query:
        return f"The total number of customers is {get_total_customers()}"

    elif "customer" in query:
        words = query.split()
        customer_id = words[-1].upper()
        return get_customer_usage(customer_id)

    elif "tickets" in query:
        return f"The total support tickets are {get_total_tickets()}"

    else:
        return "Sorry, I do not understand the question yet."