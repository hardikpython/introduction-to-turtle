import time

# Function to check if system is idle for a certain time (simulated)
def is_system_idle(idle_time):
    # Let's simulate that the system is idle if the idle time exceeds 10 seconds
    if idle_time > 10:
        return True
    return False

# Function to check if all applications are closed
def are_all_apps_closed(applications_running):
    if len(applications_running) == 0:
        return True
    return False

# Function to ask for user confirmation
def get_user_confirmation():
    response = input("Do you want to shut down the system? (yes/no): ")
    if response.lower() == 'yes':
        return True
    return False

# Main function to check conditions before shutdown
def check_shutdown_conditions():
    # Simulating system idle time
    idle_time = 15  # Let's assume the system has been idle for 15 seconds

    # Simulating list of running applications
    applications_running = ['Browser', 'TextEditor']  # Let's assume these apps are still open

    # Check if system is idle for the required time
    if not is_system_idle(idle_time):
        print("System is not idle long enough to shut down.")
        return

    # Check if all applications are closed
    if not are_all_apps_closed(applications_running):
        print("There are still applications running. Please close them before shutting down.")
        return

    # Get user confirmation for shutting down
    if get_user_confirmation():
        print("System shutting down...")
    else:
        print("Shutdown cancelled.")

# Calling the main function
check_shutdown_conditions()
