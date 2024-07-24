from TuLuan_question4_3 import list_x_name
import numpy as np

def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]

# Kiểm tra hàm get_index_from_value
outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

print(i1, i2, i3)
