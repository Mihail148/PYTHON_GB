from task_03 import DataPerson


class Employee(DataPerson):
    def __init__(self, emp_id: int = 1, *args, **kwargs):
        if len(str(emp_id)) != 6:
            raise ValueError('Некорректный идентификационный номер')
        self.emp_id = emp_id
        self.level = sum(map(int, str(emp_id))) % 7

        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    e = Employee(123321, 'Александр', 'Пушкин', 19)
    print(f'{e.emp_id=}, {e.level=}')