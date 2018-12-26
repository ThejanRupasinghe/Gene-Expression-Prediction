from datetime import datetime

def generate_submission(predictions, name):
    date = datetime.now().strftime('%m-%d-%H_%M_%S')
    fp = open("../submissions/" + name + "_" + date + ".csv", "w")
    fp.write("GeneId,Prediction\n")
    for idx, prediction in enumerate(predictions, 1):
        fp.write("%i,%f\n" % ((idx), prediction))
    fp.close()
