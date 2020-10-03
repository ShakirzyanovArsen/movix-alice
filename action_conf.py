import actions as act

action_config = {
    frozenset(['сделай', 'бочку']): act.do_a_barrel_roll,
    frozenset(['прибавь', 'громкость']): act.volume_inc,
    frozenset(['увеличь', 'громкость']): act.volume_inc,
    frozenset(['увеличить', 'громкость']): act.volume_inc,
    frozenset(['повысь', 'громкость']): act.volume_inc,
    frozenset(['повысить', 'громкость']): act.volume_inc,
    frozenset(['прибавить', 'громкость']): act.volume_inc,
    frozenset(['убавь', 'громкость']): act.volume_dec,
    frozenset(['убавить', 'громкость']): act.volume_dec,
    frozenset(['понизить', 'громкость']): act.volume_dec,
    frozenset(['понизь', 'громкость']): act.volume_dec,
    frozenset(['уменьши', 'громкость']): act.volume_dec,
    frozenset(['уменьшить', 'громкость']): act.volume_dec,
    frozenset(['открой', 'меню']): act.open_menu,
    frozenset(['открыть', 'меню']): act.open_menu,
    frozenset(['включи', 'звук']): act.mute,
    frozenset(['включить', 'звук']): act.mute,
    frozenset(['выключи', 'звук']): act.mute,
    frozenset(['отключи', 'звук']): act.mute,
    frozenset(['выключить', 'звук']): act.mute,
    frozenset(['отключить', 'звук']): act.mute,
    frozenset(['поставь', 'на', 'паузу']): act.pause,
    frozenset(['поставить', 'на', 'паузу']): act.pause,
    frozenset(['сделай', 'паузу']): act.pause,
    frozenset(['сделать', 'паузу']): act.pause,
    frozenset(['останови', 'воспроизведение']): act.pause,
    frozenset(['остановить', 'воспроизведение']): act.pause,
    frozenset(['продолжи', 'воспроизведение']): act.pause,
    frozenset(['продолжить', 'воспроизведение']): act.pause,
    frozenset(['играть', 'далее']): act.pause,
    frozenset(['убери', 'паузу']): act.pause,
    frozenset(['убрать', 'паузу']): act.pause,
    frozenset(['выбрать']): act.ok,
    frozenset(['вернись', 'назад']): act.back,
    frozenset(['верни', 'назад']): act.back,
    frozenset(['вернуть', 'назад']): act.back,
    frozenset(['включи', 'приставку']): act.power,
    frozenset(['включить', 'приставку']): act.power,
    frozenset(['выключи', 'приставку']): act.power,
    frozenset(['отключи', 'приставку']): act.power,
    frozenset(['выключить', 'приставку']): act.power,
    frozenset(['отключить', 'приставку']): act.power,
    frozenset(['включи', 'телевизор']): act.power_tv,
    frozenset(['выключи', 'телевизор']): act.power_tv,
    frozenset(['выключить', 'телевизор']): act.power_tv,
    frozenset(['отключи', 'телевизор']): act.power_tv,
    frozenset(['отключить', 'телевизор']): act.power_tv,
    frozenset(['открой', 'поиск']): act.search,
    frozenset(['открыть', 'поиск']): act.search
}
