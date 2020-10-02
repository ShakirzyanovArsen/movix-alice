import actions as act


action_config = {
    frozenset(['сделай', 'бочку']): act.do_a_barrel_roll,
    frozenset(['сделай', 'штопор']): act.do_a_spin,
    frozenset(['прибавь', 'громкость']): act.volume_inc,
    frozenset(['убавь', 'громкость']): act.volume_dec,
    frozenset(['открой', 'меню']): act.open_menu
}
