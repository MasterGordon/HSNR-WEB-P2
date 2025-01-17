from mako.lookup import TemplateLookup

class View:
    def __init__(self):
        self.lookup = TemplateLookup('./templates')

    def index(self, data):
        template = self.lookup.get_template('index.mako')
        return template.render(**data)

    def editEmployees(self, data):
        template = self.lookup.get_template('edit-employees.mako')
        return template.render(**data)

    def viewEmployee(self, data):
        template = self.lookup.get_template('view-employee.mako')
        return template.render(**data)

    def editCertificates(self, data):
        template = self.lookup.get_template('edit-certificates.mako')
        return template.render(**data)

    def editQualifications(self, data):
        template = self.lookup.get_template('edit-qualifications.mako')
        return template.render(**data)

    def editTrainings(self, data):
        template = self.lookup.get_template('edit-trainings.mako')
        return template.render(**data)

    def viewTraining(self, data):
        template = self.lookup.get_template('view-training.mako')
        return template.render(**data)

    def editTraining(self, data):
        template = self.lookup.get_template('edit-training.mako')
        return template.render(**data)

    def addTraining(self, data):
        template = self.lookup.get_template('add-training.mako')
        return template.render(**data)

    def participationEmployees(self, data):
        template = self.lookup.get_template('participation-employees.mako')
        return template.render(**data)

    def participationEmployee(self, data):
        template = self.lookup.get_template('participation-employee.mako')
        return template.render(**data)

    def participationTrainings(self, data):
        template = self.lookup.get_template('participation-trainings.mako')
        return template.render(**data)

    def participationTraining(self, data):
        template = self.lookup.get_template('participation-training.mako')
        return template.render(**data)

    def reportEmployees(self, data):
        template = self.lookup.get_template('report-employees.mako')
        return template.render(**data)

    def reportTrainings(self, data):
        template = self.lookup.get_template('report-trainings.mako')
        return template.render(**data)

    def reportCertificates(self, data):
        template = self.lookup.get_template('report-certificates.mako')
        return template.render(**data)
