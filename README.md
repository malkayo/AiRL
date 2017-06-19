# AiRL
AiRL is a project that aims at guiding several aircraft to their destination using Reinforcement Learning and Deep Learning.

Multiple agents base their decisions on a succession of 60x60 grids representing the airspace and chose which direction to go next. The policies used so far are some variants of [DQN](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf "DQN Paper")   including some improvements like prioritized replay, adaptive normalization and Monte Carlo learning.

I (foolishly) developed the environment "simulator" code and the Deep Learning part (convolutional networks) was coded with [Keras](https://keras.io/ "Keras") .

Because pictures are better than words a PyGame interface is available ([Video](https://youtu.be/a0b6hNB-CpQ "Cool Video")).

The project report (in airl/doc) gives a lot of details about the implementation of the project and some experiments. The report's code and pre-trained models can be found [here](https://github.com/malkayo/AiRL-Report "Report Files").

__Disclaimer__: this project was developed for the completion of my [Udacity Machine Learning Engineer Degree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009 "Udacity") using online resources from [Stanford CS231n](http://cs231n.stanford.edu/ "CS231n") and [UCL Reinforcement Learning](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html "Silver") courses. The code is meant for experimentation purposes only.

DOI: 10.5281/zenodo.810771
