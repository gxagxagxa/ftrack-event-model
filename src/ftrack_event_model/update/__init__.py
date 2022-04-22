from typing import Optional, List, Dict

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventUpdateSourceUserModel(NestedDataModel):
    id: str
    username: str


class FtrackEventUpdateDataUserModel(NestedDataModel):
    userid: str
    name: str


class FtrackEventUpdateSourceModel(NestedDataModel):
    id: str
    applicationId: str
    user: FtrackEventUpdateSourceUserModel


class FtrackEventUpdateDataEntityParentModel(NestedDataModel):
    entityId: str
    entityType: str
    entity_type: str
    parentId: Optional[str]


class FtrackEventUpdateDataEntityChangeOldToNewModel(NestedDataModel):
    old: Optional[str]
    new: Optional[str]


class FtrackEventUpdateDataEntityModel(NestedDataModel):
    entity_type: str
    keys: List[str]
    objectTypeId: str
    entityType: str
    parents: List[FtrackEventUpdateDataEntityParentModel]
    parentId: Optional[str]
    action: str
    entityId: str
    changes: Dict[str, FtrackEventUpdateDataEntityChangeOldToNewModel]


class FtrackEventUpdateDataModel(NestedDataModel):
    entities: List[FtrackEventUpdateDataEntityModel]
    pushToken: str
    parents: list[str]
    user: FtrackEventUpdateDataUserModel
    clientToken: str


class FtrackEventUpdateModel(FtrackEventBaseModel):
    source: FtrackEventUpdateSourceModel
    data: FtrackEventUpdateDataModel
