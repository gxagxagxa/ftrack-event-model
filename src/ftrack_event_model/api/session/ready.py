from ftrack_api.session import Session

from ftrack_event_model.base import FtrackEventBaseModel


class FtrackEventAPISessionReadyDataModel(FtrackEventBaseModel):
    session: Session


class FtrackEventAPISessionReadyModel(FtrackEventBaseModel):
    data: FtrackEventAPISessionReadyDataModel
