from typing import Optional

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventStorageScenarioActivateDataStorageScenarioDataAccessorMountPointModel(NestedDataModel):
    windows: Optional[str]
    osx: Optional[str]
    linux: Optional[str]


class FtrackEventStorageScenarioActivateDataStorageScenarioDataAccessorModel(NestedDataModel):
    mount_points: FtrackEventStorageScenarioActivateDataStorageScenarioDataAccessorMountPointModel


class FtrackEventStorageScenarioActivateDataStorageScenarioDataModel(NestedDataModel):
    location_id: str
    location_name: str
    accessor: FtrackEventStorageScenarioActivateDataStorageScenarioDataAccessorModel


class FtrackEventStorageScenarioActivateDataStorageScenarioModel(NestedDataModel):
    data: FtrackEventStorageScenarioActivateDataStorageScenarioDataModel
    scenario: str


class FtrackEventStorageScenarioActivateDataModel(NestedDataModel):
    storage_scenario: FtrackEventStorageScenarioActivateDataStorageScenarioModel


class FtrackEventStorageScenarioActivateModel(FtrackEventBaseModel):
    data: FtrackEventStorageScenarioActivateDataModel
