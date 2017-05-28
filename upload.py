#!/usr/bin/env python

import gym
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('need only an output path')
    gym.upload("{}".format(sys.argv[1]), api_key=os.environ["GYM_API_KEY"])
