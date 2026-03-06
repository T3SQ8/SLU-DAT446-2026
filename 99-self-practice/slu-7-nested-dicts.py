patients = {}


def add_entry(patient_name, date, message):
    # patients.setdefault(patient_name, {})
    if not patient_name in patients:
        patients[patient_name] = {}

    patients[patient_name][date] = message
