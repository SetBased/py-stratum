from pystratum.mssql.wrapper.Wrapper import Wrapper


# ----------------------------------------------------------------------------------------------------------------------
class Row0Wrapper(Wrapper):
    # ------------------------------------------------------------------------------------------------------------------
    def _write_result_handler(self, routine):
        self._write_line('return StaticDataLayer.execute_row0(%s)' % self._generate_command(routine))


# ----------------------------------------------------------------------------------------------------------------------
