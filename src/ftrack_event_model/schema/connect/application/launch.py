from typing import List, Dict, Callable, Optional, Union

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel, FtrackBaseSourceModel


class FtrackConnectApplicationLaunchDataOptionEnvModel(NestedDataModel):
    __root__: Dict[str, str]


class FtrackConnectApplicationLaunchDataOptionModel(NestedDataModel):
    env: FtrackConnectApplicationLaunchDataOptionEnvModel
    close_fds: bool
    cwd: str
    preexec_fn: Optional[Callable]


class FtrackConnectApplicationLaunchDataApplicationModel(NestedDataModel):
    identifier: str
    path: str
    launchArguments: Optional[str]
    version: Union[Callable, str]
    label: Optional[str]
    icon: Optional[str]
    variant: Optional[str]
    description: Optional[str]
    integrations: Optional[Dict]


class FtrackConnectApplicationLaunchDataContextModel(NestedDataModel):
    actionIdentifier: str
    label: Optional[str]
    variant: Optional[str]
    description: Optional[str]
    icon: Optional[str]
    applicationIdentifier: str
    host: Optional[str]
    selection: List
    source: FtrackBaseSourceModel


class FtrackConnectApplicationLaunchDataIntegrationModel(NestedDataModel):
    name: Optional[str]
    version: Optional[str]
    env: Optional[Dict]
    launch_arguments: Optional[List]


class FtrackConnectApplicationLaunchDataModel(NestedDataModel):
    command: List[str]
    options: FtrackConnectApplicationLaunchDataOptionModel
    application: FtrackConnectApplicationLaunchDataApplicationModel
    context: FtrackConnectApplicationLaunchDataContextModel
    integration: FtrackConnectApplicationLaunchDataIntegrationModel


class FtrackConnectApplicationLaunchModel(FtrackEventBaseModel):
    data: FtrackConnectApplicationLaunchDataModel
