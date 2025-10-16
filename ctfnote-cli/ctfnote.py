import requests
import schema
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

class CTFNote:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoint = HTTPEndpoint(f"{base_url}/graphql", {
            "Content-Type": "application/json"
        })

    def login(self, user, passwd):
        op = Operation(schema.Mutation)
        login_mutation = op.login(input={
            "login": user,
            "password": passwd,
        })

        login_mutation.jwt()

        resp = op + self.endpoint(op)
        jwt = resp.login.jwt

        self.endpoint.base_headers.update({
            "Authorization": f"Bearer {jwt}"
        })

    def getCTFs(self):
        op = Operation(schema.Query)
        q = op.ctfs()

        resp = op + self.endpoint(op)
        return resp.ctfs.nodes

    def getTasks(self):
        op = Operation(schema.Query)
        q = op.tasks()

        resp = op + self.endpoint(op)
        return resp.tasks.nodes

    def getTaskNotes(self, task) -> str:
        return requests.get(f"{self.base_url}/{task.pad_url}/download").text

