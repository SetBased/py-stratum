from pystratum.mssql.wrapper.Wrapper import Wrapper


# ----------------------------------------------------------------------------------------------------------------------
class LogWrapper(Wrapper):
    # ------------------------------------------------------------------------------------------------------------------
    def _write_result_handler(self, routine):
        self._write_line('return StaticDataLayer.execute_log(%s)' % self._generate_command(routine))


# ----------------------------------------------------------------------------------------------------------------------
