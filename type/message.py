from pydantic import BaseModel

from typing_extensions import Optional
from typing_extensions import List

from swibots import Message
from swibots import EmbedInlineField
from swibots import EmbeddedMedia
from swibots import InlineKeyboardButton
from swibots import InlineMarkup

class EmbedInlineField(BaseModel, EmbedInlineField):
    icon: Optional[str] = None
    key: Optional[str] = None
    title: Optional[str] = None

class EmbeddedMedia(BaseModel, EmbeddedMedia):
    thumbnail: str
    description: Optional[str] = None
    footer_icon: Optional[str] = None
    footer_title: Optional[str] = None
    header_icon: Optional[str] = None
    header_name: Optional[str] = None
    inline_fields: Optional[List[List["EmbedInlineField"]]] = None
    title: Optional[str] = None

class InlineKeyboardButton(BaseModel, InlineKeyboardButton):
    text: Optional[str] = None
    url: Optional[str] = None
    callback_data: Optional[str] = None
    game: Optional[bool] = False
    app: Optional[bool] = False

class InlineMarkup(BaseModel, InlineMarkup):
    inline_keyboard: List[List["InlineKeyboardButton"]] = None,

class SendMessageInput(BaseModel, Message):
    message: str
    community_id: str = None
    channel_id: str = None
    group_id: str = None
    user_id: Optional[int] = None
    user_session_id: Optional[str] = None
    document: Optional[str] = None
    caption: Optional[str] = None
    description: Optional[str] = None
    embed_message: Optional[EmbeddedMedia] = None
    inline_markup: Optional[InlineMarkup] = None
    reply_to_message_id: Optional[int] = None
