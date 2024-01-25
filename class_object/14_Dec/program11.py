
class Rasal:

    def __init__(company):
        company.Name = "RASAL PVT LTD"
        company.revenue = 121323
        company.profit = 1232
        company.address = "Pune"
        company.employee = 10000

    def comp_info(company):
        print("My Comapny name is:",company.Name)
        print("Our Company revenue is:",company.revenue)
        print("And profit is for this year:",company.profit)
        print("Our comapny is located at:",company.address)
        print("And we are team of:",company.employee,"peoples")

details = Rasal()
details.comp_info()

