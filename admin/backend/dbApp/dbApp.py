from .database import databaseSession
from .sqlQueries import SqlQueries
from admin.backend.helpers.fileSystem import fileSystem


class DatabaseInitializer:
    @classmethod
    def run(cls):
        operations = [
            SqlQueries.createDatabase(),
            SqlQueries.createProductsTable(),
            SqlQueries.createTableOrders()
        ]
        with databaseSession as db:
            for operation in operations:
                db.execute(operation)
        cls.__createProducts()

    @staticmethod
    def __createProducts():
        for file in fileSystem.listDir("./data/products/", suffix="json"):
            data = fileSystem.readJson(file)
            name = data["name"]
            description = data["description"]
            cost = float(data["cost"])
            image = fileSystem.convertImageToBytes(data["image"])
            data["image"] = image
            with databaseSession as db:
                db.execute(
                    SqlQueries.insertProduct(
                        name=name,
                        description=description,
                        cost=cost,
                        image=image
                    ),
                    data
                )
