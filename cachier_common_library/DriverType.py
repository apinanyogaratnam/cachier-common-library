class DriverType:
    RAM = 'ram'
    JSON = 'json'
    SQLITE = 'sqlite'
    PICKLE = 'pickle'

    def is_valid(self: 'DriverType', driver_type: str) -> bool:
        return driver_type in [
            self.RAM,
            self.JSON,
            self.SQLITE,
            self.PICKLE,
        ]
