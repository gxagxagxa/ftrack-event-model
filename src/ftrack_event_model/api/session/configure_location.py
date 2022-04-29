from ftrack_api.session import Session

from ftrack_event_model.base import FtrackEventBaseModel


class FtrackEventAPISessionConfigureLocationDataModel(FtrackEventBaseModel):
    session: Session


class FtrackEventAPISessionConfigureLocationModel(FtrackEventBaseModel):
    data: FtrackEventAPISessionConfigureLocationDataModel
