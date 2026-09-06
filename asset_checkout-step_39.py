# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: AssetCheckout
# AssetCheckout - Scenarios
def print_scenarios():
    print("AssetCheckout: Documented Usage Scenarios")
    print("==========================================")
    print("""
    1. Equipment Checkout:
       - Register equipment with ID, name, status ('available', 'checked_out', 'checked_in', 'broken')
       - Create recipients with name, department, and contact info
       - Check out equipment to a recipient with a checkout date and optional notes
       - System records the checkout date and updates equipment status to 'checked_out'

    2. Equipment Return:
       - Record return date when equipment is given back
       - Update equipment status to 'checked_in'
       - Optionally mark equipment as 'broken' if it has issues
       - System calculates usage duration between checkout and return dates

    3. Equipment History:
       - View complete checkout/return history for any equipment
       - Display all recipients who have used specific equipment
       - Show total usage duration and number of checkouts

    4. Equipment Management:
       - Add new equipment to the inventory
       - Remove equipment from the system
       - Search equipment by ID, name, or status
       - List all available equipment for checkout

    5. Recipient Management:
       - Add new recipients to the system
       - Search recipients by name or department
       - View all equipment currently checked out to a specific recipient
       - Remove recipients from the system

    6. Status Tracking:
       - Monitor equipment status changes over time
       - Identify broken equipment and generate maintenance alerts
       - Track equipment utilization rates
    """)
    print("==========================================")
    print("Scenarios documentation complete.")
