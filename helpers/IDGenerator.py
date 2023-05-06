import uuid


class _IDGenerator:
    @staticmethod
    def getID():
        return str(uuid.uuid4())

    @staticmethod
    def getShortIDForOrder():
        return str(uuid.uuid4())[:6]


g_IDGenerator = _IDGenerator()
