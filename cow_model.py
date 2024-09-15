
class CowModel:
    @staticmethod
    def can_be_milked(cow):
        return cow['Number of Teats'] == 4

    @staticmethod
    def calculate_milk_production(cow):
        age_years = cow.get('Age (Years)', 0)
        age_months = cow.get('Age (Months)', 0)
        return age_years + age_months
