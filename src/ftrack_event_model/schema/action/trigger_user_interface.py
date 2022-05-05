from typing import List, Optional

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackActionLaunchDataSelectionEntityModel(NestedDataModel):
    entityId: str
    entityType: str


class FtrackActionTriggerUserInterfaceDataModel(NestedDataModel):
    selection: List[FtrackActionLaunchDataSelectionEntityModel]
    actionIdentifier: str
    label: Optional[str]
    description: Optional[str]


class FtrackActionTriggerUserInterfaceModel(FtrackEventBaseModel):
    data: FtrackActionTriggerUserInterfaceDataModel
