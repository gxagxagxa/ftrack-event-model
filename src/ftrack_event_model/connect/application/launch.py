from typing import List, Dict, Callable, Optional, Union

from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel, FtrackEventBaseSourceModel


class FtrackEventConnectApplicationLaunchDataOptionEnvModel(NestedDataModel):
    __root__: Dict[str, str]


class FtrackEventConnectApplicationLaunchDataOptionModel(NestedDataModel):
    env: FtrackEventConnectApplicationLaunchDataOptionEnvModel
    close_fds: bool
    cwd: str
    preexec_fn: Optional[Callable]


class FtrackEventConnectApplicationLaunchDataApplicationModel(NestedDataModel):
    identifier: str
    path: str
    launchArguments: Optional[str]
    version: Union[Callable, str]
    label: Optional[str]
    icon: Optional[str]
    variant: Optional[str]
    description: Optional[str]
    integrations: Optional[Dict]


class FtrackEventConnectApplicationLaunchDataContextModel(NestedDataModel):
    actionIdentifier: str
    label: Optional[str]
    variant: Optional[str]
    description: Optional[str]
    icon: Optional[str]
    applicationIdentifier: str
    host: Optional[str]
    selection: List
    source: FtrackEventBaseSourceModel


class FtrackEventConnectApplicationLaunchDataIntegrationModel(NestedDataModel):
    name: Optional[str]
    version: Optional[str]
    env: Optional[Dict]
    launch_arguments: Optional[List]


class FtrackEventConnectApplicationLaunchDataModel(NestedDataModel):
    command: List[str]
    options: FtrackEventConnectApplicationLaunchDataOptionModel
    application: FtrackEventConnectApplicationLaunchDataApplicationModel
    context: FtrackEventConnectApplicationLaunchDataContextModel
    integration: FtrackEventConnectApplicationLaunchDataIntegrationModel


class FtrackEventConnectApplicationLaunchModel(FtrackEventBaseModel):
    data: FtrackEventConnectApplicationLaunchDataModel
