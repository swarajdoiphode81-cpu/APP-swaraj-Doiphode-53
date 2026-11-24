def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR")
        print("=" * 60)

        func(*args, **kwargs)

        print("=" * 60)
        print("END OF REPORT")
        print("=" * 60)

    return wrapper


class Report:
    company_name = "ABC Technologies Pvt. Ltd."

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

    def add_content(self, text):
        self.contents.append(text)

    @classmethod
    def display_report(cls, report_obj):
        print("Company Name:", cls.company_name)
        print("Report Title:", report_obj.title)
        print("Author:", report_obj.author)
        print("\nReport Contents:")

        for item in report_obj.contents:
            print("-", item)


# Applying decorator
@report_decorator
def generate_report(report_obj):
    Report.display_report(report_obj)


# Main program
report = Report("Annual Performance Report", "Ritesh")

report.add_content("Company performance was excellent.")
report.add_content("Sales increased by 20%.")
report.add_content("New projects were successfully completed.")

generate_report(report)