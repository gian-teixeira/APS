from view.provider.Provider import Provider
from model.StudentConsumption import StudentConsumption

class StudentConsumptionProvider(Provider):
    def label(obj: StudentConsumption) -> str:
        return obj.id
    
    def info(obj: StudentConsumption) -> tuple[tuple[str,str]]:
        return (
            ('ID do Estudante', obj.student_id),
            ('Créditos Gastos', obj.spent_credits),
            ('Refeições Realizadas', 
                ' '.join([f"{date}-{period}" for date,period in obj.days_attended])),
        )