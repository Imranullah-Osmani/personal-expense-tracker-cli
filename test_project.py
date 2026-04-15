from project import Transaction, Budget, calculate_remaining_budget

def test_transaction_display():
    t = Transaction(1, "Income", 1000, "Salary", "At office")
    output = t.display()
    assert "1" in output
    assert "Income" in output
    assert "1000" in output
    assert "Salary" in output
    assert "At office" in output



def test_budget_display():
    b = Budget("Food", 2000, 1000, 1000)
    output = b.__str__()
    assert "Food" in output
    assert "2000" in output
    assert "1000" in output
    assert "1000" in output


def test_set_budget():
    s = Budget("Entertainment", 1200, 200, 1000)
    s.new_spend(1000)
    assert s.b_spend == 1200
    assert s.b_remaining == 0

def test_calculate_remaining_budget():
    assert calculate_remaining_budget(1000, 500) == 500
    assert calculate_remaining_budget(1000, 5) == 995
    assert calculate_remaining_budget(1000, 50) == 950
    assert calculate_remaining_budget(100, 0) == 100
