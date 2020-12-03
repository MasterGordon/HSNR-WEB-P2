# coding: utf-8
import cherrypy
from .db.database import Database
from .view import View

class Application:
    def __init__(self, employees: Database, trainings: Database):
        self.employees = employees
        self.traingings = trainings

    @cherrypy.expose
    def index(self):
        return View().index(
                {
                    "employees": self.employees.count(),
                    "trainings": 13,
                    "participations": 5
                }
            )

    @cherrypy.expose
    def default(self):
        raise cherrypy.HTTPError(404)
    default.expose = True

    @cherrypy.expose(alias = ['edit-employees'])
    def edit_employees(self):
        return View().editEmployees(
            {"employees": 
                [
                    {"name": "Gordon", "surname": "Goldbach", "degree": "Bachelor of Science", "occupation": "web-development"}, 
                    {"name": "Erik", "surname": "Simon", "degree": "Bachelor of Science", "occupation": ".net-development"},
                    {"name": "Gordon", "surname": "Goldbach", "degree": "Bachelor of Science", "occupation": "web-development"}, 
                    {"name": "Erik", "surname": "Simon", "degree": "Bachelor of Science", "occupation": ".net-development"}
                ] 
            })

    @cherrypy.expose
    def editTrainings(self):
        return

    @cherrypy.expose
    def participationEmployees(self):
        return

    @cherrypy.expose
    def participationTrainings(self):
        return

    @cherrypy.expose
    def reportEmployees(self):
        return

    @cherrypy.expose
    def reportTrainings(self):
        return

    @cherrypy.expose
    def reportCertificates(self):
        return

# EOF
