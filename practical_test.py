class node:
    def __init__(self, pid, name, pr):
        self.patient_id = pid
        self.patient_name = name
        self.priority = pr
        self.next = None


class priorityQueue:
    def __init__(self):
        self.front = None

    # 1. Add Patient 
    def enqueue(self, new_node):

        if self.front == None:
            self.front = new_node
            return

        # Insert at first position
        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        # Insert according to priority
        temp = self.front

        while temp.next != None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):

        if self.front == None:
            print("No patients waiting!")
            return

        print("\nNext Patient to be Treated:")
        print("Patient ID:", self.front.patient_id)
        print("Patient Name:", self.front.patient_name)

        if self.front.priority == 1:
            print("Priority: Critical")
        elif self.front.priority == 2:
            print("Priority: Serious")
        else:
            print("Priority: Normal")

    # 3. Remove Patient (Dequeue)
    def dequeue(self):

        if self.front == None:
            print("No patients to remove!")
            return

        temp = self.front
        self.front = self.front.next

        print("\nPatient treated and removed!")
        print("Patient ID:", temp.patient_id)
        print("Patient Name:", temp.patient_name)

    # 4. Display All Waiting Patients
    def display_all(self):

        if self.front == None:
            print("No patients waiting!")
            return

        temp = self.front

        print("\nAll Waiting Patients:")

        while temp != None:

            print("----------------------")
            print("Patient ID:", temp.patient_id)
            print("Patient Name:", temp.patient_name)

            if temp.priority == 1:
                print("Priority: Critical")
            elif temp.priority == 2:
                print("Priority: Serious")
            else:
                print("Priority: Normal")

            temp = temp.next


# Create Priority Queue
pq = priorityQueue()

while True:

    print("\nHOSPITAL EMERGENCY MANAGEMENT")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient After Treatment")
    print("4. Display All Waiting Patients")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':

        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")

        print("1 - Critical")
        print("2 - Serious")
        print("3 - Normal")

        pr = int(input("Enter Priority: "))

        if pr >= 1 and pr <= 3:
            pq.enqueue(node(pid, name, pr))
            print("Patient added successfully!")
        else:
            print("Invalid Priority!")

    elif choice == '2':
        pq.display_next()

    elif choice == '3':
        pq.dequeue()

    elif choice == '4':
        pq.display_all()

    elif choice == '5':
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")