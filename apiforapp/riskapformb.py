


def cardiacapi(gen,d,check,color,heart):

    if gen == "Male" :
        if d["heart_score"] >= 20:
            d["heart_score"] = {
                "val": str(d["heart_score"]),
                "text": "diagnosed",
                "color": "black",
                "max": 21,
                "min": -10
            }
        elif d["heart_score"] == None:
            d["heart_score"] = {
                "val": "None",
                "text": check,
                "color": "black",
                "max": 21,
                "min": -10
            }
        else:

            d["heart_score"] = {
                "val": str(d["heart_score"]),
                "text": heart,
                "color": color,
                "max": 21,
                "min": -10
            }
    elif gen == "Female":
        if d["heart_score"] > 27:
            d["heart_score"] = {
                "val": str(d["heart_score"]),
                "text": "diagnosed",
                "color": "black",
                "max": 28,
                "min": -8
            }
        elif d["heart_score"] == None:
            d["heart_score"] = {
                "val": "None",
                "text": check,
                "color": "black",
                "max": 28,
                "min": -8
            }
        else:
            d["heart_score"] = {
                "val": str(d["heart_score"]),
                "text": heart,
                "color": color,
                "max": 28,
                "min": -8
            }
    return d["heart_score"]


def dabetiesapi(gen,d,check,color,diabet):
    print d,"hhyhyy"
    if d["diabetes_score"] > 10:
        d["diabetes_score"] = {
            "val": str(d["diabetes_score"]),
            "text": "diagnosed",
            "color": "black",
            "max":11,
            "min":0
        }
    elif d["diabetes_score"] == None:
        d["diabetes_score"] = {
            "val": "None",
            "text": check,
            "color": "black",
            "max": 11,
            "min": 0
        }
    else:
        d["diabetes_score"] = {
            "val": str(d["diabetes_score"]),
            "text": diabet,
            "color": color,
            "max": 11,
            "min": 0
        }
    return d["diabetes_score"]


def hyperapi(gen,d,check,color,hypers):

    if d["hyper_score"] >5:
        d["hyper_score"] = {
            "val": str(d["hyper_score"]),
            "text": "diagnosed",
            "color": "black",
            "max": 6,
            "min": 0
        }
    elif d["hyper_score"] == None:
        d["hyper_score"] = {
            "val": "None",
            "text": check,
            "color": "black",
            "max": 6,
            "min": 0
        }
    else:

        d["hyper_score"] = {
            "val": str(d["hyper_score"]),
            "text": hypers,
            "color": color,
            "max": 6,
            "min": 0
        }
    return d["hyper_score"]


