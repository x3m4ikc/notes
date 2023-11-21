from fastapi import APIRouter, Depends, Query, status

from auth.auth import current_user
from models.models import User
from schemas.schemas import NoteModel
from services.crud import create_note_crud, delete_note_crud, edit_note_crud, list_notes_crud

router = APIRouter(prefix="/note", tags=["Notes"])


@router.post("/", name="create_note", status_code=status.HTTP_201_CREATED, response_model=NoteModel)
async def create_note(user: User = Depends(current_user), title: str = Query(), content: str = Query()):
    note_obj = await create_note_crud(title, content, user.id)
    return note_obj


@router.patch("/", name="edit_note", status_code=status.HTTP_200_OK)
async def edit_note(
    user: User = Depends(current_user), title: str = Query(), content: str = Query(), note_id: int = Query()
):
    note_obj = await edit_note_crud(title, content, note_id, user.id)
    return note_obj


@router.delete("/", name="delete_note", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(user: User = Depends(current_user), note_id: int = Query()):
    is_success = await delete_note_crud(note_id, user.id)
    return {"status": is_success}


@router.get("/", name="list_notes", status_code=status.HTTP_200_OK)
async def list_notes(user: User = Depends(current_user), limit: int = 10, offset: int = 0):
    return [note for note in await list_notes_crud(user.id, limit, offset)]
