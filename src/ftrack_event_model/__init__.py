def event_model_factory(event):
    topic = event.get('topic', '')

    if topic == 'ftrack.update':
        import ftrack_event_model.update
        return ftrack_event_model.update.FtrackEventUpdateModel(**event)

    if topic.startswith('ftrack.meta'):
        if topic == 'ftrack.meta.connected':
            import ftrack_event_model.meta.connected
            return ftrack_event_model.meta.connected.FtrackEventMetaConnectedModel(**event)

    if topic.startswith('ftrack.api'):
        if topic.startswith('ftrack.api.session'):
            if topic == 'ftrack.api.session.configure-location':
                import ftrack_event_model.api.session.configure_location
                return ftrack_event_model.api.session.configure_location.FtrackEventAPISessionConfigureLocationModel(
                    **event)
            if topic == 'ftrack.api.session.ready':
                import ftrack_event_model.api.session.ready
                return ftrack_event_model.api.session.ready.FtrackEventAPISessionReadyModel(**event)
            if topic == 'ftrack.api.session.construct-entity-type':
                import ftrack_event_model.api.session.construct_entity_type
                return ftrack_event_model.api.session.construct_entity_type.FtrackEventAPISessionConstructEntityTypeModel(
                    **event)

    if topic.startswith('ftrack.storage-scenario'):
        if topic == 'ftrack.storage-scenario.discover':
            import ftrack_event_model.storage_scenario.discover
            return ftrack_event_model.storage_scenario.discover.FtrackEventStorageScenarioDiscoverModel(**event)
        if topic == 'ftrack.storage-scenario.configure':
            import ftrack_event_model.storage_scenario.configure
            return ftrack_event_model.storage_scenario.configure.FtrackEventStorageScenarioConfigureModel(**event)
        if topic == 'ftrack.storage-scenario.configure-done':
            import ftrack_event_model.storage_scenario.configure_done
            return ftrack_event_model.storage_scenario.configure_done.FtrackEventStorageScenarioConfigureDoneModel(
                **event)
        if topic == 'ftrack.storage-scenario.activate':
            import ftrack_event_model.storage_scenario.activate
            return ftrack_event_model.storage_scenario.activate.FtrackEventStorageScenarioActivateModel(**event)

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

    if topic.startswith('ftrack.location'):
        if topic == 'ftrack.location.component-added':
            import ftrack_event_model.location.component_added
            return ftrack_event_model.location.component_added.FtrackEventLocationComponentAddedModel(**event)
        if topic == 'ftrack.location.request-resolve':
            import ftrack_event_model.location.request_resolve
            return ftrack_event_model.location.request_resolve.FtrackEventLocationRequestResolveModel(**event)

    return None
