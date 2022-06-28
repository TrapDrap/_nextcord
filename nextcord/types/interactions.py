"""
The MIT License (MIT)

Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present tag-epic

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Literal, Optional, TypedDict, Union

from .channel import ChannelType
from .components import Component, ComponentType
from .embed import Embed
from .member import Member
from .role import Role
from .snowflake import Snowflake
from .user import User

if TYPE_CHECKING:
    from .message import AllowedMentions, Attachment, Message


ApplicationCommandType = Literal[1, 2, 3]


class _ApplicationCommandOptional(TypedDict, total=False):
    type: ApplicationCommandType
    guild_id: Snowflake
    options: List[ApplicationCommandOption]
    default_permission: bool


class ApplicationCommand(_ApplicationCommandOptional):
    id: Snowflake
    application_id: Snowflake
    name: str
    description: str
    version: Snowflake


class ApplicationCommandOptionChoice(TypedDict):
    name: str
    value: Union[str, int, float]


class _ApplicationCommandOptionOptional(TypedDict, total=False):
    required: bool
    choices: List[ApplicationCommandOptionChoice]
    options: List[ApplicationCommandOption]
    channel_types: List[ChannelType]
    min_value: Union[int, float]
    max_value: Union[int, float]
    autocomplete: bool


ApplicationCommandOptionType = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class ApplicationCommandOption(_ApplicationCommandOptionOptional):
    type: ApplicationCommandOptionType
    name: str
    description: str


ApplicationCommandPermissionType = Literal[1, 2]


class ApplicationCommandPermissions(TypedDict):
    id: Snowflake
    type: ApplicationCommandPermissionType
    permission: bool


class BaseGuildApplicationCommandPermissions(TypedDict):
    permissions: List[ApplicationCommandPermissions]


class PartialGuildApplicationCommandPermissions(BaseGuildApplicationCommandPermissions):
    id: Snowflake


class GuildApplicationCommandPermissions(PartialGuildApplicationCommandPermissions):
    application_id: Snowflake
    guild_id: Snowflake


InteractionType = Literal[1, 2, 3]


class _ApplicationCommandInteractionDataOption(TypedDict):
    name: str


class _ApplicationCommandInteractionDataOptionSubcommand(_ApplicationCommandInteractionDataOption):
    type: Literal[1, 2]
    options: List[ApplicationCommandInteractionDataOption]


class _ApplicationCommandInteractionDataOptionString(_ApplicationCommandInteractionDataOption):
    type: Literal[3]
    value: str


class _ApplicationCommandInteractionDataOptionInteger(_ApplicationCommandInteractionDataOption):
    type: Literal[4]
    value: int


class _ApplicationCommandInteractionDataOptionBoolean(_ApplicationCommandInteractionDataOption):
    type: Literal[5]
    value: bool


class _ApplicationCommandInteractionDataOptionSnowflake(_ApplicationCommandInteractionDataOption):
    type: Literal[6, 7, 8, 9]
    value: Snowflake


class _ApplicationCommandInteractionDataOptionNumber(_ApplicationCommandInteractionDataOption):
    type: Literal[10]
    value: float


ApplicationCommandInteractionDataOption = Union[
    _ApplicationCommandInteractionDataOptionString,
    _ApplicationCommandInteractionDataOptionInteger,
    _ApplicationCommandInteractionDataOptionSubcommand,
    _ApplicationCommandInteractionDataOptionBoolean,
    _ApplicationCommandInteractionDataOptionSnowflake,
    _ApplicationCommandInteractionDataOptionNumber,
]


class ApplicationCommandResolvedPartialChannel(TypedDict):
    id: Snowflake
    type: ChannelType
    permissions: str
    name: str


class ApplicationCommandInteractionDataResolved(TypedDict, total=False):
    users: Dict[Snowflake, User]
    members: Dict[Snowflake, Member]
    roles: Dict[Snowflake, Role]
    channels: Dict[Snowflake, ApplicationCommandResolvedPartialChannel]
    attachments: Dict[Snowflake, Attachment]
    messages: dict[Snowflake, Message]


class _ApplicationCommandInteractionDataOptional(TypedDict, total=False):
    options: List[ApplicationCommandInteractionDataOption]
    resolved: ApplicationCommandInteractionDataResolved
    target_id: Snowflake


class ApplicationCommandInteractionData(_ApplicationCommandInteractionDataOptional):
    id: Snowflake
    name: str
    type: ApplicationCommandType


class _ComponentInteractionDataOptional(TypedDict, total=False):
    values: List[str]
    value: str


class ComponentInteractionData(_ComponentInteractionDataOptional):
    custom_id: str
    component_type: ComponentType


class ModalSubmitActionRowInteractionData(TypedDict):
    type: Literal[1]
    components: List[ComponentInteractionData]


ModalSubmitComponentInteractionData = Union[
    ModalSubmitActionRowInteractionData,
    ComponentInteractionData,
]


class ModalSubmitInteractionData(TypedDict):
    custom_id: str
    components: List[ModalSubmitComponentInteractionData]


InteractionData = Union[
    ApplicationCommandInteractionData, ComponentInteractionData, ModalSubmitInteractionData
]


class _InteractionOptional(TypedDict, total=False):
    data: InteractionData
    guild_id: Snowflake
    channel_id: Snowflake
    member: Member
    user: User
    message: Message
    locale: str
    guild_locale: str


class Interaction(_InteractionOptional):
    id: Snowflake
    application_id: Snowflake
    type: InteractionType
    token: str
    version: int


class InteractionApplicationCommandCallbackData(TypedDict, total=False):
    tts: bool
    content: str
    embeds: List[Embed]
    allowed_mentions: AllowedMentions
    flags: int
    components: List[Component]


InteractionResponseType = Literal[1, 4, 5, 6, 7]


class _InteractionResponseOptional(TypedDict, total=False):
    data: InteractionApplicationCommandCallbackData


class InteractionResponse(_InteractionResponseOptional):
    type: InteractionResponseType


class _EditApplicationCommandOptional(TypedDict, total=False):
    description: str
    options: Optional[List[ApplicationCommandOption]]
    type: ApplicationCommandType


class EditApplicationCommand(_EditApplicationCommandOptional):
    name: str
    default_permission: bool
