import actions as act

action_config = {
    frozenset(['сделай', 'бочку']): act.do_a_barrel_roll,
    frozenset(['прибавь', 'громкость']): act.volume_inc,
    frozenset(['убавь', 'громкость']): act.volume_dec,
    frozenset(['открой', 'меню']): act.open_menu,
    frozenset(['включи', 'звук']): act.mute,
    frozenset(['выключи', 'звук']): act.mute,
    frozenset(['поставь', 'на', 'паузу']): act.pause,
    frozenset(['продолжи', 'воспроизведение']): act.pause,
    frozenset(['выбрать']): act.ok,
    frozenset(['вернись', 'назад']): act.back,
    frozenset(['включи', 'приставку']): act.power,
    frozenset(['выключи', 'приставку']): act.power,
    frozenset(['включи', 'телевизор']): act.power_tv,
    frozenset(['выключи', 'телевизор']): act.power_tv,
    frozenset(['открой', 'поиск']): act.search,
}
