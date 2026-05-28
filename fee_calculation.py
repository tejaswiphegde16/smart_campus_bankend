def calculate_fee(tuition, hostel=0, transport=0):

    return tuition + hostel + transport

def fee_demo():

    tuition = int(input("Enter tuition fee: "))
    hostel = int(input("Enter hostel fee: "))
    transport = int(input("Enter transport fee: "))

    total = calculate_fee(tuition, hostel, transport)

    print("Total Fee:", total)