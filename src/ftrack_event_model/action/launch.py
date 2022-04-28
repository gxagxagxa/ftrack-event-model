from typing import List, Optional, Dict

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventActionLaunchDataSelectionEntityModel(NestedDataModel):
    entityId: str
    entityType: str


class FtrackEventActionLaunchDataModel(NestedDataModel):
    selection: List[FtrackEventActionLaunchDataSelectionEntityModel]
    actionIdentifier: str
    applicationIdentifier: Optional[str]
    variant: Optional[str]
    integrations: Optional[Dict]
    label: Optional[str]
    host: Optional[str]
    icon: Optional[str]
    description: Optional[str]


class FtrackEventActionLaunchModel(FtrackEventBaseModel):
    data: FtrackEventActionLaunchDataModel
