class ChildrenCamp:
    def __init__(self, child_id, chocolates_received):
        self.child_id = child_id
        self.chocolates_received = chocolates_received

    def calculate_total_chocolates(self):
        return sum(self.chocolates_received)

    def reward_child(self, child_id_rewarded, extra_chocolates):
        if extra_chocolates < 1:
            return "Extra chocolates is less than 1"
        if child_id_rewarded not in self.child_id:
            return "Child id is invalid"
        index = self.child_id.index(child_id_rewarded)
        self.chocolates_received[index] += extra_chocolates
        return self.chocolates_received

child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

camp = ChildrenCamp(child_id, chocolates_received)
print(camp.calculate_total_chocolates())

print(camp.reward_child(30, 2))

print(camp.calculate_total_chocolates())

print(camp.reward_child(60, 2))

print(camp.reward_child(40, 0))
