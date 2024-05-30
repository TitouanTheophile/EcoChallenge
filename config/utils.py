
def extract_conf(conf):
    nb_exec = conf.get("nb_exec")
    scenarios = conf.get("scenarios")
    return (nb_exec, scenarios)