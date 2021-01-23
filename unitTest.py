import unittest
import vehicle_simulator


class UnitTest(unittest.TestCase):
    def test_autonomous_vehicle_command_menu(self):
        with self.assertRaises(Exception) as context:
            # function does not take parameters
            param = "check-1-2"
            vehicle_simulator.autonomous_vehicle_command_menu(param)
            param_num = 38573295739570350785027359758375298759237598
            vehicle_simulator.autonomous_vehicle_command_menu(param_num)
            vehicle_simulator.autonomous_vehicle_command_menu(None)

    def test_set_a_dest(self):
        with self.assertRaises(Exception) as context:
            # function does not take parameters
            param = "check-1-2"
            vehicle_simulator.set_a_dest(param)
            param_num = 38573295739570350785027359758375298759237598
            vehicle_simulator.set_a_dest(param_num)
            vehicle_simulator.set_a_dest(None)

    def test_get_vehicle(self):
        with self.assertRaises(Exception) as context:
            # function does not take parameters
            param = "check-1-2"
            vehicle_simulator.get_vehicle(param)
            param_num = 38573295739570350785027359758375298759237598
            vehicle_simulator.get_vehicle(param_num)
            vehicle_simulator.get_vehicle(None)

    def test_check_for_order(self):
        with self.assertRaises(Exception) as context:
            # function does not take parameters
            param = "check-1-2"
            vehicle_simulator.check_for_order(param)
            param_num = 38573295739570350785027359758375298759237598
            vehicle_simulator.check_for_order(param_num)
            vehicle_simulator.check_for_order(None)

    def test_print_pending_orders(self):
        with self.assertRaises(Exception) as context:
            # Takes 1 argument
            vehicle_simulator.print_pending_orders()
            nonsense = "asfasfasf"
            vehicle_simulator.print_pending_orders(nonsense)
            more_nonesense = 23530754308345438523742985757962597597598723572
            vehicle_simulator.print_pending_orders(more_nonesense)
            vehicle_simulator.print_pending_orders(None)

    def test_get_route(self):
        with self.assertRaises(Exception) as context:
            # Takes 4 arguments
            vehicle_simulator.get_route()
            nonsense = "asfasfasf"
            vehicle_simulator.get_route(nonsense, nonsense, nonsense, nonsense)
            num0, num1, num2, num3  = 23, 325, 235, 1
            vehicle_simulator.get_route(num0, num1, num2, num3)
            vehicle_simulator.get_route(None, None, None, None)

    def test_parse_duration_into_list(self):
        with self.assertRaises(Exception) as context:
            # Takes 1 argument
            vehicle_simulator.parse_duration_into_list()
            nonsense = "asfasfasf"
            vehicle_simulator.parse_duration_into_list(nonsense)
            more_nonesense = 23530754308345438523742985757962597597598723572
            vehicle_simulator.parse_duration_into_list(more_nonesense)
            vehicle_simulator.parse_duration_into_list(None)

    def test_parse_lat_and_long_into_list(self):
        with self.assertRaises(Exception) as context:
            # Takes 1 argument
            vehicle_simulator.parse_lat_and_long_into_list()
            nonsense = "asfasfasf"
            vehicle_simulator.parse_lat_and_long_into_list(nonsense)
            more_nonesense = 23530754308345438523742985757962597597598723572
            vehicle_simulator.parse_lat_and_long_into_list(more_nonesense)
            vehicle_simulator.parse_lat_and_long_into_list(None)

    def test_simulate_instance(self):
        with self.assertRaises(Exception) as context:
            # Takes 4 arguments
            vehicle_simulator.simulate_instance()
            nonsense = "asfasfasf"
            vehicle_simulator.simulate_instance(nonsense, nonsense, nonsense, nonsense)
            num0, num1, num2, num3  = 23, 325, 235, 1
            # yes, I should do this in a for loop
            vehicle_simulator.simulate_instance(num0, num1, num2, num3)
            vehicle_simulator.simulate_instance(num0, None, None, None)
            vehicle_simulator.simulate_instance(None, num1, None, None)
            vehicle_simulator.simulate_instance(None, None, num2, None)
            vehicle_simulator.simulate_instance(None, None, None, num3)
            vehicle_simulator.simulate_instance(nonsense, None, None, None)
            vehicle_simulator.simulate_instance(None, nonsense, None, None)
            vehicle_simulator.simulate_instance(None, None, nonsense, None)
            vehicle_simulator.simulate_instance(None, None, None, nonsense)

    def test_update_vehicle_coordinates(self):
        with self.assertRaises(Exception) as context:
            # Takes 3 arguments
            vehicle_simulator.update_vehicle_coordinates()
            nonsense = "asfasfasf"
            vehicle_simulator.update_vehicle_coordinates(nonsense, nonsense, nonsense)
            vehicle_simulator.update_vehicle_coordinates(None, None, None)

    def test_start_TaaS(self):
        with self.assertRaises(Exception) as context:
            # Takes 1 arguments
            vehicle_simulator.start_TaaS()
            nonsense = "asfasfasf"
            vehicle_simulator.start_TaaS(nonsense)
            more_nonesense = 23530754308345438523742985757962597597598723572
            vehicle_simulator.start_TaaS(more_nonesense)
            vehicle_simulator.start_TaaS(None)

    def test_vSim(self):
        with self.assertRaises(Exception) as context:
            # Takes 1 arguments
            nonsense = "asfasfasf"
            vehicle_simulator.vSim(nonsense)
            more_nonesense = 23530754308345438523742985757962597597598723572
            vehicle_simulator.vSim(more_nonesense)
            vehicle_simulator.vSim(None)


if __name__ == '__main__':
    unittest.main()