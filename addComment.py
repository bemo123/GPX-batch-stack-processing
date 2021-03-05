# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:35:38 2021

@author: Benedikt
"""

import gpxpy
import os

def main():
    GPX_files = glob('*.gpx')
    for GPX_file in GPX_files:

            #print('reading '+GPX_file+'...')
            gpx_file = gpxpy.parse(open(GPX_file))
            
            #add comment
            cmt = 'YOUR COMMENT'
            gpx_file.tracks[0].comment = cmt
            
            #write updatedfile to output folder
            output_path = 'output/'
            output_file = GPX_file #[:-4]+'_modified.gpx'
            with open(os.path.join(output_path + output_file), 'w') as fh: 
                fh.write(gpx_file.to_xml())

            #print('done')
         
if __name__ == '__main__':
    from glob import glob
    main()

