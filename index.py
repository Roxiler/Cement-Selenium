from cement.core.controller import CementBaseController, expose
from cement.core.foundation import CementApp
from cement.core import foundation, backend
from cement.utils.misc import init_defaults

from selenium import webdriver
from conf.config import Config
from conf.datasets import data

from pages.login import Login

import time

# Setting up log files
defaults = init_defaults('intelfarming', 'log.logging')
defaults['log.logging']['file'] = Config.get('log_filename')

# define an application base controller
class IntelFarmingBaseController(CementBaseController):

    class Meta:
        label = 'base'
        description = "FuturAfric IntelFarming"
        epilog = "For help, append --help to the command"
        config_defaults = defaults
        arguments = [
            (['--profile'],
             dict(action='store', help='takes profile name to select the test dataset')),
        ]

    @expose(help="This command tests the whole end to end workflow")
    def endtoend(self):
        """
        This function runs an end to end test cases suits
        """

        if self.app.pargs.profile:
            self.app.log.info("Recieved profile as '%s'." % self.app.pargs.profile)

            # Getting the corresponding profile
            dataset = data.get(self.app.pargs.profile)

            if not dataset:
                self.app.log.error("Invalid profile provided")
                self.app.close()
                exit()

            browser = webdriver.Chrome(Config.get('chromedriver'))
            browser.get(Config.get('siteurl'))

            # Passing only data relevant to login
            login = Login(browser, Config, dataset.get('login')) 
            login.run()

            time.sleep(3)
        else:
            self.app.log.error("No profile received, please provide a profile with --profile PROFILE NAME")


class MyApp(CementApp):
    class Meta:
        label = 'IntelFarming'
        config_defaults=defaults
        handlers = [IntelFarmingBaseController]

with MyApp() as app:
    app.run()



	
