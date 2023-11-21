from fastapi import HTTPException, status
from sqlalchemy import select

from db.database import async_session
from models.models import Note


async def create_note_crud(title, content, user_id):
    async with async_session() as session:
        note_obj = Note(title=title, content=content, user_id=user_id)
        session.add(note_obj)
        await session.commit()
        await session.refresh(note_obj)
    return note_obj


async def edit_note_crud(title, content, note_id, user_id):
    async with async_session() as session:
        note_obj = await session.get(Note, note_id)
        if not user_id == note_obj.user_id:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="You can not edit this note, this one is not yours",
            )
        note_obj.title = title
        note_obj.content = content
        await session.commit()
        return note_obj


async def delete_note_crud(note_id, user_id):
    async with async_session() as session:
        note_obj = await session.get(Note, note_id)
        if not note_obj:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You can not delete this note, it does not exist",
            )
        if not user_id == note_obj.user_id:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="You can not delete this note, this one is not yours",
            )
        await session.delete(note_obj)
        await session.commit()
        return True


async def list_notes_crud(user_id, limit, offset):
    async with async_session() as session:
        statement = select(Note).where(Note.user_id == user_id).offset(offset).limit(limit)
        result = await session.execute(statement)
        await session.commit()
        return result.scalars()
