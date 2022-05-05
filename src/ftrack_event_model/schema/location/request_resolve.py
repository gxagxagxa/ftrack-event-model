from typing import Optional

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackLocationRequestResolveDataModel(NestedDataModel):
    locationName: str
    platform: str
    componentId: str
    serverUrl: Optional[str]


class FtrackLocationRequestResolveModel(FtrackEventBaseModel):
    data: FtrackLocationRequestResolveDataModel
