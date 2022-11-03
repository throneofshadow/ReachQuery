import pandas as pd
import cv2
import numpy as np
import os
from visualizations import SingleReachViz


def import_file(path_to_csv, use_index=False):
    return pd.read_csv(path_to_csv, index_col=use_index)


class BlockQuery:
    def __init__(self, dir_path, rat, date, session, fps=10):
        self.cap, self.data, self.prediction_file = None, None, None
        self.single_reach_video_images, self.single_reach_query_data, self.single_reach_query_predictions = None, None, None
        self.load_path, self.fps, self.video_width, self.video_height, self.fps = None, None, None, None, fps
        self.dir_path = dir_path
        self.rat = rat
        self.date = date
        self.session = session
        self.load_data_from_main_path()

    def load_data_from_main_path(self):
        self.load_path = self.dir_path + '\\' + self.rat + '\\' + self.date + '\\' + self.session + '\\'
        video_dir = 'classification_videos'
        current_path = os.getcwd()
        data_path = self.load_path + 'data.csv'
        os.chdir(self.load_path)
        for file in os.listdir(video_dir):
            if file.endswith('.mp4') and 'LabLabel' in file:
                self.cap = cv2.VideoCapture('classification_videos\\' + file)
                self.video_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                self.video_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            if file.endswith('.csv'):
                self.prediction_file = import_file('classification_videos\\' + file)
        os.chdir(current_path)  # Set path back
        self.data = import_file(data_path)

    def query_over_block(self, hand_query=False, grasp_query=False, tug_query=False):
        row_= 0
        for row in self.prediction_file.iterrows():
            if row[1][1] > 0:
                lb = row[1][1]
                ub = row[1][2]
                grasps = row[1][3]
                ind_grasps = grasps.split(',')
                num_grasps = len(ind_grasps)
                hand = row[1][4]
                tug = row[1][5]
                notes = row[1][6]
                row_ += 1
                if notes:
                    break
                else:
                    # Extract data if conditions are met (use hand, tug, and num_grasps)
                    self.load_data_from_boundaries(lb, ub, row_)
                    # Do things here (plot data, save a cut video into a directory named reaches)

    def load_data_from_boundaries(self, bound_lower, bound_upper, idd, save_video=True):
        """ Function to load reaching video data (.mp4) from reaching videos. This function requires an upper and
            lower bound, in frame numbers eg. 34567.
            Inputs
            --------
            bound_lower: int, lower bound to extract images from video stack
            bound_upper: int, upper bound to extract images from video stack

        """
        self.single_reach_video_images = self.read_images_to_array_opencv(bound_lower, bound_upper)
        if save_video:
            self.cut_reaching_video(idd)
        self.single_reach_query_data = self.data[bound_lower, bound_upper]

        SingleReachViz(self.single_reach_query_data)  # Create single-reach visualizations

    def read_images_to_array_opencv(self, bound_lower, bound_upper):
        images = []
        ret = True
        self.cap.set(bound_lower, bound_upper)
        while ret:
            ret, img = self.cap.read()
            if ret:
                images.append(img)
        return np.stack(images, axis=0)

    def cut_reaching_video(self, reach_number, fps):
        if not os.path.exists(self.load_path+'\\classification_videos\\trial_videos'):
            os.makedirs(self.load_path+'\\classification_videos\\trial_videos')
        out = cv2.VideoWriter('reach_' + str(reach_number) + 'video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps,
                              (self.video_width, self.video_height), False)
        for i in range(self.single_reach_video_images.shape[0]):
            out.write(self.single_reach_video_images[i, :, :])  # Write numpy data to video.
        out.release()

    def find_peak_time(self):
        """ Function to find peak (through maximal palm speed) of reaching behavior. """

    def find_end_time(self):
        """ Function to find the end time of a given reach (from trajectory minimization) """
    def find_start_time(self):
        """ Function to find the tentative start time of a reach, given a definite positive threshold on a given palm. """
    def find_duration(self):
        """ Function to find the tentative duration of a reach, given a definite positive threshold on a given palm. """
    def find_grasp_peak(self):
        """ Find peak time of a given grasp using a palm speed thresholding. """
    def find_retract_times(self):
        """ Find total time to retract"""
    def find_retract_start(self):
        """ Find time retraction starts using handle data. """
    def find_retract_stop(self):
        """ Find time when retraction stops using handle data. """
    def find_lick_times(self):
        """ Find tentative reward-delivering times using a lick-o-meter sensor. """
