from abc import ABC, abstractmethod
class BaseRepository(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        pass

    @abstractmethod
    async def read(self, **kwargs):
        pass

    @abstractmethod
    async def update(self, **kwargs):
        pass

    @abstractmethod
    async def delete(self, **kwargs):
        pass