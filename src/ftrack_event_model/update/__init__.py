from typing import Optional, List, Dict

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventUpdateSourceUserModel(NestedDataModel):
    id: Optional[str]
    username: Optional[str]


class FtrackEventUpdateDataUserModel(NestedDataModel):
    userid: str
    name: str


class FtrackEventUpdateSourceModel(NestedDataModel):
    id: Optional[str]
    applicationId: Optional[str]
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
    entity_type: Optional[str]
    keys: Optional[List[str]]
    objectTypeId: Optional[str]
    entityType: Optional[str]
    parents: Optional[List[FtrackEventUpdateDataEntityParentModel]]
    parentId: Optional[str]
    action: str
    entityId: Optional[str]
    changes: Optional[Dict[str, FtrackEventUpdateDataEntityChangeOldToNewModel]]


class FtrackEventUpdateDataModel(NestedDataModel):
    entities: List[FtrackEventUpdateDataEntityModel]
    pushToken: Optional[str]
    parents: list[str]
    user: Optional[FtrackEventUpdateDataUserModel]
    clientToken: Optional[str]


class FtrackEventUpdateModel(FtrackEventBaseModel):
    source: FtrackEventUpdateSourceModel
    data: FtrackEventUpdateDataModel
