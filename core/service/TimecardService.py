from core.models import Timecard, Employee


class TimecardService:

    def get_timecard_by_emp_full_name(fullName):

        if (fullName is None or fullName == ""):
            return Timecard.objects.all()

        row = []

        for timecard in list(Timecard.objects.all()):
            if str(timecard.employer.get_full_name()).find(fullName) > -1:
                row.append(timecard)

        return row