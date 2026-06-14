def login_required(func):

    def wrapper():

        print("Checking Login...")

        func()

    return wrapper


@login_required
def dashboard():
    print("Dashboard Opened Successfully")


dashboard()
