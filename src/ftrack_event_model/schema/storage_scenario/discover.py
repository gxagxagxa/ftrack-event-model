from typing import Optional, List

from ftrack_event_model.schema.base import FtrackEventBaseModel, NestedDataModel


class FtrackStorageScenarioDiscoverModelDataFilterInitialConfigModel(NestedDataModel):
    disabled: bool
    property: str
    root: str
    id: str


class FtrackStorageScenarioDiscoverModelDataFilterModel(NestedDataModel):
    disabled: bool
    property: str
    root: str
    id: str
    initialConfig: FtrackStorageScenarioDiscoverModelDataFilterInitialConfigModel


class FtrackStorageScenarioDiscoverModelDataModel(NestedDataModel):
    query: str
    groupers: Optional[List]
    sorters: Optional[List]
    filters: List[FtrackStorageScenarioDiscoverModelDataFilterModel]


class FtrackStorageScenarioDiscoverModel(FtrackEventBaseModel):
    data: FtrackStorageScenarioDiscoverModelDataModel
