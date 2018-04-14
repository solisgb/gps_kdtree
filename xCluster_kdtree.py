# -*- coding: Latin-1 -*-
"""
Created on Sun Mar 25 14:23:56 2018

@author: solis
"""

import traceback
import logging

if __name__ == "__main__":

    try:
        import cluster_kdtree as ckdt

        gps_s, gps_all = ckdt.get_data()

        ii = ckdt.get_cluster(gps_s, gps_all)

        ckdt.write_clusters(gps_s, gps_all, ii)

        print('ok', end=' ')
    except Exception as e:
        logging.error(traceback.format_exc())
    finally:
        print('fin')
