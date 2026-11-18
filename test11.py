class node:

    def __init__(self, pid, name, pr):
        self.patient_id = pid
        self.patient_name = name
        self.priority = pr
        self.next = None


class priorityQueue:# creates a class for managing patients

    def __init__(self):
        self.front = None # it is initially empty

    # Input Patient Details
    def input_patient(self):

        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        pr = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if pr < 1 or pr > 3:
            print("Invalid Priority")
        else:
            new_node = node(pid, name, pr)
            self.enqueue(new_node)

    # 1. Add Patient (Enqueue)
    def enqueue(self, new_node):

        if self.front == None or new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node

        else:
            temp = self.front

            while temp.next != None and temp.next.priority <= new_node.priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully")

    # 2. Display Next Patient
    def display_next(self):

        if self.front == None:
            print("Queue is empty")

        else:
            print("Next patient to be treated:")
            print("Patient ID:", self.front.patient_id)
            print("Patient Name:", self.front.patient_name)
            print("Priority:", self.front.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):

        if self.front == None:
            print("Queue is empty")

        else:
            temp = self.front

            print("Patient treated:")
            print("Patient ID:", temp.patient_id)
            print("Patient Name:", temp.patient_name)

            self.front = self.front.next

    # 4. Display All Patients
    def display_all(self):

        if self.front == None:
            print("Queue is empty")

        else:
            temp = self.front

            print("All waiting patients:")

            while temp != None:
                print("Patient ID:", temp.patient_id)
                print("Patient Name:", temp.patient_name)
                print("Priority:", temp.priority)
                print("-------------------")

                temp = temp.next


# Main Program

pq = priorityQueue()

while True:

    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        pq.input_patient()

    elif ch == 2:
        pq.display_next()

    elif ch == 3:
        pq.dequeue()

    elif ch == 4:
        pq.display_all()

    elif ch == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice")