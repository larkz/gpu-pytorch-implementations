from opt.value_estimator import *
from environment.MarketEnv import *
from common.RangeMap import *
import numpy as np
from opt.bbo_sim_anneal import *


STATE_DIM = 2
ACTION_DIM = 11
BATCH_SIZE = 200

marketEnv = MarketEnv(action_size = ACTION_DIM, max_price = 100, max_inventory = 5, n_agents = 3)

range_dict = {
    (0, 10): 0.10,
    (10, 20): 0.10,
    (20, 30): 0.10,
    (30, 40): 0.10,
    (40, 50): 0.10,
    (50, 60): 0.10,
    (60, 70): 0.10,
    (70, 80): 0.10,
    (80, 90): 0.10,
    (90, 100): 0.10,
}

policy_dic = RangeMapDict(range_dict)

perturb_policy(policy_dic)
