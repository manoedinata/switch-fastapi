from pydantic import BaseModel

from typing_extensions import Optional

from swibots import AuthUser

class MeResponse(BaseModel, AuthUser):
    id: Optional[int] = None
    user_name: Optional[str] = None
    name: Optional[str] = None
    creator_name: Optional[str] = None
    verify_email: Optional[bool] = None
    privacy: Optional[str] = None
    is_bot: Optional[bool] = None
    bot_privacy: Optional[str] = None
    profile_colour: Optional[str] = None
    otp: Optional[str] = None
    otp_expiry: Optional[str] = None
    bio: Optional[str] = None
    imageurl: Optional[str] = None
    private_imageurl: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None
    more_about_this: Optional[str] = None
    media1: Optional[str] = None
    media2: Optional[str] = None
    media3: Optional[str] = None
    media4: Optional[str] = None
    media5: Optional[str] = None
    active: Optional[bool] = None
    parent_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
