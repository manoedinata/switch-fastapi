from pydantic import BaseModel

from typing_extensions import Optional
from typing_extensions import List

from swibots import UserTournament
from swibots import User

class UserInput(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None

class UserTournament(BaseModel, UserTournament):
    id: Optional[str] = None
    type: Optional[type] = None
    name: Optional[str] = None
    user_id: Optional[str] = None
    xp_earned: Optional[int] = None

class UserResponse(BaseModel, User):
    id: Optional[int] = None
    name: Optional[str] = None
    bio: Optional[str] = None
    user_name: Optional[str] = None
    imageurl: Optional[str] = None
    active: Optional[bool] = None
    deleted: Optional[bool] = None
    roleInfo: Optional[str] = None
    link: Optional[str] = None
    admin: Optional[bool] = None
    is_bot: Optional[bool] = None
    is_game: Optional[bool] = None
    is_friend: Optional[bool] = None
    tournamentsParticipated: Optional[List[UserTournament]] = None
