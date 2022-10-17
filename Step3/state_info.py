from States import hauntedroom_state, mainentrance_state, skeletonroom_state, shadowfigure_state

states = [{'name':'mainentrance', 'on_exit': ['say_goodbye'], 'on_enter': ['say_hello']}, 
          {'name':'hauntedroom', 'on_exit': ['say_goodbye'], 'on_enter': ['say_hello']},
          {'name':'skeletonroom', 'on_exit': ['say_goodbye'], 'on_enter': ['say_hello']},
          {'name':'shadowfigure', 'on_exit': ['say_goodbye'], 'on_enter': ['say_hello']}
        ]

state_class_dict = {"mainentrance": mainentrance_state.MainEntranceState, 
                    "hauntedroom": hauntedroom_state.HauntedRoomState,
                    "shadowfigure": shadowfigure_state.ShadowFigureState,
                    "skeletonroom": skeletonroom_state.SkeletonRoomState}
transitions=[
    {'trigger': 'west',  'source':'mainentrance', 'dest':'shadowfigure'},
    {'trigger': 'south', 'source':'mainentrance', 'dest':'hauntedroom'},
    {'trigger': 'north', 'source':'mainentrance', 'dest':'skeletonroom'},
    {'trigger': 'north', 'source':'skeletonroom', 'dest':'skeletonroom'},
    {'trigger': 'south', 'source':'skeletonroom', 'dest':'mainentrance'},
    {'trigger': 'east',  'source':'shadowfigure','dest':'mainentrance'},
    {'trigger': 'north', 'source':'hauntedroom', 'dest':'mainentrance'}
    ]