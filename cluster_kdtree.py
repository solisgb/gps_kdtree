# -*- coding: Latin-1 -*-
"""
Created on Sun Mar 25 17:58:36 2018

@author: solis

"""

import numpy as np
from scipy import spatial
import pyodbc
import cluster_kdtree_parameters as par


def get_data():
    """
    retrieve data from DB
    """
    from db_con_str import con_str

    cstr = con_str(par.DB)
    con = pyodbc.connect(cstr)
    cur = con.cursor()
    cur.execute(par.SELECT_PS)
    gps_s = [[row.ID, row.FECHA, row.Z, row.NOMBRE, row.X,
              row.Y] for row in cur]

    cur.execute(par.SELECT_D)
    gps_all = [[row.ID, row.FECHA, row.Z, row.NOMBRE, row.X,
                row.Y] for row in cur]

    cur.close()
    con.close()

    return gps_s, gps_all


def get_cluster(gps_s, gps_all):
    """
    get cluster using kdtree algorithm
    """
    if len(gps_s) == 0:
        raise ValueError('len(gps_s) = 0')
    if len(gps_all) == 0:
        raise ValueError('len(gps_all) = 0')
    xy_d = np.array([[row[4], row[5]] for row in gps_all], dtype=np.float64)
    tree = spatial.cKDTree(xy_d)
    xy_s = np.array([[row[4], row[5]] for row in gps_s], dtype=np.float64)
    ii = tree.query_ball_point(xy_s, par.DISTANCE)
    return ii


def write_clusters(gps_s, gps_all, ii):
    """escribe los resultados"""
    from os.path import join
    fo = open(join(par.DIR_OUT, par.F_OUT), 'w', par.BUFSIZE)
    for id1, row in enumerate(ii):
        for j in row:
            fo.write('{0:d}\t{1:d}\t{2}\t{3:0.2f}\t{4}\t{5:0.2f}\t{6:0.2f}\n'
                     .format(id1, gps_all[j][0],
                             gps_all[j][1].strftime('%d/%m/%Y'),
                             gps_all[j][2],
                             gps_all[j][3],
                             gps_all[j][4], gps_all[j][5]))
    fo.flush()
    fo.close()
