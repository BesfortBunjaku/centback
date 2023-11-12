from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_centillion():
    return "centillion app created!"

 