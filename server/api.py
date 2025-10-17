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


# API to boot guest VM
boot_guest = Endpoint(
    name="boot_guest",
    description="Boot a guest VM",
    methods="POST",
    url="/api/bootguest",
    parameters=["name"]
)


# API to create a guest VM
create_guest = Endpoint(
    name="create_guest",
    description="Create a guest VM",
    methods="POST",
    url="/api/createguest",
    parameters=["name", "memory", "cores", "cdrom", "volume"]
)


# Add apis to endpoint dict
endpoints["boot_guest"] = boot_guest
endpoints["create_guest"] = create_guest