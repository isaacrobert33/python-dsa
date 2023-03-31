class Role:
    ROLES = [
        "ENGINEER",
        "GRAPHICS DESIGNER",
        "PROJECT_MANAGER",
        "SALES_REPRESENTATIVE",
        "CUSTOMER RELATIONSHIP OFFICER",
    ]

    def __init__(self, role_id: int) -> None:
        self.role = self.ROLES[role_id]

    @classmethod
    def get_available_roles(cls):
        return cls.ROLES

    def __repr__(self) -> str:
        return f"<{self.role}>"


class Employee:
    def __init__(self, name: str, role: Role, salary: int) -> None:
        self.name = name
        self.salary = salary
        self.role = role

    def __str__(self) -> str:
        return f"<{self.name}: {self.role}>"


class Employees:
    def __init__(self, staffs: list) -> None:
        self.staffs = staffs

    def calc_average_salary(self):
        staffs_salary = [s.salary for s in self.staffs]
        return sum(staffs_salary) / len(self.staffs)

    def occupied_roles(self, member_id: int = None) -> list:
        return (
            self.staffs[member_id].role if member_id else [r.role for r in self.staffs]
        )


staffs = [
    Employee("Isaac", Role(1), 4000),
    Employee("Robert", Role(3), 5000),
    Employee("Tommy", Role(2), 5000),
    Employee("Camcoh", Role(4), 1400),
]
employees = Employees(staffs=staffs)
print(employees.calc_average_salary())
