# -*- coding: utf-8 -*-

import math
import pandas as pd

def calc_ab(alpha_a, beta_a, alpha_b, beta_b):
    # see evanmiller.org/bayesian-ab-testing.html
    # αA number of successes for A
    # βA number of failures for A
    # αB number of successes for B
    # βB number of failures for B

    total = 0.0
    for i in range(alpha_b):
        num = math.lgamma(alpha_a+i) + math.lgamma(beta_a+beta_b) + math.lgamma(1+i+beta_b) + math.lgamma(alpha_a+beta_a)
        den = math.log(beta_b+i) + math.lgamma(alpha_a+i+beta_a+beta_b) + math.lgamma(1+i) + math.lgamma(beta_b) + math.lgamma(alpha_a) + math.lgamma(beta_a)
        total += math.exp(num - den)
    return total

df = pd.read_csv('test_AB_data.csv')
df['p'] = 0.0
df['p'] = df.apply(lambda x: calc_ab(x['success_false']+1,x['fail_false']+1,x['success_true']+1,x['fail_true']+1), axis=1)

print df

df.to_csv('test2.csv')