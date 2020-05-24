import argparse
from deeplearning.main.Logger import Logger


class Driver:
    """This class executes the program in the correct mode"""

    def __init__(self):
        """This constructor initializes the class appropriately"""
        self._prepare_args()
        self._prepare_logger()

    def _prepare_args(self):
        """This private method preps the args parser"""
        args_parser = argparse.ArgumentParser(
            description="Indicate whether you want to create or edit a path, "
                        "or run an already existing path from disk")

        # Add the mode argument
        args_parser.add_argument("mode",
                                 choices=[
                                     "edit",
                                     "run"
                                 ],
                                 help="Indicate the execution mode")

        # Parse whatever the user has sent in
        self._args = args_parser.parse_args()

    def _prepare_logger(self):
        """This private method will get the logger up and running"""
        self._logger = Logger()

    def drive(self):
        """This method is the logical entry point for the class"""
        if self._args.mode == "edit":
            self._logger.write_to_log("Starting edit mode")

        if self._args.mode == "run":
            self._logger.write_to_log("Starting run mode")

        # Close the logger now that we're done
        self._logger.close_log()
