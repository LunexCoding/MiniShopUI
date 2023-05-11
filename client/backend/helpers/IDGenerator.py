import uuid


class _IDGenerator:
    @staticmethod
    def getOrderID():
        return str(uuid.uuid4())[:6]


g_IDGenerator = _IDGenerator()
