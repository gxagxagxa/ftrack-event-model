from typing import List, Optional

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventActionDiscoverDataSelectionEntityModel(NestedDataModel):
    entityId: str
    entityType: str


class FtrackEventActionDiscoverDataSorterModel(NestedDataModel):
    direction: str
    property: str
    root: str


class FtrackEventActionDiscoverDataModel(NestedDataModel):
    selection: Optional[List[FtrackEventActionDiscoverDataSelectionEntityModel]]
    groupers: List
    filters: List
    sorters: List[FtrackEventActionDiscoverDataSorterModel]


class FtrackEventActionDiscoverModel(FtrackEventBaseModel):
    data: FtrackEventActionDiscoverDataModel
