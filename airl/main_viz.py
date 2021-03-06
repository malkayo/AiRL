#!/usr/bin/python

from simulator.environment import Environment
from policy.dqn import DQN
from main_train import Trainer
from simulator.vizsimulator import run_simu
import numpy as np
import timeit

np.set_printoptions(threshold=np.inf, linewidth=200)


# Visualize a policy with the Pygame interface
class Viz_Trainer(Trainer):
    def __init__(self):
        Trainer.__init__(self)

        # Load the policy
        self.params_folder = "./models/"
        self.params_file = "best_model.h5"
        self.estimator_type = "conv"
        
        # Simulation parameters
        self.nb_simu = 1000
        self.n_aircraft = 1
        self.eps = 0.01  # epsillon parameter
        self.valid_actions = ["Straight", "Small Left", "Left", "Small Right", "Right"]
        self.speed = 0.05
        self.airspace_width = 1500  # Airspace width (meters)
        self.airspace_height = 1500  # Airspace height (meters)
        self.wp_heading_bool = False  # Indicate whether waypoints have a heading attribute
        self.random_wp_position_bool = False  # Initialize the waypoint's position randomly

        # number of frames the agent sees before choosing its next action
        self.frame_buffer_size = 3
        self.input_mean = 2.13E-3
        self.input_std = 7.25E-2

    def run(self):
        print "Viz Start"
        env = Environment(self.airspace_width, self.airspace_height)
        state_dimension = (self.frame_buffer_size, ) + env.get_state_dimension()

        # Initialize policy
        self.policy = DQN(
            model_type=self.estimator_type, valid_actions=self.valid_actions,
            state_dimension=state_dimension, eps=self.eps,
            params_file=self.params_file, params_folder=self.params_folder,
            input_mean=self.input_mean, input_std=self.input_std)

        # Run the viz simulator
        for n in range(self.nb_simu):
            print "!!!! Simulation {}".format(n + 1)
            run_simu(self, self.n_aircraft, self.frame_buffer_size,
                     verbose=True,
                     render_bool=True,
                     frame_delay=int(1./(self.speed+1e-6)),
                     wp_heading_bool=self.wp_heading_bool,
                     random_wp_position_bool=self.random_wp_position_bool)


if __name__ == '__main__':
    trainer = Viz_Trainer()
    trainer.run()
