class Hawaii:
    def __init__(self):
        self.data = []

    def add_val(self, p_id, process, start_time, priority):
        self.data.append({'P_ID': p_id, 'Process': process, 'Start Time(ms)': start_time, 'Priority': priority})

    def sort_way(self, key):
        n = len(self.data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.data[j][key] > self.data[j + 1][key]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def print_table(self):
        print("{:<5} {:<10} {:<15} {:<10}".format("P_ID", "Process", "Start Time(ms)", "Priority"))
        print("="*40)
        for val in self.data:
            print("{:<5} {:<10} {:<15} {:<10}".format(val['P_ID'], val['Process'], val['Start Time(ms)'], val['Priority']))

obj_call = Hawaii()
obj_call.add_val("P1", "VSCode", 100, "MID")
obj_call.add_val("P23", "Eclipse", 234, "MID")
obj_call.add_val("P93", "Chrome", 189, "High")
obj_call.add_val("P42", "JDK", 9, "High")
obj_call.add_val("P9", "CMD", 7, "High")
obj_call.add_val("P87", "NotePad", 23, "Low")

print("\nChoose how you want to Sort:")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
print("3. Sort by Priority")

Ops = int(input("Enter Your Choice: "))

if Ops == 1:
    obj_call.sort_way('P_ID')
elif Ops == 2:
    obj_call.sort_way('Start Time(ms)')
elif Ops == 3:
    obj_call.sort_way('Priority')
# elif Ops == 4:
else:
    print("Invalid Choice. Please enter a valid option.")

obj_call.print_table()