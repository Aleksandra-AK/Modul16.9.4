from people import Worker, Volunteers

guest_list = []
while True:
    name = input("Enter the name: ")
    if name == '':
        break
    town = input("Enter the city: ")
    if input("Are you volunteer? ") == 'y':
        status = input("Enter the status: ")
        guest_list.append(Volunteers(name, town, status))
    else:
        status = input("Enter the position: ")
        guest_list.append(Worker(name, town, status))
for pep in guest_list:
    print(pep.get_guest())







