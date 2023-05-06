class SqlQueries:
    @staticmethod
    def createProductsTable():
        return """
        CREATE TABLE IF NOT EXISTS `products` (
        `id` VARCHAR(36) NOT NULL,
        `name` VARCHAR(255) NOT NULL,
        `description` TEXT(500) NOT NULL,
        `cost` FLOAT NOT NULL,
        `image` BLOB NOT NULL,
        PRIMARY KEY (`id`));
        """

    @staticmethod
    def createTableOrders():
        return """
        CREATE TABLE IF NOT EXISTS `orders` (
        `id` VARCHAR(6) NOT NULL,
        `cost` FLOAT NOT NULL,
        `status` VARCHAR(45) NOT NULL,
        PRIMARY KEY (`id`));
        """

    @staticmethod
    def selectAllProducts():
        return """SELECT * FROM `products`"""