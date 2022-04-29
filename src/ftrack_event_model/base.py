from typing import Any, Dict, Optional

from pydantic import BaseModel


class NestedDataModel(BaseModel):
    def __init__(__pydantic_self__, *args: Optional[Dict], **data: Any) -> None:
        if (args) and (not data):
            super().__init__(**(args[0]))
        else:
            super().__init__(**data)


class FtrackEventBaseSourceUserModel(NestedDataModel):
    username: Optional[str]
    id: Optional[str]


class FtrackEventBaseSourceModel(NestedDataModel):
    id: Optional[str]
    applicationId: Optional[str]
    user: Optional[FtrackEventBaseSourceUserModel]


class FtrackEventBaseModel(NestedDataModel):
    id: str
    topic: str
    sent: Optional[str]
    source: Any
    target: Optional[str]
    in_reply_to_event: Any
    data: Any
