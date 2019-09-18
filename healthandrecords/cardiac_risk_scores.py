def men_non(age, smoker, hdl_level,systolic, treated_for_systolic_bp, totalcholestoral):
    age_p = 0
    smoke_p = 0
    hdl_p = 0
    sys_p = 0
    tc_p = 0
    per_s = 0
    h_per = {1: (range(0, 5)), 2: (range(5, 7)), 3: (7, 7), 4: (8, 8), 5: (9, 9), 6: (10, 10), 8: (11, 11),
             10: (12, 12), 12: (13, 13), 16: (14, 14), 20: (15, 15), 25: (16, 16)}
    men_age_score = {-9: (range(15, 34 + 1)), -4: (range(35, 39 + 1)), 0: (range(40, 44 + 1)), 3: (range(45, 49 + 1)),
                     6: (range(50, 54 + 1)), 8: (range(55, 59 + 1)), 10: (range(60, 64 + 1)), 11: (range(65, 69 + 1)),
                     12: (range(70, 74 + 1)), 13: (range(75, 85 + 1))}
    men_smoke_score = {8: (range(15, 39 + 1)), 5: (range(40, 49 + 1)), 3: (range(50, 59 + 1)), 1: (range(60,  85 + 1))}
    men_hdl_score = {2: (range(40)), 1: (range(40, 50)), 0: (range(50, 60))}  # 60+ has to be included value -1
    men_sys_bp_un = {0: (range(120, 129 + 1)), 1: (range(130, 159 + 1))}  # 160+ has to be included 2
    men_sys_bp = {0: (range(120)), 1: (range(120, 129 + 1)),
                  2: (range(130, 159 + 1))}  # 160+ has to be included value 3
    tc_men20 = {0: (range(160)), 4: (range(160, 199 + 1)), 7: (range(200, 239 + 1)),
                9: (range(240, 270 + 1))}  # 280+ value 11
    tc_men40 = {0: (range(160)), 3: (range(160, 199 + 1)), 5: (range(200, 239 + 1)),
                6: (range(240, 270 + 1))}  # 280+ value 8
    tc_men50 = {0: (range(160)), 2: (range(160, 199 + 1)), 3: (range(200, 239 + 1)),
                4: (range(240, 270 + 1))}  # 280+ value 5
    tc_men60 = {0: (range(160)), 1: (range(160,  239 + 1)),
                2: (range(240, 270 + 1))}  # 280+ value 3
    tc_men70 = {0: (range(160, 239 + 1)),
                1: (range(240, 270 + 1))}  # 280+ value 1
    for age_points, age_range in men_age_score.iteritems():
        if age in age_range:
            age_p = age_points
    for smoke_points, smoker_age_range in men_smoke_score.iteritems():
        if age in smoker_age_range:
            if smoker == 'Yes':
                smoke_p = int(smoke_points)
            else:
                if smoker == 'No':
                    smoke_p = 0
    for hdl_points, hdl_range in men_hdl_score.iteritems():
        if (hdl_level) in hdl_range:
            hdl_p = hdl_points
        else:
            if (hdl_level) > 60:
                hdl_p = -1
    if treated_for_systolic_bp == 'Yes':
        for sys_points, sys_range in men_sys_bp.iteritems():
            if systolic in sys_range:
                sys_p = sys_points
            else:
                if systolic > 160:
                    sys_p = 3
    elif treated_for_systolic_bp == 'No':
        for sys_points, sys_range in men_sys_bp_un.iteritems():
            if systolic in sys_range:
                sys_p = sys_points
            else:
                if systolic > 160:
                    sys_p = 2
    if age in range(20, 39 + 1):
        for tc_points, tc_range in tc_men20.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 11
    elif age in range(40, 49 + 1):
        for tc_points, tc_range in tc_men40.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 8
    elif age in range(50, 59 + 1):
        for tc_points, tc_range in tc_men50.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 5
    elif age in range(60, 69 + 1):
        for tc_points, tc_range in tc_men60.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 3
    else:
        for tc_points, tc_range in tc_men70.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 1
    h_score = age_p + smoke_p + tc_p + hdl_p + sys_p
    # print h_score
    for i, j in h_per.iteritems():
        if h_score in j:
            per_s = i
        else:
            if h_score >= 17:
                per_s = 30
    print h_score, per_s


    return h_score, per_s


# women
def women_non(age, smoker, hdl_level,systolic, treated_for_systolic_bp, totalcholestoral):
    age_p = 0
    smoke_p = 0
    hdl_p = 0
    sys_p = 0
    tc_p = 0
    per_s=0
    h_per = {1: (range(0, 13)), 2: (range(13, 15)), 3: (15, 15), 4: (16, 16), 5: (17, 17), 6: (18, 18), 8: (19, 19),
             11: (20, 20), 14: (21, 21), 17: (22, 22), 22: (23, 23), 27: (24, 24)}
    women_age_score = {-7: (range(15, 34 + 1)), -3: (range(35, 39 + 1)), 0: (range(40, 44 + 1)), 3: (range(45, 49 + 1)),
                       6: (range(50, 54 + 1)), 8: (range(55, 59 + 1)), 10: (range(60, 64 + 1)), 12: (range(65, 69 + 1)),
                       14: (range(70, 74 + 1)), 16: (range(75, 85 + 1))}
    women_smoke_score = {9: (range(15, 39 + 1)), 7: (range(40, 49 + 1)), 4: (range(50, 59 + 1)), 2: (range(60, 69 + 1)),
                         1: (range(70, 85 + 1))}
    women_hdl_score = {0: (range(50, 60)), 1: (range(40, 50)), 2: (range(40))}  # 60+ has to be included value -1
    women_sys_bp_un = {0: (range(120)), 1: (range(120, 129 + 1)), 2: (range(130, 139 + 1)),
                       3: (range(140, 159 + 1))}  # 160+ has to be included value 4
    women_sys_bp = {0: (range(120)), 3: (range(120, 129 + 1)), 4: (range(130, 139 + 1)),
                    5: (range(140, 159 + 1))}  # 160+ has to be included value 6
    tc_women20 = {0: (range(160)), 4: (range(160, 199 + 1)), 8: (range(200, 239 + 1)),
                  11: (range(240, 270 + 1))}  # 280+ value 13
    tc_women40 = {0: (range(160)), 3: (range(160, 199 + 1)), 6: (range(200, 239 + 1)),
                  8: (range(240, 270 + 1))}  # 280+ value 10
    tc_women50 = {0: (range(160)), 2: (range(160, 199 + 1)), 4: (range(200, 239 + 1)),
                  5: (range(240, 270 + 1))}  # 280+ value 7
    tc_women60 = {0: (range(160)), 1: (range(160, 199 + 1)), 2: (range(200, 239 + 1)),
                  3: (range(240, 270 + 1))}  # 280+ value 4
    tc_women70 = {0: (range(160)), 1: (range(160, 239 + 1)),
                  2: (range(240, 270 + 1))}  # 280+ value 2
    for age_points, age_range in women_age_score.iteritems():
        if age in age_range:
            age_p = age_points
    for smoke_points, smoker_age_range in women_smoke_score.iteritems():
        if age in smoker_age_range:
            if smoker == 'Yes':
                smoke_p = smoke_points

            else:
                smoke_p = 0

    for hdl_points, hdl_range in women_hdl_score.iteritems():
        if  hdl_level in hdl_range:
            hdl_p = hdl_points

        else:
            if  hdl_level > 60:
                hdl_p = -1
                # print hdl_p
    if treated_for_systolic_bp == 'Yes':
        for sys_points, sys_range in women_sys_bp.iteritems():
            if systolic in sys_range:
                sys_p = sys_points

            else:
                if systolic > 160:
                    sys_p = 6

    elif treated_for_systolic_bp == 'No':
        for sys_points, sys_range in women_sys_bp_un.iteritems():
            if systolic in sys_range:
                sys_p = sys_points
            else:
                if systolic > 160:
                    sys_p = 4
    if age in range(20, 39 + 1):
        for tc_points, tc_range in tc_women20.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 13
    elif age in range(40, 49 + 1):
        for tc_points, tc_range in tc_women40.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 10
    elif age in range(50, 59 + 1):
        for tc_points, tc_range in tc_women50.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 7
    elif age in range(60, 69 + 1):
        for tc_points, tc_range in tc_women60.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 4
    else:
        for tc_points, tc_range in tc_women70.iteritems():
            if totalcholestoral in tc_range:
                tc_p = tc_points
            else:
                if totalcholestoral > 280:
                    tc_p = 2
    h_score = age_p + smoke_p + tc_p + hdl_p + sys_p
    for i, j in h_per.iteritems():
        if h_score in j:
            per_s = i
        else:
            if h_score >= 24:
                per_s = 30
    print h_score, per_s
    #print age_p, smoke_p, hdl_p, sys_p, tc_p
    return h_score, per_s


# men_dia
def gender_1(gender, age, smoker,  hdl_level, systolic, treated_for_systolic_bp, totalcholestoral):
    # gender,age,smoker, hdl_level,systolictreat,tc=gender,age,smoker,hdl,systolic,treat,tc
    if gender == 'Male':
        h_score, per_s = men_non(age, smoker,  hdl_level, systolic, treated_for_systolic_bp, totalcholestoral)
        print h_score, per_s
        return h_score, per_s
    else:
        if gender == 'Female':
            h_score, per_s = women_non(age, smoker, hdl_level,systolic, treated_for_systolic_bp, totalcholestoral)
            print h_score, per_s
            return h_score, per_s


def hyper(age, smoker, systolic, waist_circumference, gender):
     agr = ''
     smokr = ''
     bpr = ''
     waistr = ''
     if age >= 35:
         apr = 2
     else:
         apr = 0
     # print apr,"hyper gae"
     if smoker == 'Yes':
         smokr = 1
     else:
         smokr = 0
     print smokr, "smokr gae"
     if systolic > 140:
         bpr = 1
     else:
         bpr = 0
     print bpr, "bpr gae"
     if gender == 'Male':
         if waist_circumference >= 85:
             waistr = 1
         else:
             waistr = 0
     else:
         if gender == 'Female' and waist_circumference >= 80:
             waistr = 1
         else:
             waistr = 0
     print waistr,waist_circumference, "waistr",apr ,'agerp', smokr,'smoker' , bpr ,'prehypt',systolic
     return apr + smokr + bpr + waistr
    # for score_points,score_range in
# newlist=[['Male',24,'Yes',65,130,'Yes',160],['Male',24,'No',65,130,'Yes',160],['Male',24,'Yes',65,130,'Yes',160],['Male',24,'Yes',65,130,'Yes',160],
#          ['Female',64,'No',65,130,'Yes',160],['Male',24,'No',65,130,'Yes',160],['Male',24,'No',65,130,'Yes',160],['Male',24,'Yes',65,130,'Yes',160],
#          ['Male',24,'Yes',65,130,'Yes',160],['Female',54,'No',65,130,'Yes',160]]

