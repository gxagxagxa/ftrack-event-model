from typing import Optional

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventLocationRequestResolveDataModel(NestedDataModel):
    locationName: str
    platform: str
    componentId: str
    serverUrl: Optional[str]


class FtrackEventLocationRequestResolveModel(FtrackEventBaseModel):
    data: FtrackEventLocationRequestResolveDataModel
