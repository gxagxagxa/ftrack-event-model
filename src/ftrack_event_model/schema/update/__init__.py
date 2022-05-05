from typing import Optional, List, Dict

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackUpdateSourceUserModel(NestedDataModel):
    id: Optional[str]
    username: Optional[str]


class FtrackUpdateDataUserModel(NestedDataModel):
    userid: str
    name: str


class FtrackUpdateSourceModel(NestedDataModel):
    id: Optional[str]
    applicationId: Optional[str]
    user: FtrackUpdateSourceUserModel


class FtrackUpdateDataEntityParentModel(NestedDataModel):
    entityId: str
    entityType: str
    entity_type: str
    parentId: Optional[str]


class FtrackUpdateDataEntityChangeOldToNewModel(NestedDataModel):
    old: Optional[str]
    new: Optional[str]


class FtrackUpdateDataEntityModel(NestedDataModel):
    entity_type: Optional[str]
    keys: Optional[List[str]]
    objectTypeId: Optional[str]
    entityType: Optional[str]
    parents: Optional[List[FtrackUpdateDataEntityParentModel]]
    parentId: Optional[str]
    action: str
    entityId: Optional[str]
    changes: Optional[Dict[str, FtrackUpdateDataEntityChangeOldToNewModel]]


class FtrackUpdateDataModel(NestedDataModel):
    entities: List[FtrackUpdateDataEntityModel]
    pushToken: Optional[str]
    parents: list[str]
    user: Optional[FtrackUpdateDataUserModel]
    clientToken: Optional[str]


class FtrackUpdateModel(FtrackEventBaseModel):
    source: FtrackUpdateSourceModel
    data: FtrackUpdateDataModel
