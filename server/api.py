# Create an API Endpoint class that self defines all api calls
class Endpoint:
    def __init__(self, name, description, methods, url, parameters):
        self.name = name
        self.description = description
        self.methods = methods
        self.url = url
        self.parameters = parameters or []

# Initialize an empty dictionary to store API endpoints
endpoints = {}


# API to create a guest VM
create_guest = Endpoint(
    name="create_guest",
    description="Create a guest VM",
    methods="POST",
    url="/api/createguest",
    parameters=["name", "memory"]
)

# Add api to endpoint dict
endpoints["create_guest"] = create_guest