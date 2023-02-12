import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="D:\\Automation Notes\\Python Project\\pythonProject\\SVproject\\Logs\\automations.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger