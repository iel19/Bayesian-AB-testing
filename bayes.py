# -*- coding: utf-8 -*-

import math
import sys
first_arg = int(sys.argv[1])+1
second_arg = int(sys.argv[2])+1
third_arg = int(sys.argv[3])+1
fourth_arg = int(sys.argv[4])+1

def calc_ab(alpha_a=first_arg, beta_a=second_arg, alpha_b=third_arg, beta_b=fourth_arg):
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

if __name__ == "__main__":
    print calc_ab()
