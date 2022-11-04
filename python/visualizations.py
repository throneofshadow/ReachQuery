import pdb
import matplotlib.pyplot as plt


class SingleReachViz:
    def __init__(self, dataframe, hand, path_to_save):
        self.data = dataframe
        self.hand = hand
        self.right_hand_positions, self.left_hand_positions, self.right_hand_speeds, self.left_hand_speeds = None, None, None, None
        self.left_palm_speed, self.right_palm_speed, self.right_palm_pos, self.left_palm_pos = None, None, None, None
        self.handle, self.nose, self.handle_s, self.nose_s = None, None, None, None
        self.save_path = path_to_save
        self.plot_palm_speeds()

    def plot_palm_speeds(self):
        plt.plot(self.data['Left Palm S'], color='r', label='Left Palm S')
        plt.plot(self.data['Right Palm S'], color='g', label='Right Palm S')
        pdb.set_trace()

