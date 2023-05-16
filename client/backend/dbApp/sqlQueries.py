class SqlQueries:
    @staticmethod
    def createDatabase():
        return """CREATE DATABASE IF NOT EXISTS `storage`;"""

    @staticmethod
    def createProductsTable():
        return """
        CREATE TABLE IF NOT EXISTS `storage`.`products` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(255) NOT NULL,
        `description` TEXT(500) NOT NULL,
        `cost` FLOAT NOT NULL,
        `image` LONGBLOB NOT NULL,
        PRIMARY KEY (`id`));
        """

    @staticmethod
    def createTableOrders():
        return """
        CREATE TABLE IF NOT EXISTS `storage`.`orders` (
        `id` VARCHAR(6) NOT NULL,
        `cost` FLOAT NOT NULL,
        `productIDs` TEXT(1000) NOT NULL,
        PRIMARY KEY (`id`));
        """

    @staticmethod
    def selectAllProducts():
        return """SELECT * FROM `storage`.`products`"""

    @staticmethod
    def insertProduct(name, description, cost, image):
        return """
        INSERT INTO `storage`.`products`
            (name, description, cost, image)
        SELECT
            %(name)s, %(description)s, %(cost)s, %(image)s
        WHERE
            NOT EXISTS (
                SELECT name FROM `storage`.`products` WHERE name = %(name)s
            )
        """

    @staticmethod
    def insertOrder(orderID, cost, productIDs):
        return """
        INSERT INTO `storage`.`orders`
            (id, cost, productIDs)
        VALUES 
            (%(orderID)s, %(cost)s, %(productIDs)s);
        """