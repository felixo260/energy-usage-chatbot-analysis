from APP.data_loader import load_data

customers, energy, chatbot, support = load_data()

def get_average_energy_usage():
    return round(energy["Usage_kWh"].mean(), 2)

def get_average_bill():
    return round(energy["Total_Charge"].mean(), 2)

def get_total_customers():
    return customers.shape[0]

def get_automation_rate():
    automated = chatbot[chatbot["Response_Type"] == "automated"].shape[0]
    total = chatbot.shape[0]

    return round((automated / total) * 100, 2)
def get_customer_usage(customer_id):

    customer_data = energy[energy["Customer_ID"] == customer_id]

    if customer_data.empty:
        return "Customer not found"

    usage = round(customer_data["Usage_kWh"].mean(), 2)

    return f"Customer {customer_id} average usage is {usage} kWh"

def get_total_tickets():
    return support.shape[0]
