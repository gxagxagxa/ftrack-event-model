from typing import Optional, List

from ftrack_event_model.base import FtrackEventBaseModel, NestedDataModel


class FtrackEventStorageScenarioDiscoverModelDataFilterInitialConfigModel(NestedDataModel):
    disabled: bool
    property: str
    root: str
    id: str


class FtrackEventStorageScenarioDiscoverModelDataFilterModel(NestedDataModel):
    disabled: bool
    property: str
    root: str
    id: str
    initialConfig: FtrackEventStorageScenarioDiscoverModelDataFilterInitialConfigModel


class FtrackEventStorageScenarioDiscoverModelDataModel(NestedDataModel):
    query: str
    groupers: Optional[List]
    sorters: Optional[List]
    filters: List[FtrackEventStorageScenarioDiscoverModelDataFilterModel]


class FtrackEventStorageScenarioDiscoverModel(FtrackEventBaseModel):
    data: FtrackEventStorageScenarioDiscoverModelDataModel
