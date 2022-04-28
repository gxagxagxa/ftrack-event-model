def event_model_factory(event):
    topic = event.get('topic', '')

    if topic == 'ftrack.update':
        import ftrack_event_model.update
        return ftrack_event_model.update.FtrackEventUpdateModel(**event)

    if topic == 'ftrack.meta.connected':
        import ftrack_event_model.meta.connected
        return ftrack_event_model.meta.connected.FtrackEventMetaConnectedModel(**event)

    if topic.startswith('ftrack.action'):
        if topic == 'ftrack.action.discover':
            import ftrack_event_model.action.discover
            return ftrack_event_model.action.discover.FtrackEventActionDiscoverModel(**event)

        if topic == 'ftrack.action.launch':
            import ftrack_event_model.action.launch
            return ftrack_event_model.action.launch.FtrackEventActionLaunchModel(**event)

        if topic == 'ftrack.action.trigger-user-interface':
            import ftrack_event_model.action.trigger_user_interface
            return ftrack_event_model.action.trigger_user_interface.FtrackEventActionTriggerUserInterfaceModel(**event)

    return None
