from typing import List, Optional, Dict

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackActionLaunchDataSelectionEntityModel(NestedDataModel):
    entityId: str
    entityType: str


class FtrackActionLaunchDataModel(NestedDataModel):
    selection: List[FtrackActionLaunchDataSelectionEntityModel]
    actionIdentifier: str
    applicationIdentifier: Optional[str]
    variant: Optional[str]
    integrations: Optional[Dict]
    label: Optional[str]
    host: Optional[str]
    icon: Optional[str]
    description: Optional[str]


class FtrackActionLaunchModel(FtrackEventBaseModel):
    data: FtrackActionLaunchDataModel
