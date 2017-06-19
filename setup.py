from setuptools import setup

setup(name='airl',
      version='0.1dev',
      description='Reinforcement Learning applied to a toy transportation problem',
      long_description=open('README.txt').read(),
      url='https://github.com/malkayo/AiRL',
      author='Yoni Malka',
      author_email='yoni.s.malka@gmail.com',
      license='MIT',
      packages=['airl', 'airl.experience', 'airl.policy', 'airl.simulator'],
      install_requires=['numpy', 'keras', 'pandas', 'scipy', 'h5py'],
      include_package_data=True)
