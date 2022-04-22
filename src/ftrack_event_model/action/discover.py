from typing import Dict, List

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventActionDiscoverDataSelectionEntityModel(NestedDataModel):
    entityId: str
    entityType: str


class FtrackEventActionDiscoverDataSorterModel(NestedDataModel):
    direction: str
    property: str
    root: str


class FtrackEventActionDiscoverDataModel(NestedDataModel):
    selection: List[FtrackEventActionDiscoverDataSelectionEntityModel]
    groupers: List[Dict[str, str]]
    filters: List
    sorters: List[FtrackEventActionDiscoverDataSorterModel]


class FtrackEventActionDiscoverModel(FtrackEventBaseModel):
    data: FtrackEventActionDiscoverDataModel
