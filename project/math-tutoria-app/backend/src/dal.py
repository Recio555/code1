from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument

from pydantic import BaseModel

from uuid import uuid4
from typing import Union, Optional

class ListSummary(BaseModel):
    id: str
    name: str
    item_count: int
    nombre: str
    apellido: str

    @staticmethod
    def from_doc(doc) -> "ListSummary":
        return ListSummary(
            id=str(doc["_id"]),
            name=doc.get("name", ""),
            item_count=doc.get("item_count", 0),
            nombre=doc.get("nombre", ""),
            apellido=doc.get("apellido", "")
        )

class ToDoListItem(BaseModel):
    id: str
    label: str
    checked: bool

    @staticmethod
    def from_doc(item) -> "ToDoListItem":
        return ToDoListItem(
            id=item.get("id", ""),
            label=item.get("label", ""),
            nombre=doc.get("nombre", ""),
            checked=item.get("checked", False),
        )

class ToDoList(BaseModel):
    id: str
    name: str
    items: list[ToDoListItem]

    @staticmethod
    def from_doc(doc) -> "ToDoList":
        return ToDoList(
            id=str(doc["_id"]),
            name=doc.get("name", ""),
            items=[ToDoListItem.from_doc(item) for item in doc.get("items", [])],
        )

class ToDoDAL:
    def __init__(self, todo_collection: AsyncIOMotorCollection):
        self._todo_collection = todo_collection

    async def list_todo_lists(self, session=None):
        cursor = self._todo_collection.aggregate(
            [
                {
                    "$project": {
                        "nombre": 1,
                        "apellido": 1,
                        "name": 1,
                        "item_count": {"$size": {"$ifNull": ["$items", []]}}
                    }
                },
                {
                    "$sort": {"name": 1}
                }
            ],
            session=session,
        )
        async for doc in cursor:
            yield ListSummary.from_doc(doc)

    async def create_todo_list(self, name: str, session=None) -> str:
        response = await self._todo_collection.insert_one(
            {"name": name, "items": []},
            session=session,
        )
        return str(response.inserted_id)

    async def get_todo_list(self, id: Union[str, ObjectId], session=None) -> Optional[ToDoList]:
        doc = await self._todo_collection.find_one(
            {"_id": ObjectId(id)},
            session=session,
        )
        return ToDoList.from_doc(doc) if doc else None

    async def delete_todo_list(self, id: Union[str, ObjectId], session=None) -> bool:
        response = await self._todo_collection.delete_one(
            {"_id": ObjectId(id)},
            session=session,
        )
        return response.deleted_count == 1

    async def create_item(
        self,
        id: Union[str, ObjectId],
        label: str,
        session=None,
    ) -> Optional[ToDoList]:
        result = await self._todo_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {
                "$push": {
                    "items": {
                        "id": uuid4().hex,
                        "label": label,
                        "checked": False,
                    }
                }
            },
            session=session,
            return_document=ReturnDocument.AFTER,
        )
        return ToDoList.from_doc(result) if result else None

    async def set_checked_state(
        self,
        doc_id: Union[str, ObjectId],
        item_id: str,
        checked_state: bool,
        session=None,
    ) -> Optional[ToDoList]:
        result = await self._todo_collection.find_one_and_update(
            {"_id": ObjectId(doc_id), "items.id": item_id},
            {"$set": {"items.$.checked": checked_state}},
            session=session,
            return_document=ReturnDocument.AFTER,
        )
        return ToDoList.from_doc(result) if result else None

    async def delete_item(
        self,
        doc_id: Union[str, ObjectId],
        item_id: str,
        session=None,
    ) -> Optional[ToDoList]:
        result = await self._todo_collection.find_one_and_update(
            {"_id": ObjectId(doc_id)},
            {"$pull": {"items": {"id": item_id}}},
            session=session,
            return_document=ReturnDocument.AFTER,
        )
        return ToDoList.from_doc(result) if result else None


