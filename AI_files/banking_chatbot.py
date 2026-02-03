import re

def get_response(user_input: str) -> str:
    text = user_input.lower().strip()

    # Exit
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for using our banking assistant. Goodbye!"

    # Greetings
    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", text):
        return "Hello! How can I help you with your banking needs today?"

    # Account types
    if re.search(r"\b(account|account types|savings|current)\b", text):
        return (
            "We offer Savings Accounts, Current Accounts, Fixed Deposits "
            "and Recurring Deposits."
        )

    # Balance enquiry
    if re.search(r"\b(balance|check balance)\b", text):
        return (
            "For security reasons, I cannot show your balance here.\n"
            "Please use mobile banking, net banking, ATM, or visit the branch."
        )

    # Branch timings
    if re.search(r"\b(timing|branch hours|open)\b", text):
        return (
            "Our branches operate from 9:30 AM to 3:30 PM (Mon–Fri).\n"
            "2nd and 4th Saturdays are holidays."
        )

    # Lost card
    if re.search(r"\b(lost card|block card|stolen card)\b", text):
        return (
            "Please immediately call our 24x7 helpline at 1800-123-4567 "
            "to block your card."
        )

    # Open new account
    if re.search(r"\b(open account|new account|account opening)\b", text):
        return (
            "To open a new account, bring ID proof, address proof, and photos.\n"
            "You can also apply online."
        )

    # Loans
    if re.search(r"\b(loan|home loan|education loan|personal loan)\b", text):
        return (
            "We offer Home, Personal, Education and Vehicle Loans.\n"
            "Interest rates depend on amount and tenure."
        )

    # Interest rates
    if re.search(r"\b(interest|roi|rate of interest)\b", text):
        return (
            "Interest rates vary for savings, FD, RD and loans.\n"
            "Please check the official website for latest rates."
        )

    # Net banking
    if re.search(r"\b(net banking|mobile banking|online banking)\b", text):
        return (
            "You can activate net banking using your customer ID.\n"
            "Download our mobile app for mobile banking."
        )

    # Default reply
    return (
        "Sorry, I didn't understand that.\n"
        "You can ask about accounts, balance, loans, interest rates, "
        "net banking, branch timings or lost card."
    )

def banking_chatbot():
    print("BankBot: Welcome! I am your rule-based banking assistant.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("BankBot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

# Run chatbot
banking_chatbot()