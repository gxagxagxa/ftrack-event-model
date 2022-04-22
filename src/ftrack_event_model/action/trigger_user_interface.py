from typing import List, Optional

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventActionLaunchDataSelectionEntityModel(NestedDataModel):
    entityId: str
    entityType: str


class FtrackEventActionTriggerUserInterfaceDataModel(NestedDataModel):
    selection: List[FtrackEventActionLaunchDataSelectionEntityModel]
    actionIdentifier: str
    label: Optional[str]
    description: Optional[str]


class FtrackEventActionTriggerUserInterfaceModel(FtrackEventBaseModel):
    data: FtrackEventActionTriggerUserInterfaceDataModel
