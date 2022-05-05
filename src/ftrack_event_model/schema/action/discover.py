from typing import List, Optional

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackActionDiscoverDataSelectionEntityModel(NestedDataModel):
    entityId: str
    entityType: str


class FtrackActionDiscoverDataSorterModel(NestedDataModel):
    direction: str
    property: str
    root: str


class FtrackActionDiscoverDataModel(NestedDataModel):
    selection: Optional[List[FtrackActionDiscoverDataSelectionEntityModel]]
    groupers: List
    filters: List
    sorters: List[FtrackActionDiscoverDataSorterModel]


class FtrackActionDiscoverModel(FtrackEventBaseModel):
    data: FtrackActionDiscoverDataModel
