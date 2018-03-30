import cv2
import numpy
import math
from enum import Enum

class GripPipeline:
    """
    An OpenCV pipeline generated by GRIP.
    """
    
    def __init__(self):
        """initializes all values to presets or None if need to be set
        """

        self.__cv_resize_dsize = (0, 0)
        self.__cv_resize_fx = 0.5
        self.__cv_resize_fy = 0.5
        self.__cv_resize_interpolation = cv2.INTER_LINEAR

        self.cv_resize_output = None

        '''self.__hsl_threshold_input = self.cv_resize_output
        self.__hsl_threshold_hue = [63.12949640287769, 100.13651877133105]
        self.__hsl_threshold_saturation = [190.33273381294964, 255.0]
        self.__hsl_threshold_luminance = [82.55395683453236, 255.0]'''
        
        self.__hsl_threshold_input = self.cv_resize_output
        self.__hsl_threshold_hue = [63, 96]
        self.__hsl_threshold_saturation = [163.33273381294964, 255.0]
        self.__hsl_threshold_luminance = [0, 255.0]

        self.hsl_threshold_output = None

        self.__find_contours_input = self.hsl_threshold_output
        self.__find_contours_external_only = False

        self.find_contours_output = None
        '''self.__filter_contours_contours = self.find_contours_output
        self.__filter_contours_min_area = 0.0
        self.__filter_contours_min_perimeter = 5.0
        self.__filter_contours_min_width = 0.0
        self.__filter_contours_max_width = 50.0
        self.__filter_contours_min_height = 1.0
        self.__filter_contours_max_height = 100.0
        self.__filter_contours_solidity = [87.23021582733814, 100]
        self.__filter_contours_max_vertices = 100.0
        self.__filter_contours_min_vertices = 5.0
        self.__filter_contours_min_ratio = 0.2
        self.__filter_contours_max_ratio = 5.0'''
        self.__filter_contours_contours = self.find_contours_output
        self.__filter_contours_min_area = 33
        self.__filter_contours_min_perimeter = 11.0
        self.__filter_contours_min_width = 2.0
        self.__filter_contours_max_width = 50.0
        self.__filter_contours_min_height =4.0 
        self.__filter_contours_max_height = 100.0
        self.__filter_contours_solidity = [87.23021582733814, 100]
        self.__filter_contours_max_vertices = 10.0
        self.__filter_contours_min_vertices = 4.0
        self.__filter_contours_min_ratio = 0.2
        self.__filter_contours_max_ratio = 5.0

        self.filter_contours_output = None


    def process(self, source0):
        """
        Runs the pipeline and sets all outputs to new values.
        """
        # Step CV_resize0:
        self.__cv_resize_src = source0
        (self.cv_resize_output) = self.__cv_resize(self.__cv_resize_src, self.__cv_resize_dsize, self.__cv_resize_fx, self.__cv_resize_fy, self.__cv_resize_interpolation)

        # Step HSL_Threshold0:
        self.__hsl_threshold_input = self.cv_resize_output
        (self.hsl_threshold_output) = self.__hsl_threshold(self.__hsl_threshold_input, self.__hsl_threshold_hue, self.__hsl_threshold_saturation, self.__hsl_threshold_luminance)

        # Step Find_Contours0:
        self.__find_contours_input = self.hsl_threshold_output
        (self.find_contours_output) = self.__find_contours(self.__find_contours_input, self.__find_contours_external_only)

        # Step Filter_Contours0:
        self.__filter_contours_contours = self.find_contours_output
        (self.filter_contours_output) = self.__filter_contours(self.__filter_contours_contours, self.__filter_contours_min_area, self.__filter_contours_min_perimeter, self.__filter_contours_min_width, self.__filter_contours_max_width, self.__filter_contours_min_height, self.__filter_contours_max_height, self.__filter_contours_solidity, self.__filter_contours_max_vertices, self.__filter_contours_min_vertices, self.__filter_contours_min_ratio, self.__filter_contours_max_ratio)


    @staticmethod
    def __cv_resize(src, d_size, fx, fy, interpolation):
        """Resizes an Image.
        Args:
            src: A numpy.ndarray.
            d_size: Size to set the image.
            fx: The scale factor for the x.
            fy: The scale factor for the y.
            interpolation: Opencv enum for the type of interpolation.
        Returns:
            A resized numpy.ndarray.
        """
        return cv2.resize(src, d_size, fx=fx, fy=fy, interpolation=interpolation)

    @staticmethod
    def __hsl_threshold(input, hue, sat, lum):
        """Segment an image based on hue, saturation, and luminance ranges.
        Args:
            input: A BGR numpy.ndarray.
            hue: A list of two numbers the are the min and max hue.
            sat: A list of two numbers the are the min and max saturation.
            lum: A list of two numbers the are the min and max luminance.
        Returns:
            A black and white numpy.ndarray.
        """
        out = cv2.cvtColor(input, cv2.COLOR_BGR2HLS)
        return cv2.inRange(out, (hue[0], lum[0], sat[0]),  (hue[1], lum[1], sat[1]))

    @staticmethod
    def __find_contours(input, external_only):
        """Sets the values of pixels in a binary image to their distance to the nearest black pixel.
        Args:
            input: A numpy.ndarray.
            external_only: A boolean. If true only external contours are found.
        Return:
            A list of numpy.ndarray where each one represents a contour.
        """
        if(external_only):
            mode = cv2.RETR_EXTERNAL
        else:
            mode = cv2.RETR_LIST
        method = cv2.CHAIN_APPROX_SIMPLE
        im2, contours, hierarchy =cv2.findContours(input, mode=mode, method=method)
        return contours

    @staticmethod
    def __filter_contours(input_contours, min_area, min_perimeter, min_width, max_width,
                        min_height, max_height, solidity, max_vertex_count, min_vertex_count,
                        min_ratio, max_ratio):
        """Filters out contours that do not meet certain criteria.
        Args:
            input_contours: Contours as a list of numpy.ndarray.
            min_area: The minimum area of a contour that will be kept.
            min_perimeter: The minimum perimeter of a contour that will be kept.
            min_width: Minimum width of a contour.
            max_width: MaxWidth maximum width.
            min_height: Minimum height.
            max_height: Maximimum height.
            solidity: The minimum and maximum solidity of a contour.
            min_vertex_count: Minimum vertex Count of the contours.
            max_vertex_count: Maximum vertex Count.
            min_ratio: Minimum ratio of width to height.
            max_ratio: Maximum ratio of width to height.
        Returns:
            Contours as a list of numpy.ndarray.
        """
        output = []
        for contour in input_contours:
            x,y,w,h = cv2.boundingRect(contour)
            #if (w < min_width or w > max_width):
            #    continue
            #if (h < min_height or h > max_height):
            #    continue
            area = cv2.contourArea(contour)
            #if (area < min_area):
            #    continue
            #if (cv2.arcLength(contour, True) < min_perimeter):
            #    continue
            hull = cv2.convexHull(contour)
        hullArea = cv2.contourArea(hull)
        #if hullArea != 0:
        try:
            solid = 100 * area / hullArea
        except:
            solid = 100*area

        #else:
	    #	 solid = 0
            #if (solid < solidity[0] or solid > solidity[1]):
            #    continue
            #if (len(contour) < min_vertex_count or len(contour) > max_vertex_count):
            #    continue
            ratio = (float)(w) / h
            #if (ratio < min_ratio or ratio > max_ratio):
            #    continue
            output.append(contour)
        return output



